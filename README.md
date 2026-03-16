# language-translator

translator.py is a command-line Python tool that translates text using Google Translate via the deep-translator library. It supports auto language detection, flexible input for over 100 languages (by code or name), and interactive prompts with error handling.

Project Overview

translator.py is a simple, interactive command-line language translator built in Python. It uses Google Translate via the deep-translator library to convert user text between over 100 languages, with auto source detection and flexible language input.
​

How It's Made
Developed using Python 3 with the deep-translator library (install via pip install deep-translator). Key components include:

Imports GoogleTranslator and language constants (with fallback reversal for codes-to-names).

Functions: get_supported_languages_dict() for mappings, translate_text() for core translation with validation, display_available_languages() for user reference.

Main script handles CLI inputs, errors, and formatted output.
​

How to Use
Install dependency: pip install deep-translator.

Run: python translator.py.

Optionally view languages (yes/no).

Enter text, source language ('auto', 'en', or 'english'), and destination ('es' or 'spanish').

Get translated result or error message.
​

Example:

text
Enter the text: Hello world
Source: auto
Destination: spanish
Translated: Hola mundo

Limitations

Relies on Google Translate API (free but rate-limited; no offline mode).

Command-line only; no GUI or batch processing.

Source detection marked as 'Auto-Detected' (no actual detection shown; requires extra library for precision).

Error-prone for rare languages or complex text; no API key for heavy use.

Dependent on deep-translator library updates for language support.
