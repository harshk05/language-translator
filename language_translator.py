# Python Language Translator
# This script uses the deep-translator library to translate text.
# Before running, make sure you have the library installed:
# pip install deep-translator

from deep_translator import GoogleTranslator
from deep_translator.exceptions import LanguageNotSupportedException
from deep_translator.constants import GOOGLE_LANGUAGES_TO_CODES

# Attempt to import GOOGLE_CODES_TO_LANGUAGES, or create it if not available.
# This handles cases where some versions of deep-translator might not directly export it.
try:
    from deep_translator.constants import GOOGLE_CODES_TO_LANGUAGES
except ImportError:
    # If GOOGLE_CODES_TO_LANGUAGES cannot be imported, create it by reversing GOOGLE_LANGUAGES_TO_CODES
    print("Note: GOOGLE_CODES_TO_LANGUAGES not directly found in constants, generating it manually.") # Optional: for user info
    GOOGLE_CODES_TO_LANGUAGES = {code: name for name, code in GOOGLE_LANGUAGES_TO_CODES.items()}

def get_supported_languages_dict():
    """Returns a dictionary of supported languages (name: code) by Google Translate via deep-translator."""
    # GOOGLE_LANGUAGES_TO_CODES is {'afrikaans': 'af', ...}
    return GOOGLE_LANGUAGES_TO_CODES

def translate_text(text, dest_lang, src_lang='auto'):
    """
    Translates text from a source language to a destination language
    using deep-translator.

    Args:
        text (str): The text to be translated.
        dest_lang (str): The destination language (code e.g., 'es' or full name e.g., 'spanish').
        src_lang (str, optional): The source language (code, full name, or 'auto').
                                  Defaults to 'auto'.

    Returns:
        str: The translated text, or an error message if translation fails.
    """
    supported_langs_map_name_to_code = get_supported_languages_dict() # name_to_code map
    supported_codes = list(supported_langs_map_name_to_code.values()) # ['af', 'sq', ...]
    supported_names = list(supported_langs_map_name_to_code.keys())   # ['afrikaans', 'albanian', ...]

    try:
        # Determine destination language code
        dest_code = dest_lang.lower()
        if dest_code in supported_names: # User entered 'spanish'
            dest_code = supported_langs_map_name_to_code[dest_code]
        elif dest_code not in supported_codes: # User entered invalid code or name
            return (f"Error: Invalid destination language '{dest_lang}'. "
                    f"Please use a valid language code or name.")

        # Determine source language code
        src_code = src_lang.lower()
        if src_code != 'auto':
            if src_code in supported_names: # User entered 'english'
                src_code = supported_langs_map_name_to_code[src_code]
            elif src_code not in supported_codes:
                 return (f"Error: Invalid source language '{src_lang}'. "
                         f"Please use a valid language code, name, or 'auto'.")

        # Initialize the translator
        translator = GoogleTranslator(source=src_code, target=dest_code)
        
        # Perform the translation
        translated_text = translator.translate(text)
        
        return translated_text
    except LanguageNotSupportedException as e:
        return f"Language Error: {e}"
    except Exception as e:
        return f"An error occurred during translation: {e}"

def display_available_languages():
    """Displays a list of available languages and their codes."""
    print("\nAvailable languages (Name: Code):")
    langs_map_name_to_code = get_supported_languages_dict() 
    
    count = 0
    # Sort by language name for better readability
    for name, code in sorted(langs_map_name_to_code.items()):
        print(f"{name.title()}: {code}")
        count += 1
        if count >= 25: # Display first 25 languages
            print("... and many more. You can use common language names or their codes.")
            break
    print("-" * 30)

if __name__ == "__main__":
    print("--- Simple Language Translator (using deep-translator) ---")

    # Option to display languages
    show_langs = input("Do you want to see a list of available languages? (yes/no): ").strip().lower()
    if show_langs == 'yes':
        display_available_languages()

    # Get input from the user
    text_to_translate = input("Enter the text you want to translate: ")
    if not text_to_translate.strip():
        print("Error: Text to translate cannot be empty.")
        exit()

    # Get source language
    source_language_input = input("Enter the source language (e.g., 'en', 'english', or 'auto' for detection): ").strip().lower()
    if not source_language_input: # Default to auto if empty
        source_language_input = 'auto'

    # Get destination language
    destination_language_input = input("Enter the destination language (e.g., 'es' or 'spanish'): ").strip().lower()
    while not destination_language_input:
        print("Destination language cannot be empty.")
        destination_language_input = input("Enter the destination language (e.g., 'es' or 'spanish'): ").strip().lower()

    # Perform the translation
    translated_text = translate_text(text_to_translate, destination_language_input, source_language_input)

    # Display the result
    print("\n--- Translation Result ---")
    if not translated_text.startswith("Error:") and not translated_text.startswith("Language Error:"):
        detected_source_lang_display = source_language_input.title()
        
        if source_language_input == 'auto':
            # For simplicity, we'll just state 'Auto-Detected'.
            # If you need to show the actual detected language, you might need a separate detection call,
            # for example, using: from deep_translator.detection import single_detection
            # detected_lang_code = single_detection(text_to_translate) # May require API key for some services or have limits
            # detected_source_lang_display = f"Auto-Detected ({GOOGLE_CODES_TO_LANGUAGES.get(detected_lang_code, detected_lang_code).title()})"
            detected_source_lang_display = "Auto-Detected"


        # Get full name for destination language for display
        dest_display_name = destination_language_input.title() # Default to user input
        
        # GOOGLE_CODES_TO_LANGUAGES should now be defined one way or another
        if GOOGLE_CODES_TO_LANGUAGES: # Check if it's populated
            if destination_language_input in GOOGLE_CODES_TO_LANGUAGES: # if it's a code like 'es'
                dest_display_name = GOOGLE_CODES_TO_LANGUAGES.get(destination_language_input, destination_language_input).title()
            # If user entered full name like 'spanish', it's already title-cased by .title() above.
            # We could also check against GOOGLE_LANGUAGES_TO_CODES keys if needed for consistency.
            elif destination_language_input in GOOGLE_LANGUAGES_TO_CODES: # if it's a name like 'spanish'
                 dest_display_name = destination_language_input.title()


        print(f"Original text ({detected_source_lang_display}): {text_to_translate}")
        print(f"Translated text ({dest_display_name}): {translated_text}")
    else:
        print(translated_text) # Print the error message

    print("--------------------------")
