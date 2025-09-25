# Language Translator GUI using Python

This project is a simple **Language Translator** built using **Python**, **Tkinter**, and **googletrans** library. It provides a user-friendly GUI where users can enter text, select a target language, and get the translated output instantly.

---

## Features

- Translate text from one language to another using **Google Translate API** (via `googletrans` library).
- User-friendly GUI built with **Tkinter**.
- Dropdown menu with full language names.
- Displays translated text in a read-only output area.
- Supports multiple languages like Spanish, French, German, Chinese, Arabic, Hindi, and more.

---

## Libraries Used

### 1. googletrans
- A Python library that interfaces with Google Translate API.
- Handles translation easily by providing language codes and translation functions.
- Key Class:
  - `Translator`: Used to create a translation object and perform translations using `.translate()` method.
- Example:
  ```python
  from googletrans import Translator
  translator = Translator()
  translated_text = translator.translate("Hello", dest="fr")
  print(translated_text.text)  # Output: Bonjour

  
