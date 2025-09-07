# Language Detector (CLI)
# pip install langdetect

from langdetect import detect, detect_langs

def main():
    print("Language Detector (CLI)")
    text = input("Enter text: ")

    if not text.strip():
        print("No text entered.")
        return

    try:
        # detect single best
        lang = detect(text)
        # detect probabilities
        langs = detect_langs(text)

        print("\nResult:")
        print(f"  Main Language: {lang}")
        print("  Probabilities:")
        for l in langs:
            print("   ", l)
    except Exception as e:
        print("Could not detect language:", e)

if __name__ == "__main__":
    main()
