import random
print("WELCOME TO STONE PAPER SCISSOR GAME")

inp = input("press enter for instruction")
instruction = ("""
                's' is for Scissor
                 'p' is for paper
                 'r' is for rock
                
                 """)
print(instruction)
print("""
type 
        'start' to start game'
       'quit' to quit game""")
command = input()
if command == "quit":
    print("thanks for playing")
else:
    print("game has been started enter your move !!   Type 'quit' to end the game ")


    computer_moves = ["s",  "p", "r"]
    users_move = ""

    users_scores = 0
    computers_scores = 0
    while users_move!=quit:
        n=random.choice(computer_moves)
        users_move = input("Your Move-> ")
        q = f"{users_move},{n}"
        print(f"My Move-> {n}")
        print(q)
        if q == "r,s":
            print("you won")
            users_scores += 1
        elif q == "p,s":
                print("i won")
                computers_scores += 1
        elif q == "p,r":
            print("you won")
            users_scores += 1
        elif q == "r,p":
            print("i won")
            computers_scores +=  1
        elif q == "s,p":
            print("you won")

            users_scores += 1
        elif q == "s,r":
            print("i won")
            computers_scores += 1
        elif users_move=="quit":
            break
        elif users_move==n :
            print("draw")
        else:
            print("Invalid Move !!")

    print(f""" final score:
              your score: {users_scores} 
              my score: {computers_scores}
            
            Thanks for playing"""
          )
    input('Press ENTER to exit')










