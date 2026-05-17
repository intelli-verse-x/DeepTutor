import type { Metadata } from "next";
import { Plus_Jakarta_Sans, Lora } from "next/font/google";
import "./globals.css";
import ThemeScript from "@/components/ThemeScript";
import { AppShellProvider } from "@/context/AppShellContext";
import { I18nClientBridge } from "@/i18n/I18nClientBridge";

const fontSans = Plus_Jakarta_Sans({
  subsets: ["latin"],
  display: "swap",
  variable: "--font-sans",
});

const fontSerif = Lora({
  subsets: ["latin"],
  display: "swap",
  variable: "--font-serif",
});

export const metadata: Metadata = {
  title: 'DeepTutor | AI-Powered Intelligent Learning Companion',
  description: 'Agent-native intelligent learning companion powered by AI. Personalized tutoring, adaptive learning paths, and interactive lessons for students. Get help with homework, test prep, and concept mastery.',
  metadataBase: new URL('https://tutor.intelli-verse-x.ai'),
  alternates: {
    canonical: '/',
  },
  openGraph: {
    title: 'DeepTutor | AI Learning Companion',
    description: 'Intelligent tutoring system powered by AI for personalized education.',
    url: 'https://tutor.intelli-verse-x.ai',
    siteName: 'DeepTutor',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'DeepTutor | AI Learning Companion',
    description: 'Personalized AI tutoring for students.',
  },
  robots: {
    index: true,
    follow: true,
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning className={`${fontSans.variable} ${fontSerif.variable}`}>
      <head>
        <ThemeScript />
      </head>
      <body className="font-sans bg-[var(--background)] text-[var(--foreground)]">
        <AppShellProvider>
          <I18nClientBridge>
            {children}
          </I18nClientBridge>
        </AppShellProvider>
      </body>
    </html>
  );
}
