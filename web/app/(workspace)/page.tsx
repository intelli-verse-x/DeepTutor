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

  const faqSchema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is DeepTutor?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "DeepTutor is an AI-powered intelligent learning companion that provides personalized tutoring, adaptive learning paths, and interactive lessons. It helps students with homework, test preparation, and concept mastery through step-by-step AI guidance."
        }
      },
      {
        "@type": "Question",
        "name": "How does DeepTutor personalize learning?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "DeepTutor uses adaptive AI algorithms to understand each student's learning style, pace, and knowledge gaps. It creates customized learning paths and adjusts difficulty levels based on student performance and progress."
        }
      },
      {
        "@type": "Question",
        "name": "What subjects does DeepTutor cover?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "DeepTutor covers a wide range of subjects including mathematics, science, language arts, social studies, and more. The AI tutor can help with homework questions, concept explanations, and test preparation across multiple grade levels."
        }
      }
    ]
  };

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(faqSchema) }}
      />
    </>
  );
}
