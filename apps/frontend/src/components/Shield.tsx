"use client";
import { useEffect } from "react";
export function Shield() {
  useEffect(() => {
    // Block right-click context menu
    document.addEventListener("contextmenu", (e) => { e.preventDefault(); }, true);
    // Block DevTools keyboard shortcuts
    const handleKey = (e: KeyboardEvent) => {
      const k = e.key.toLowerCase();
      const c = e.ctrlKey || e.metaKey;
      const s = e.shiftKey;
      const a = e.altKey;
      if (k === "f12") { e.preventDefault(); return; }
      if (c && s && (k === "i" || k === "j" || k === "c" || k === "k")) { e.preventDefault(); return; }
      if (c && k === "u") { e.preventDefault(); return; }
      if (c && a && (k === "i" || k === "j" || k === "u")) { e.preventDefault(); return; }
    };
    document.addEventListener("keydown", handleKey, true);
  }, []);
  return null;
}
