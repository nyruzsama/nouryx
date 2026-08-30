import re

path = r"C:\Users\Jalica Macalabo\.gemini\antigravity\brain\312cb222-e586-453a-ac33-0afcc3b968b1\.system_generated\steps\72\content.md"
with open(path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Search for occurrences of keywords like Bucket, Tonkatsu, Tebasaki, etc.
keywords = ["Bucket", "Tonkatsu", "Katsudon", "Tebasaki", "Cajun", "Shrimp", "Crab", "Garlic Butter", "Platter", "Solo"]

for kw in keywords:
    for match in re.finditer(re.escape(kw), text, re.IGNORECASE):
        start = max(0, match.start() - 150)
        end = min(len(text), match.end() + 250)
        snippet = text[start:end]
        # Clean HTML tags if any
        snippet_clean = re.sub(r'<[^>]+>', ' ', snippet)
        snippet_clean = re.sub(r'\s+', ' ', snippet_clean)
        print(f"[{kw} Context]: {snippet_clean}\n")
