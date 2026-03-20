def analyze_content(text):
    words = text.split()
    return {
        "words": len(words),
        "characters": len(text),
        "paragraphs": text.count("\n") + 1,
        "reading_time": round(len(words) / 200, 2)
    }