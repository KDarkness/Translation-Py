import os
import requests
import json
from tkinter import Tk, Button, Label, filedialog

#Define a function to display language choices and get user's selection
def get_choice(choices, window_title):
    def set_choice(choice):
        nonlocal source_lang, target_lang
        if not source_lang:
            source_lang = choice
            window.title("Select Target Language")
        else:
            target_lang = choice
            window.destroy()
            
# Initialize the source and target language selections to None
    source_lang, target_lang = None, None
    
# Create a tkinter window to display the language choices
    window = Tk()
    window.title(window_title)
    window.geometry("500x200")
    
# Display the language choices in buttons and assign the set_choice function to each button's command    
    for i, chunk in enumerate(chunked(choices, 4)):
        for j, choice in enumerate(chunk):
            btn = Button(window, text=choice, command=lambda choice=choice: set_choice(choice))
            btn.grid(row=i, column=j, padx=10, pady=10)
            
# Run the tkinter event loop until the window is closed
    window.mainloop()
    return source_lang, target_lang

#Define a function to split an iterable into chunks of a given size
def chunked(iterable, size):
    return [iterable[i:i+size] for i in range(0, len(iterable), size)]

#Open a dialog to select the input file and store the file path
input_file = filedialog.askopenfilename(title="Select Input File")
if not input_file:
    print("No input file selected.")
    exit()
    
#Open a dialog to select the output file and store the file path
output_file = filedialog.asksaveasfilename(title="Save Output As", defaultextension=".txt")
if not output_file:
    print("No output file selected.")
    exit()
#If no output file is selected, print an error message and exit the program
endpoint = "https://api-free.deepl.com/v2/translate"
api_key = "b188505b-8a71-6c9a-3561-d0ae6c40c7fa:fx"

#Dictionary of supported languages and their corresponding language codes
languages = {
    "English": "en",
    "Spanish": "es",
    "German": "de",
    "French": "fr",
    "Italian": "it",
    "Dutch": "nl",
    "Polish": "pl",
    "Russian": "ru",
    "Portuguese": "pt",
}

#Display the language choices and get the user's selected source and target languages
source_lang, target_lang = get_choice(list(languages.keys()), "Select Source Language")
if not source_lang or not target_lang:
    print("No source or target language selected.")
    exit()

params = {
    "auth_key": api_key,
    "text": "",
    "source_lang": languages[source_lang],
    "target_lang": languages[target_lang],
}

with open(input_file, 'r') as f:
    text = f.read()

params["text"] = text

print(f"Translating from {source_lang} to {target_lang} using DeepL API...")
response = requests.post(endpoint, params=params)
print(response.status_code)
print(response.content)

response_data = json.loads(response.content)

if "message" in response_data:
    print("Translation error:", response_data["message"])
    exit()

if "translations" in response_data:
    translation = response_data["translations"][0]["text"]
else:
    print("No translation found.")
    translation = ""

with open(output_file, 'w') as f:
    f.write(translation)
    
# Display a message to indicate the translation
window = Tk()
window.title("Translation Complete")
message = Label(window, text="Translation Complete!")
message.pack(padx=20, pady=20)
window.mainloop()
