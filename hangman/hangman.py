import random
import hangman_words
import hangman_ascii

choice = "y"

while choice == 'y':
    chosen_word = random.choice(hangman_words.word_list)
    display = []

    for i in range(len(chosen_word)):
        display.append("_")
        print(display[i],end='')

    print()

    lives = 0
    flag = True
    stages = hangman_ascii.ascii_art()

    while flag:
        guess = input("Guess letter: ").lower()

        if guess in display:
            print('You already entered this letter')

        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess

        for _ in display:
            print(_,end='')
        print()

        if guess not in chosen_word:
            print(f"letter {guess} is not in the word")

            lives += 1
            if lives == 6:
                print(f"Your word was {(chosen_word.upper())}")
                print("You Lose.")
                flag = False

        if '_' not in display:
            print("You Win.")
            flag = False

        print(stages[lives])

        if flag == False:
            choice = input("Do you want to play again(y/n): ")