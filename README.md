# Translation-Py
This code translates a text file from one language to another using the DeepL API.

Dependencies
os
requests
json
tkinter
filedialog

How to use
1. Run the script.
2. Select the source language from the list of available languages.
3. Select the target language from the remaining available languages.
4. Select the input file.
5. Select the output file.
6. Wait for the translation process to finish.
7. Find the translated text in the output file.

Note
The code uses the DeepL API to perform the translation. Please ensure that you have an API key and that the requests module is installed before running the code.
The available languages are: English, Spanish, German, French, Italian, Dutch, Polish, Russian, Portuguese.

Using the code
1. Define your API key by replacing the "api_key" variable with your own API key.
2. Run the script and follow the prompts to select the source and target languages, input file, and output file.
3. Wait for the translation process to finish.
4. Find the translated text in the output file.

Code explanation
The code prompts the user to select the source and target languages, input file, and output file using tkinter's filedialog. It then sends a POST request to the DeepL API with the text to be translated, the source and target languages, and the API key. The API response is parsed using the json module, and the translated text is written to the output file.

additional steps i would take if i had more time or knowledge would be to add a dictionary
