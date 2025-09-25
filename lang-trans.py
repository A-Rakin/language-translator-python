from googletrans import Translator  # Import Translator class from googletrans library
import tkinter as tk                # Import Tkinter for GUI

# Initialize Translator
translator = Translator()  # Create a Translator object to use for translations

# Function to perform translation
def translate():
    # Get the text from the input text area and remove extra whitespace
    text = input_text.get("1.0", tk.END).strip()
    
    # Get the selected language name from the dropdown
    target_name = target_lang_var.get()
    
    # Look up the corresponding language code for the selected language
    target_lang = languages[target_name]
    
    # If there is some text, perform translation
    if text:
        translated_text = translator.translate(text, dest=target_lang)
        
        # Enable the output text area so we can write to it
        output_text.config(state="normal")
        
        # Clear any previous text in the output area
        output_text.delete("1.0", tk.END)
        
        # Insert the translated text into the output area
        output_text.insert(tk.END, translated_text.text)
        
        # Disable the output area to prevent manual editing
        output_text.config(state="disabled")

#Create GUI Window
root = tk.Tk()  # Initialize main window
root.title("Language Translator")  # Set window title
root.geometry("400x400")          # Set window size (width x height)

#Input Text Area
input_text = tk.Text(root, height=5, width=40)  # Create a text box for user input
input_text.pack(pady=10)                        # Add padding vertically

#Language Dictionary
# Dictionary mapping full language names (displayed in dropdown) to Google Translate codes
languages = {
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh",
    "Arabic": "ar",
    "Russian": "ru",
    "Bengali": "bn",
    "Hindi": "hi",
    "Japanese": "ja",
    "Korean": "ko",
    "Italian": "it",
    "Portuguese": "pt",
    "Turkish": "tr",
    "Urdu": "ur",
    "Dutch": "nl",
    "Hebrew": "he",
    "Greek": "el",
    "Czech": "cs",
    "Romanian": "ro",
    "Hungarian": "hu",
    "Vietnamese": "vi",
    "Thai": "th",
    "Indonesian": "id",
    "Malay": "ms",
    "Tamil": "ta",
    "Telugu": "te",
    "Gujarati": "gu",
    "Ukrainian": "uk",
}

#Target Language Dropdown
target_lang_var = tk.StringVar(root)      # Create Tkinter variable to hold selected language
target_lang_var.set("Spanish")            # Set default language selection

# Create a dropdown menu showing full language names
lang_dropdown = tk.OptionMenu(root, target_lang_var, *languages.keys())
lang_dropdown.pack()                       # Pack it into the GUI

#Translate Button
translate_button = tk.Button(root, text="Translate", command=translate)  # Button to trigger translation
translate_button.pack(pady=5)  # Add vertical padding

#Output Text Area 
output_text = tk.Text(root, height=5, width=40, state="disabled")  # Output area (disabled to prevent editing)
output_text.pack(pady=10)  # Pack it with vertical padding

#Start the GUI loop
root.mainloop()  # Start Tkinter event loop


#Run with this command in terminal : py -3.11 lang-trans.py
#Install python 3.11