from random import choice
words = ['PYTHON','PROGRAMMING','COPILOT','CLEAN','PREMIUM']

guessed_word = choice(words)

incorrect_guess = 0

print('=== Hangman Game ===')
print('I have chosen a word. Try to guess it!')
print('You have 6 chances.')

word = ''

for i in range(len(guessed_word)):
    word += '_ '

guessed_letters = ''

while incorrect_guess < 6:

        if '_' not in word:
                    print('Congratulations! You guessed the word: ',guessed_word) 
                    print('You win!')
                    break
        
        print('\nWord:',word)
        print('Guessed letters:',guessed_letters)
        print(f'Incorrect guesses: {incorrect_guess} / 6')
    
        
    
        letter = input('\nEnter a letter: ').capitalize()

        if not letter.isalpha() or len(letter) > 1:
                 print('Invalid input(only one alphabet is accepted.)')

        elif letter in guessed_letters:
             
             print('You have already guessed this letter.')

        
         
        elif letter in guessed_word:
            if letter not in guessed_letters:
                guessed_letters += letter+', '
            print('Good guess!')
            for i in range(len(guessed_word)):
                if guessed_word[i] == letter:
                    index = i
                    letters_list = word.split()
                    letters_list[index] = letter
                    word = ' '.join(letters_list)
    
    
        else:
            print('Incorrect guess!')
            guessed_letters += letter+', '
            incorrect_guess += 1
else:
    print('--- Game over ---')
    print('The word is',guessed_word)



    


        

    

