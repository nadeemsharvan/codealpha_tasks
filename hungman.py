import random

words = ['apple', 'tiger', 'chair', 'river', 'pizza']
word = random.choice(words)
guessed = []
wrong = 0
max_wrong = 6

print('=== Hangman Game ===')

while wrong < max_wrong:
    display = ''
    for ch in word:
        if ch in guessed:
            display += ch + ' '
        else:
            display += '_ '
    print('\nWord:', display.strip())
    print('Wrong guesses left:', max_wrong - wrong)

    if all(ch in guessed for ch in word):
        print('🎉 You won! The word was', word)
        break

    guess = input('Enter a letter: ').lower()

    if len(guess) != 1 or not guess.isalpha():
        print('Enter only one letter.')
        continue

    if guess in guessed:
        print('Already guessed!')
        continue

    guessed.append(guess)

    if guess not in word:
        wrong += 1
        print('❌ Wrong guess!')
else:
    print('\n💀 Game Over! The word was', word)
