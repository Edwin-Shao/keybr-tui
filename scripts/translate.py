#!/usr/bin/env python3
"""Translate wordlist-en.txt using Google Translate (googletrans)."""
import json
import time

from googletrans import Translator

WORDLIST = "data/wordlist-en.txt"
OUTPUT = "data/translations.json"

def main():
    translator = Translator()

    with open(WORDLIST) as f:
        words = [line.strip() for line in f if line.strip()]

    print(f"Loaded {len(words)} words")

    try:
        with open(OUTPUT) as f:
            translations = json.load(f)
        print(f"Resuming from {len(translations)} existing translations")
    except FileNotFoundError:
        translations = {}

    for i, word in enumerate(words):
        if word in translations:
            continue
        try:
            result = translator.translate(word, src="en", dest="zh-cn")
            translations[word] = result.text
            print(f"[{i+1}/{len(words)}] {word} → {result.text}")
        except Exception as e:
            print(f"[{i+1}/{len(words)}] {word} → ERROR: {e}")
            translations[word] = ""

        if (i + 1) % 100 == 0:
            with open(OUTPUT, "w", encoding="utf-8") as f:
                json.dump(translations, f, ensure_ascii=False, indent=2)
            print(f"  --- saved {len(translations)} translations ---")

        time.sleep(0.3)

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(translations, f, ensure_ascii=False, indent=2)
    print(f"Done! {len(translations)} translations saved to {OUTPUT}")

if __name__ == "__main__":
    main()
