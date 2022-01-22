from words import words
from Hang_visuals import lives_visual_dict
import random

def getvalidword(words):
    word=random.choice(words)

    while "-" in word or " " in word:
        word=random.choice(words)

    return word.upper()

def hangman():
    word=getvalidword(words)
    word_letters=set(word)
    used_letters=set()
    lives=6
    count=0
    while lives!=0:        
        print(f"You have {lives} left and you've used this words till now: {used_letters}")
        word_list=[letter if letter in used_letters else "-" for letter in word]
        print(f"Current word: {word_list}")

        letter=input("\nGuess a Letter: ").upper()
        used_letters.add(letter)

        if letter not in word_letters:
            lives -=1
            print(f"Your letter {letter}, is not in the word.\n{lives_visual_dict[lives]}\n")

        else:
            count+=1

        if count == len(word):
            print("YOU WIN!!!")
            break

    else:        
        print(f"YOU LOSE!!\nThe correct word was {word}")

if __name__=="__main__":
    hangman()