"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";

/**
 * Root page now redirects to /chat.
 * Handles backward compatibility for /?session=xxx URLs.
 */
export default function HomePage() {
  const router = useRouter();

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const sessionId = params.get("session");
    const capability = params.get("capability");
    const tools = params.getAll("tool");

    let target = sessionId ? `/chat/${sessionId}` : "/chat";

    const query: string[] = [];
    if (capability) query.push(`capability=${encodeURIComponent(capability)}`);
    tools.forEach((t) => query.push(`tool=${encodeURIComponent(t)}`));
    if (query.length) target += `?${query.join("&")}`;

    router.replace(target);
  }, [router]);

  const schema = {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "DeepTutor",
    "applicationCategory": "EducationalApplication",
    "description": "AI-powered intelligent learning companion for personalized tutoring and adaptive learning.",
    "offers": {
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "USD"
    },
    "featureList": [
      "Personalized tutoring",
      "Adaptive learning paths",
      "Interactive lessons",
      "Homework help",
      "Test preparation"
    ]
  };

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }}
      />
    </>
  );
}
