import random
import ascii_art


class HangMan():
    def __init__(self):
        self.get_words()
        self.rand_word = random.choice(self.word_list)
        self.word_sketch = ["_" for i in range(0, len(self.rand_word))]
        self.chances = 7
        self.guesses = []
        self.hang = -1
        self.hangman = [" " for x in range(8)]
        self.draw = ["O", "|", "|", "/", "\\", "/", "\\"]
        self.won = False
        self.lost = False

    def get_words(self):
        try:
            with open("word_list.txt", "r") as f:
                self.word_list = f.read().splitlines()
        except FileNotFoundError:
            import requests
            word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
            response = requests.get(word_site)
            word_list = response.content.splitlines()
            self.word_list = [x.decode().lower() for x in word_list]
        else:
            print("No words to play, sorry")

    def display(self):
        if self.hang >= 0:
            self.hangman[self.hang] = self.draw[self.hang]
        if self.chances <= 0:
            self.message = f"""GAME OVER!!!
                        The word was {self.rand_word}
                            """
            self.lost = True
        else:
            self.message = f"""word: {self.word_sketch},
                        guessed letters: {self.guesses},
                        """
        print("\033[H\033[J", end="")
        print(ascii_art.logo)
        print(
            f"""
                        You have a total of {self.chances} mistakes before the hanging                        
                         _ _ _ _ _
                        |         l
                        |         l
                        |         {self.hangman[0]}
                        |        {self.hangman[3]}{self.hangman[1]}{self.hangman[4]}
                        |         {self.hangman[2]}
                        |        {self.hangman[5]} {self.hangman[6]}
                        |        
                        |

                        {self.message}
                    """
        )

    def get_guess_compute(self):
        if "_" not in set(self.word_sketch):
            print("YOU WIN! No hanging today, \O/")
            self.won = True
        elif self.chances <= 0:
            self.lost = True
        else:
            input_char = input("\t\t\tGuess a letter: ").lower()
            while len(input_char) != 1 or input_char.isdigit():
                input_char = input(
                    "\t\t\tPlease type ONLY 1 LETTER AND also not a number.\n\t\t\tGuess a letter: ").lower()
            char_set = set(self.rand_word)
            if input_char in char_set:
                for i in range(0, len(self.rand_word)):
                    if input_char == self.rand_word[i]:
                        self.word_sketch[i] = input_char
            else:
                self.guesses.append(input_char)
                self.hang += 1
                self.chances -= 1


def main():
    game_on = HangMan()
    while game_on.won != True and game_on.lost != True:
        game_on.display()
        game_on.get_guess_compute()


if __name__ == '__main__':
    main()