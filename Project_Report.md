# translator.py Project Report

This report details the translator.py project, a lightweight Python-based command-line tool for translating text across multiple languages using Google Translate. Designed for simplicity and ease of use, it leverages the deep-translator library to provide reliable translations with user-friendly features like language previews and error handling.

## Project Description

translator.py enables users to translate any input text from a source language (auto-detected or specified) to a destination language. It supports over 100 languages recognized by Google Translate, accepting both ISO codes (e.g., 'es') and full names (e.g., 'Spanish'). The tool is interactive, prompting for inputs and displaying formatted results, making it ideal for quick translations without needing a web browser.

Key goals:
- Accessibility for non-technical users via natural language inputs.
- Robust validation to prevent common errors.
- Minimal dependencies for easy setup.

## Technical Architecture

### Dependencies

- `deep-translator`: Handles Google Translate integration, including GoogleTranslator class and constants like `GOOGLE_LANGUAGES_TO_CODES`.
- Standard Python libraries: No external APIs or heavy frameworks required.

### Core Components

The script (~200 lines) is structured modularly:

1. **Language Mapping**:
   - `get_supported_languages_dict()`: Returns `{name: code}` dict from `GOOGLE_LANGUAGES_TO_CODES`.

2. **Translation Logic** (`translate_text(text, dest_lang, src_lang='auto')`):
   - Validates dest/src languages against supported lists.
   - Maps names to codes (e.g., 'spanish' → 'es').
   - Initializes `GoogleTranslator(source=src_code, target=dest_code)`.
   - Catches `LanguageNotSupportedException` and general errors, returning user-friendly messages.

3. **UI Helpers**:
   - `display_available_languages()`: Prints sorted list of first 25 languages (name: code) for reference.

4. **Main Execution Block**:
   - CLI prompts with input validation (e.g., loops for empty dest_lang).
   - Results display: Original (with source label), translated text, or errors.

The code includes fallbacks, like reversing `GOOGLE_LANGUAGES_TO_CODES` to create `GOOGLE_CODES_TO_LANGUAGES` if unavailable in some library versions.

## Installation and Usage

### Setup

```bash
pip install deep-translator
git clone [repo]  # If hosted
cd translator
python translator.py
```

### Step-by-Step Usage

1. Launch: Prints welcome and offers language list.
2. Input text (required, non-empty).
3. Source language: 'auto' (default), 'en', 'english', etc.
4. Destination: 'es', 'spanish', etc. (validated in loop).
5. Output example:

```
Original text (Auto-Detected): Hello, how are you?
Translated text (Spanish): Hola, ¿cómo estás?
```

Supports edge cases: Invalid languages return "Error: Invalid destination language 'xyz'. Please use a valid language code or name."

## Features

- **Flexible Inputs**: Codes or names; auto source.
- **Preview Mode**: Optional language list (sorted, truncated).
- **Error Resilience**: Specific handling for unsupported languages/exceptions.
- **Clean Output**: Labels languages properly (e.g., title-cased names).

## Limitations and Improvements

| Aspect | Limitation | Potential Fix |
|--------|------------|---------------|
| Detection | Labels as 'Auto-Detected' without showing actual lang. | Integrate `single_detection` from deep-translator (may need API). |
| Throughput | Free Google Translate limits (e.g., rate limits). | Add paid API key support or local models like argos-translate. |
| Interface | CLI-only. | Add Streamlit/Flask GUI or batch file processing. |
| Offline | Requires internet. | Switch to offline libraries (e.g., MarianMT via transformers). |
| Advanced | No batch, history, or UI themes. | Add argparse for CLI flags, logging. |

## Future Enhancements

- GUI via Tkinter or web app.
- Batch translation from files.
- Voice input/output integration.
- Custom language models for privacy.

## Conclusion

This project demonstrates clean Python practices: modularity, error handling, and external library integration—suitable for portfolios or quick tools. It serves as a foundation for more advanced translation features and can be extended with GUI, batch processing, or offline capabilities based on user needs.
