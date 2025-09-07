Language Detector (CLI)

This is a simple command-line tool to detect the language of a given text using the langdetect
 library.

Features

Detects the main language of an input text.

Shows the probabilities of multiple possible languages.

Provides a clear and simple CLI-based interaction.

Installation

Make sure you have Python 3 installed. Then install the required dependency:

pip install langdetect

Usage

Run the script from the terminal:

python language_tester.py


You will be prompted to enter some text. Example:

Language Detector (CLI)
Enter text: Bonjour, comment ça va?


Output:

Result:
  Main Language: fr
  Probabilities:
    fr:0.999996785175

Error Handling

If no text is entered, the program will notify you.

If detection fails, it will show an error message instead of crashing.

Example
Enter text: This is a simple language detection test.
Result:
  Main Language: en
  Probabilities:
    en:0.999996785175
