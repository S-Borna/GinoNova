"use client";
import { useEffect } from "react";
export function Shield() {
  useEffect(() => {
    const block = (e: Event) => { e.preventDefault(); return false; };
    document.addEventListener("contextmenu", block, true);
    document.addEventListener("selectstart", block, true);
    document.addEventListener("copy", block, true);
    const handleKey = (e: KeyboardEvent) => {
      const k = e.key.toLowerCase();
      const c = e.ctrlKey || e.metaKey;
      const s = e.shiftKey;
      if (k === "f12" || (c && s && ["i","j","c"].includes(k)) || (c && ["u","s"].includes(k))) e.preventDefault();
    };
    document.addEventListener("keydown", handleKey, true);
    const style = document.createElement("style");
    style.textContent = "*{-webkit-user-select:none!important;user-select:none!important;}";
    document.head.appendChild(style);
  }, []);
  return null;
}
