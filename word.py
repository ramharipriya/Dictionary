import random
from random_words import RandomWords
from PyDictionary import PyDictionary

def newWord():
    d = PyDictionary()
    rw = RandomWords()

    word = rw.random_word()
    definitions = d.meaning(word)

    try:
        part_of_speech = random.choice( list ( definitions.keys() ) )
        definition = random.choice(definitions[part_of_speech])
    except:
        return "NULL_DEFINITION"
    return {
        "word": word,
        "definition": definition,
        "part_of_speech": part_of_speech
    }

word = newWord()

while(word == "NULL_DEFINITION"):
    word = newWord()

print(f'{word["word"]}: {word["definition"]} ({word["part_of_speech"]})')
