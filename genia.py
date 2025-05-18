import os
#from google import genai
#from config import key
from colorama import init, Fore, Style

init(autoreset=True)

#client = genai.Client(api_key=key)

#def respond(prompt, temperature=0.3):
#    try:
#        contents = [types.Content(role="user",parts=[types.Part.from_text(text=prompt)])]
#        configparams = types.GenerateContentConfig(temperature=temperature)
#        response = client.models.generate_content(
#            model="gemini-2.0-flash", contents=contents,config=configparams
#        )
#        return response.text
#    except Exception as e:
#        return Fore.RED + Style.BRIGHT + "X Error: " + str(e)

def getessaydetails():
    print(Fore.CYAN + "= AI Writing Assistant =\n")

    topic = input(Fore.YELLOW + "? What is the topic of your essay?")
    type = input(Fore.YELLOW + "? What type of essay are you writing?")

    print(Fore.LIGHTYELLOW_EX + Style.DIM + "# Select the desired essay word count.")



getessaydetails()