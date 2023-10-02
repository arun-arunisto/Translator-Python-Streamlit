from googletrans import Translator

def translate_to_english():
    print("Welcome to the Translator to English App!")
    while True:
        print("\nEnter 'exit' to quit the app.")
        source_text = input("Enter the text to translate: ")

        if source_text.lower() == 'exit':
            print("Thank you for using the Translator to English App. Goodbye!")
            break

        try:
            translator = Translator()
            translation = translator.translate(source_text, dest='en')  # 'en' is the language code for English
            print(f"Translated text to English: {translation.text}")
        except Exception as e:
            print(f"Translation failed. Error: {e}")

if __name__ == "__main__":
    translate_to_english()

"""from googletrans import Translator, LANGUAGES

translator = Translator()
print(LANGUAGES)"""
