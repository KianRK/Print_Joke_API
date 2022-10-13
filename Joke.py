import urllib.request as ulib
import json

#Creating dictionaries for required language and joke types in url

language_dict = {1: '', 2: 'lang=fr', 3: 'lang=de'}
type_dict = {1: '', 2: 'type=twopart', 3: 'type=single'}

#Standard-url if language is english and no certain joke type is required

url = 'https://v2.jokeapi.dev/joke/Any'

#Letting user choose language and joke type per console input where input is the key in respective dictionary

joke_language = int(input("Select your language: (1) English (2) French (3) German\n"))
joke_type = int(input("What time of joke you want to hear?: (1) surprise (2) two liner (3) one liner\n"))
print("\n")

#If only one setting deviates from the standard, the url needs to have an extra option added with the '?'
#this is achieved by assigning the standard settings to one, so they can be interpreted as a boolean "True".
#Not the cleanest way in terms of programming etiquette, but the most direct I could think of.

if joke_language ^ joke_type:
    url = 'https://v2.jokeapi.dev/joke/Any' + '?' + language_dict[joke_language] + type_dict[joke_type]

#If neither option is set to standard both extra options need to be added to the url

if joke_language != 1 and joke_type != 1:
    url = 'https://v2.jokeapi.dev/joke/Any' + '?' + language_dict[joke_language] + '&' + type_dict[joke_type]

#getting the url-data in textformat

url_txt = ulib.urlopen(url).read()

#loading the dictionary from url

joke_dict = json.loads(url_txt)

if joke_dict["type"] == "twopart":
    print(joke_dict["setup"])
    print("......")
    print(joke_dict["delivery"])

else:
    print(joke_dict["joke"])


