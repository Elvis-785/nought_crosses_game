from helpers import draw_board, check_turn, check_for_win
import os

spots={1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}

playing=True
comlete=False
turn=0
prev_turn=-1

while playing:
    #reset the screen.
    os.system("cls" if os.name=="nt" else "clear")
    draw_board(spots)
    #if an invalid turn occured, let the player know.
    if prev_turn==turn:
        print("Invalid spot selected, please pick another.")
    prev_turn=turn
    print("Player "+ str((turn%2)+1)+"'s turn: Pick your spot or press q to quit")
    #get input from the player.
    choice=input()
    if choice=="q":
        playing=False
    #check if the player gave a number from 1-9.
    elif str.isdigit(choice) and int(choice) in spots:
        #Check if the spot already been taken.
        if not spots[int(choice)] in {"x", "O"}:
            #Valid input, update the board
            turn += 1
            spots[int(choice)]=check_turn(turn)
            #Check if the game has ended (and someone has won)
            if check_for_win(spots):
                playing, complete=False, True
            if turn > 8:
                playing = False
#Out of loop, print the results
#Draw the board one last time.
os.system("cls" if os.name=="nt" else "clear")
draw_board(spots)
#if there was a winner say who won.
if complete:
    if choice == "X":
        print("Player 1 has won.")
    print("Player 2 has won.")
else:
    #Tie game.
    print("It is a draw.")

print("Thanks for playing!")
    