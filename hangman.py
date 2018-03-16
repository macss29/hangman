import random

def hangman(word):
    wrong = 0
    man = ["0","|","/","\\","/","\\"]
    hang = [" "]*6
    
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong <= len(man):
        stages = [" ",
              "______   ",
              "|    |  ",
              "|    {}  ".format(hang[0]),
              "|   {}{}{}  ".format(hang[2],hang[1],hang[3]),
              "|   {} {}  ".format(hang[4],hang[5]),
              "|        "
              ]
        if wrong == len(man):
                break
        print("\n")
        print("\n".join(stages))
        print("\n")
        print(" ".join(board))
        msg = "Guess a letter\n"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            hang[wrong] = man[wrong]
            wrong += 1
        if "_" not in board:
            print("You Win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages))
        print("You lose! It was {}.".format(word))

        
randwords = ["horse","job","computer","hope","forest","forever", "luck", "phone", "court", "class", "hero", "basket", "justice", "odor", "rose", "flower"]
w = random.randint(0,len(randwords)-1)
hangman(randwords[w])
