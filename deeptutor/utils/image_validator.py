"""
Image Validation Utilities
===========================

Production-ready image validation for API endpoints.
Validates size, format, dimensions, and content safety.
"""

import base64
import io
from typing import Literal

from PIL import Image

from deeptutor.logging import get_logger

logger = get_logger("ImageValidator")


class ImageValidationError(Exception):
    """Raised when image validation fails."""
    pass


# Configuration
MAX_IMAGE_SIZE_BYTES = 10 * 1024 * 1024  # 10MB
MAX_IMAGE_WIDTH = 4096
MAX_IMAGE_HEIGHT = 4096
MIN_IMAGE_WIDTH = 50
MIN_IMAGE_HEIGHT = 50

ALLOWED_FORMATS = {"JPEG", "PNG", "GIF", "WEBP", "BMP"}


def validate_image_for_api(
    image_base64: str | None,
    max_size_mb: float = 10.0,
    allowed_formats: set[str] | None = None,
) -> dict[str, any]:
    """
    Validate image for API usage.
    
    Args:
        image_base64: Base64 encoded image string
        max_size_mb: Maximum allowed size in megabytes
        allowed_formats: Set of allowed image formats (PIL format names)
        
    Returns:
        dict with validation results and image metadata
        
    Raises:
        ImageValidationError: If validation fails
    """
    if not image_base64:
        raise ImageValidationError("No image provided")
    
    # Strip data URL prefix if present
    if image_base64.startswith("data:"):
        # Extract base64 part after comma
        try:
            image_base64 = image_base64.split(",", 1)[1]
        except IndexError:
            raise ImageValidationError("Invalid data URL format")
    
    # Validate base64 string
    try:
        image_bytes = base64.b64decode(image_base64)
    except Exception as e:
        raise ImageValidationError(f"Invalid base64 encoding: {str(e)}")
    
    # Check size
    size_bytes = len(image_bytes)
    max_size_bytes = int(max_size_mb * 1024 * 1024)
    
    if size_bytes > max_size_bytes:
        size_mb = size_bytes / (1024 * 1024)
        raise ImageValidationError(
            f"Image too large: {size_mb:.2f}MB (max: {max_size_mb}MB). "
            "Please compress or resize the image."
        )
    
    if size_bytes == 0:
        raise ImageValidationError("Image is empty")
    
    # Validate image format and dimensions
    try:
        image = Image.open(io.BytesIO(image_bytes))
        
        # Get format
        image_format = image.format
        if not image_format:
            raise ImageValidationError("Unable to determine image format")
        
        # Check allowed formats
        formats = allowed_formats or ALLOWED_FORMATS
        if image_format.upper() not in formats:
            raise ImageValidationError(
                f"Unsupported image format: {image_format}. "
                f"Allowed formats: {', '.join(formats)}"
            )
        
        # Check dimensions
        width, height = image.size
        
        if width > MAX_IMAGE_WIDTH or height > MAX_IMAGE_HEIGHT:
            raise ImageValidationError(
                f"Image dimensions too large: {width}x{height}px "
                f"(max: {MAX_IMAGE_WIDTH}x{MAX_IMAGE_HEIGHT}px)"
            )
        
        if width < MIN_IMAGE_WIDTH or height < MIN_IMAGE_HEIGHT:
            raise ImageValidationError(
                f"Image dimensions too small: {width}x{height}px "
                f"(min: {MIN_IMAGE_WIDTH}x{MIN_IMAGE_HEIGHT}px)"
            )
        
        # Check if image is corrupted
        try:
            image.verify()
        except Exception as e:
            raise ImageValidationError(f"Image appears to be corrupted: {str(e)}")
        
        # Return validation results
        return {
            "valid": True,
            "format": image_format,
            "size_bytes": size_bytes,
            "size_mb": round(size_bytes / (1024 * 1024), 2),
            "width": width,
            "height": height,
            "mode": image.mode,
        }
        
    except ImageValidationError:
        raise
    except Exception as e:
        raise ImageValidationError(f"Failed to process image: {str(e)}")


def sanitize_image_base64(image_base64: str) -> str:
    """
    Sanitize and normalize base64 image string.
    
    Args:
        image_base64: Base64 encoded image (with or without data URL prefix)
        
    Returns:
        Clean base64 string without data URL prefix
    """
    if not image_base64:
        return image_base64
    
    # Remove data URL prefix
    if image_base64.startswith("data:"):
        try:
            image_base64 = image_base64.split(",", 1)[1]
        except IndexError:
            pass
    
    # Remove whitespace
    return image_base64.strip()


def get_image_info(image_base64: str) -> dict[str, any]:
    """
    Get information about an image without full validation.
    
    Args:
        image_base64: Base64 encoded image string
        
    Returns:
        Dictionary with image metadata
    """
    try:
        # Sanitize
        clean_base64 = sanitize_image_base64(image_base64)
        
        # Decode
        image_bytes = base64.b64decode(clean_base64)
        
        # Open image
        image = Image.open(io.BytesIO(image_bytes))
        
        return {
            "format": image.format,
            "size_bytes": len(image_bytes),
            "size_mb": round(len(image_bytes) / (1024 * 1024), 2),
            "width": image.size[0],
            "height": image.size[1],
            "mode": image.mode,
        }
    except Exception as e:
        logger.warning(f"Failed to get image info: {e}")
        return {}


def compress_image_if_needed(
    image_base64: str,
    max_size_mb: float = 5.0,
    quality: int = 85,
) -> tuple[str, bool]:
    """
    Compress image if it exceeds size limit.
    
    Args:
        image_base64: Base64 encoded image
        max_size_mb: Maximum size in MB
        quality: JPEG quality (1-100)
        
    Returns:
        Tuple of (compressed_base64, was_compressed)
    """
    try:
        # Sanitize
        clean_base64 = sanitize_image_base64(image_base64)
        
        # Check current size
        image_bytes = base64.b64decode(clean_base64)
        current_size_mb = len(image_bytes) / (1024 * 1024)
        
        if current_size_mb <= max_size_mb:
            return image_base64, False
        
        # Compress
        image = Image.open(io.BytesIO(image_bytes))
        
        # Convert to RGB if needed (for JPEG)
        if image.mode in ("RGBA", "LA", "P"):
            # Create white background
            background = Image.new("RGB", image.size, (255, 255, 255))
            if image.mode == "P":
                image = image.convert("RGBA")
            background.paste(image, mask=image.split()[-1] if image.mode in ("RGBA", "LA") else None)
            image = background
        
        # Compress to JPEG
        output = io.BytesIO()
        image.save(output, format="JPEG", quality=quality, optimize=True)
        compressed_bytes = output.getvalue()
        
        # Encode back to base64
        compressed_base64 = base64.b64encode(compressed_bytes).decode('utf-8')
        
        new_size_mb = len(compressed_bytes) / (1024 * 1024)
        logger.info(f"Compressed image: {current_size_mb:.2f}MB -> {new_size_mb:.2f}MB")
        
        return f"data:image/jpeg;base64,{compressed_base64}", True
        
    except Exception as e:
        logger.error(f"Failed to compress image: {e}")
        return image_base64, False


def prepare_image_for_vision_llm(
    image_base64: str,
    max_dimension: int = 2048,
    max_size_mb: float = 2.0,
    jpeg_quality: int = 85,
) -> tuple[str, bool]:
    """
    Resize and compress images before vision LLM calls (faster uploads + inference).

    Returns:
        Tuple of (data URI string, whether the image was modified)
    """
    if not image_base64:
        return image_base64, False

    try:
        if image_base64.startswith("data:"):
            _, _, clean_base64 = image_base64.partition(",")
        else:
            clean_base64 = image_base64

        image_bytes = base64.b64decode(clean_base64)
        image = Image.open(io.BytesIO(image_bytes))
        original_size_mb = len(image_bytes) / (1024 * 1024)
        width, height = image.size
        modified = False

        if max(width, height) > max_dimension:
            image.thumbnail((max_dimension, max_dimension), Image.Resampling.LANCZOS)
            modified = True
            logger.info(
                "Resized image for vision: %sx%s -> %sx%s",
                width,
                height,
                image.size[0],
                image.size[1],
            )

        if image.mode in ("RGBA", "LA", "P"):
            background = Image.new("RGB", image.size, (255, 255, 255))
            if image.mode == "P":
                image = image.convert("RGBA")
            background.paste(
                image,
                mask=image.split()[-1] if image.mode in ("RGBA", "LA") else None,
            )
            image = background
            modified = True
        elif image.mode != "RGB":
            image = image.convert("RGB")
            modified = True

        output = io.BytesIO()
        image.save(output, format="JPEG", quality=jpeg_quality, optimize=True)
        compressed_bytes = output.getvalue()
        compressed_mb = len(compressed_bytes) / (1024 * 1024)

        if compressed_mb > max_size_mb:
            for quality in (75, 65, 55):
                output = io.BytesIO()
                image.save(output, format="JPEG", quality=quality, optimize=True)
                compressed_bytes = output.getvalue()
                compressed_mb = len(compressed_bytes) / (1024 * 1024)
                if compressed_mb <= max_size_mb:
                    break
            modified = True

        if (
            not modified
            and original_size_mb <= max_size_mb
            and image_base64.startswith("data:image/jpeg")
        ):
            return image_base64, False

        b64 = base64.b64encode(compressed_bytes).decode("utf-8")
        logger.info(
            "Prepared image for vision: %.2fMB -> %.2fMB (%sx%s)",
            original_size_mb,
            compressed_mb,
            image.size[0],
            image.size[1],
        )
        return f"data:image/jpeg;base64,{b64}", True

    except Exception as e:
        logger.warning("prepare_image_for_vision_llm failed, using original: %s", e)
        return image_base64, False
