#MODULE
import time
import getpass
#GALGJE START
print("----------------------")
print("GALGJE")
print("----------------------")
time.sleep(1)
print( )
word = getpass.getpass(prompt = "Speler 1, kies een woord (woord is niet zichtbaar tijdens het typen):").lower()
print( )

#VAR
guesses = ''
chances = 9
guess_right = []
#SHOW UNDERSCORE
for index in word:
    guess_right += "_"
show_word = ' '.join(guess_right)
print(show_word)
#WHILE FUNCTION
while chances > 0:
    guess = input("Speler 2, raad het woord: ").lower()
    print( )
    guesses += guess
    #GUESS NOT EQUAL
    if guess not in word:  
        chances -= 1
        #KANSEN OP
        if chances == 0:
            print("Alle kansen zijn op")
            print("SPELER 2 HEEFT VERLOREN")
            print("Het juiste woord was: " + word)
            break;
        else:
            print("Probeer het nog eens!")
            print("Je hebt nog", + chances, 'kansen over')
            print(" ")
    #GUESS EQUAL
    elif guess == word:
        print('SPELER 2 HEEFT GEWONNEN')
        print('Het juiste woord was ' + word)
        break;
    else:
        for index in range(len(word)):
            if word[index] == guess:
                guess_right[index] = guess
    guessed_words = ''.join(guess_right)
    #GUESSES RIGHT
    if(guessed_words == word):
        print('SPELER 2 HEEFT GEWONNEN')
        print('Het juiste woord was ' + word)
        break;
    #SHOW UNDERSCORES
    print(guessed_words)