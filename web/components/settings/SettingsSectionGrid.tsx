"use client";

import { useCallback, useEffect, useState } from "react";
import Link from "next/link";
import { useTranslation } from "react-i18next";
import { ArrowUpRight } from "lucide-react";

import { fetchAuthStatus } from "@/lib/auth";
import {
  getActiveModel,
  getActiveProfile,
  useSettings,
} from "@/components/settings/SettingsContext";
import {
  SETTINGS_CATEGORIES,
  type Lang,
  type SettingsLeaf,
} from "@/lib/settings-nav";

/**
 * Second-level grid for a sub-hub category (Models, Chat). Lists the
 * category's leaves as tiles — colored icon, configured chip for model
 * services, and a blurb — the focused view the user reaches by clicking the
 * hub block.
 */
export default function SettingsSectionGrid({
  categoryKey,
}: {
  categoryKey: string;
}) {
  const { i18n } = useTranslation();
  const zh = i18n.language?.toLowerCase().startsWith("zh");
  const tr = useCallback((l: Lang) => (zh ? l.zh : l.en), [zh]);

  const { catalog, catalogEditable } = useSettings();

  const category = SETTINGS_CATEGORIES.find((c) => c.key === categoryKey);

  const [hideAdminOnly, setHideAdminOnly] = useState(false);
  useEffect(() => {
    let cancelled = false;
    fetchAuthStatus().then((authStatus) => {
      if (cancelled || !authStatus) return;
      setHideAdminOnly(Boolean(authStatus.enabled) && !authStatus.is_admin);
    });
    return () => {
      cancelled = true;
    };
  }, []);

  const chipFor = useCallback(
    (leaf: SettingsLeaf): { ok: boolean; label: Lang } | null => {
      if (!leaf.service) return null;
      if (catalogEditable !== true) return null;
      const configured =
        leaf.service === "search"
          ? Boolean(getActiveProfile(catalog, leaf.service)?.provider)
          : Boolean(getActiveModel(catalog, leaf.service)?.model);
      return {
        ok: configured,
        label: configured
          ? { zh: "已配置", en: "Configured" }
          : { zh: "未配置", en: "Not set" },
      };
    },
    [catalog, catalogEditable],
  );

  if (!category?.children) return null;

  const leaves = category.children.filter(
    (leaf) => !(leaf.adminOnly && hideAdminOnly),
  );

  return (
    <div>
      <header className="mb-6">
        <h1 className="font-serif text-[22px] font-semibold tracking-tight text-[var(--foreground)]">
          {tr(category.label)}
        </h1>
        <p className="mt-1.5 text-[13px] leading-relaxed text-[var(--muted-foreground)]">
          {tr(category.blurb)}
        </p>
      </header>

      <div className="grid gap-3 sm:grid-cols-2">
        {leaves.map((leaf) => (
          <LeafCard key={leaf.key} leaf={leaf} chip={chipFor(leaf)} tr={tr} />
        ))}
      </div>
    </div>
  );
}

function LeafCard({
  leaf,
  chip,
  tr,
}: {
  leaf: SettingsLeaf;
  chip: { ok: boolean; label: Lang } | null;
  tr: (l: Lang) => string;
}) {
  const Icon = leaf.icon;
  return (
    <Link
      href={leaf.href}
      className="group relative flex flex-col rounded-xl border border-[var(--border)] bg-[var(--card)] p-4 transition-all duration-150 hover:-translate-y-0.5 hover:border-[var(--foreground)]/20 hover:shadow-[0_6px_20px_-12px_rgba(0,0,0,0.25)]"
    >
      <div className="flex items-start gap-3">
        <span
          aria-hidden
          className={`flex h-10 w-10 shrink-0 items-center justify-center rounded-lg ${leaf.tile}`}
        >
          <Icon size={18} strokeWidth={1.7} />
        </span>
        <div className="min-w-0 flex-1">
          <div className="flex items-center gap-2">
            <h3 className="truncate text-[14.5px] font-medium leading-tight tracking-tight text-[var(--foreground)]">
              {tr(leaf.label)}
            </h3>
            {chip && (
              <span
                className={`inline-flex shrink-0 items-center gap-1 rounded-full px-1.5 py-0.5 text-[10.5px] font-medium ${
                  chip.ok
                    ? "bg-emerald-500/10 text-emerald-600 dark:text-emerald-400"
                    : "bg-[var(--muted)]/60 text-[var(--muted-foreground)]"
                }`}
              >
                <span
                  className={`h-1.5 w-1.5 rounded-full ${
                    chip.ok
                      ? "bg-emerald-500"
                      : "bg-[var(--muted-foreground)]/50"
                  }`}
                />
                {tr(chip.label)}
              </span>
            )}
          </div>
        </div>
        <ArrowUpRight
          size={16}
          className="shrink-0 text-[var(--muted-foreground)]/40 transition-colors group-hover:text-[var(--foreground)]"
        />
      </div>
      <p className="mt-3 text-[12.5px] leading-relaxed text-[var(--muted-foreground)]">
        {tr(leaf.blurb)}
      </p>
    </Link>
  );
}
