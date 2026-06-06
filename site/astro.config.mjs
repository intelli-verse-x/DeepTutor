// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

// i18n — English is the source-of-truth locale. Chinese pages live under
// `src/content/docs/zh-cn/` mirroring the English structure. Pages not yet
// translated fall back to English automatically.
const zh = "zh-CN";

export default defineConfig({
  site: "https://deeptutor.info",
  redirects: {
    "/docs/developer/contributing/": "/docs/contributing/",
    "/zh-cn/docs/developer/contributing/": "/zh-cn/docs/contributing/",
  },
  integrations: [
    starlight({
      title: "DeepTutor",
      description: "Agent-native, open-source personalized tutoring.",
      defaultLocale: "root",
      locales: {
        root: { label: "English", lang: "en" },
        "zh-cn": { label: "简体中文", lang: "zh-CN" },
      },
      logo: {
        src: "./src/assets/logo.png",
        replacesTitle: false,
      },
      customCss: ["./src/styles/global.css", "./src/styles/starlight.css"],
      components: {
        SiteTitle: "./src/components/SiteTitle.astro",
        SocialIcons: "./src/components/SocialIcons.astro",
      },
      social: [
        {
          icon: "github",
          label: "GitHub",
          href: "https://github.com/HKUDS/DeepTutor",
        },
        {
          icon: "discord",
          label: "Discord",
          href: "https://discord.gg/eRsjPgMU4t",
        },
      ],
      sidebar: [
        {
          label: "Overview",
          translations: { [zh]: "总览" },
          items: [
            {
              label: "Documentation home",
              translations: { [zh]: "文档主页" },
              slug: "docs",
            },
            {
              label: "Contributing",
              translations: { [zh]: "参与贡献" },
              slug: "docs/contributing",
            },
          ],
        },
        {
          label: "Get Started",
          translations: { [zh]: "快速上手" },
          items: [
            {
              label: "Overview",
              translations: { [zh]: "概览" },
              slug: "docs/get-started",
            },
            {
              label: "1 · Install from PyPI",
              translations: { [zh]: "1 · PyPI 安装" },
              slug: "docs/get-started/pypi",
            },
            {
              label: "2 · Install from Source",
              translations: { [zh]: "2 · 源码安装" },
              slug: "docs/get-started/from-source",
            },
            {
              label: "3 · Docker",
              translations: { [zh]: "3 · Docker" },
              slug: "docs/get-started/docker",
            },
            {
              label: "4 · CLI-Only Install",
              translations: { [zh]: "4 · 纯 CLI 安装" },
              slug: "docs/get-started/cli-only",
            },
            {
              label: "Multi-User Deployment",
              translations: { [zh]: "多用户部署" },
              slug: "docs/get-started/multi-user",
            },
            {
              label: "Providers",
              translations: { [zh]: "模型与搜索提供商" },
              slug: "docs/get-started/providers",
            },
            {
              label: "Troubleshooting",
              translations: { [zh]: "故障排查" },
              slug: "docs/get-started/troubleshooting",
            },
          ],
        },
        {
          label: "Explore DeepTutor",
          translations: { [zh]: "探索 DeepTutor" },
          items: [
            {
              label: "Overview",
              translations: { [zh]: "概览" },
              slug: "docs/explore",
            },
            {
              label: "Chat Workspace",
              translations: { [zh]: "聊天工作台" },
              slug: "docs/explore/chat-workspace",
            },
            {
              label: "Co-Writer",
              translations: { [zh]: "Co-Writer 协同写作" },
              slug: "docs/explore/co-writer",
            },
            {
              label: "Book Engine",
              translations: { [zh]: "Book Engine" },
              slug: "docs/explore/book",
            },
            {
              label: "Knowledge",
              translations: { [zh]: "知识库" },
              slug: "docs/explore/knowledge",
            },
            {
              label: "Space",
              translations: { [zh]: "Space 空间" },
              slug: "docs/explore/space",
            },
            {
              label: "Memory",
              translations: { [zh]: "记忆系统" },
              slug: "docs/explore/memory",
            },
            {
              label: "Settings",
              translations: { [zh]: "设置" },
              slug: "docs/explore/settings",
            },
          ],
        },
        {
          label: "Explore TutorBot",
          translations: { [zh]: "TutorBot 渠道" },
          items: [
            {
              label: "Overview",
              translations: { [zh]: "概览" },
              slug: "docs/tutorbot",
            },
            { label: "Telegram", slug: "docs/tutorbot/telegram" },
            { label: "Discord", slug: "docs/tutorbot/discord" },
            { label: "Slack", slug: "docs/tutorbot/slack" },
            { label: "Matrix", slug: "docs/tutorbot/matrix" },
            { label: "Zulip", slug: "docs/tutorbot/zulip" },
            {
              label: "Feishu / Lark",
              translations: { [zh]: "飞书 / Lark" },
              slug: "docs/tutorbot/feishu",
            },
            {
              label: "WeCom",
              translations: { [zh]: "企业微信" },
              slug: "docs/tutorbot/wecom",
            },
            {
              label: "DingTalk",
              translations: { [zh]: "钉钉" },
              slug: "docs/tutorbot/dingtalk",
            },
            { label: "QQ", slug: "docs/tutorbot/qq" },
            { label: "WhatsApp", slug: "docs/tutorbot/whatsapp" },
            {
              label: "Email",
              translations: { [zh]: "电子邮件" },
              slug: "docs/tutorbot/email",
            },
            { label: "Mochat", slug: "docs/tutorbot/mochat" },
          ],
        },
        {
          label: "DeepTutor CLI",
          translations: { [zh]: "DeepTutor CLI" },
          items: [
            {
              label: "Overview",
              translations: { [zh]: "概览" },
              slug: "docs/cli",
            },
            {
              label: "Command Reference",
              translations: { [zh]: "命令参考" },
              slug: "docs/cli/commands",
            },
            {
              label: "Interactive REPL",
              translations: { [zh]: "交互式 REPL" },
              slug: "docs/cli/chat-repl",
            },
            {
              label: "Agent Handoff",
              translations: { [zh]: "代理交接" },
              slug: "docs/cli/agent-handoff",
            },
            {
              label: "Server API",
              translations: { [zh]: "服务端 API" },
              slug: "docs/cli/server-api",
            },
          ],
        },
      ],
    }),
  ],
});
