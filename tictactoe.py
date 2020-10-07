#Sohini Mukhopadhyay
import random

def dispmat(board):
    print(f""" 
     {board[7]} | {board[8]} | {board[9]}                    7 | 8 | 9  
    ---+---+---                  ---+---+---
     {board[4]} | {board[5]} | {board[6]}     Positions-->   4 | 5 | 6 
    ---+---+---                  ---+---+--- 
     {board[1]} | {board[2]} | {board[3]}                    1 | 2 | 3 
    """)

def check(board, turn):
    if board[1]==board[2]==board[3]!=" " or board[4]==board[5]==board[6]!=" " or board[7]==board[8]==board[9]!=" " or \
        board[1]==board[4]==board[7]!=" " or board[2]==board[5]==board[8]!=" " or board[3]==board[6]==board[9]!=" " or \
        board[7]==board[5]==board[3]!=" " or board[1]==board[5]==board[9]!=" ":

         dispmat(board)
         print()
         print("************************************************************")
         print()
         print(f"{turn} Won!!")
         print()
         print("************************************************************")
         print()
         return 1
    return 0

def validip(board, turn):
    ip=" "
    while True:
        ip = input("Enter Position: ")
        try:                #to catch string input except space
            if ip==" ":
                print()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                print("Thanks for Playing, Let's not exit abruptly next time?")
                print()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                exit()
            elif 0<int(ip)<10:
                if board[int(ip)]!=" ":
                    print("Value already Allocated, Please choose different location")
                else:
                    board[int(ip)] = turn
                    break
            else:
                print("Please enter valid integer(1-9)")
        except:
            print("Please enter valid integer(1-9)")
    #return ip

def play(board, symbol):
    dispmat(board)
    sym1, sym2 = symbol[random.randint(0,1)]
    i=0
    flag=0
    for i in range(0,9):
        if i%2==0:
            print(f"\n{sym1}'s Turn: ")
            validip(board, sym1)
            if i>3:
                flag = check(board, sym1)
        else:
            print(f"\n{sym2}'s Turn: ")
            validip(board, sym2)
            if i>3:
                flag = check(board, sym2)
        #print(board)
        if flag==1:
            break
        else:
            dispmat(board)
    if flag==0:
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()
        print("Sorry, It's a  Draw")
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()

def main():
    board = ['loc control', ' ', ' ', ' ',' ',' ',' ',' ',' ',' ']
    symbol = [('O', 'X'), ('X', 'O')]
    play(board, symbol)

while True:
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print("Enter space to exit")
    print()
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print()
    print()
    print("\tWELCOME TO A GAME OF TIC-TAC-TOE")
    print()
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print()
    main()                      # calling main function
    print()
    ip = input("DO YOU WANT TO PLAY ANOTHER GAME? (Y/y)").upper()
    if ip!='Y':
        print()
        print("\tGOODBYE!")
        print()
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()
        break