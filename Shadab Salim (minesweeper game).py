                                                                 #Code for making MINESWEEPER game.
#-------------------------------------------------------------------CODE STARTS FROM HERE---------------------------------------------------------------------
import random
board=[[0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0]]
 
    
boarddisplay=[[-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1]]
 
 
    
#code for giving input for mines.
nummines=int(input("How many mines do you want in your game---->"))
if nummines>25:
    print("Impossible.(because max input is 24) setting to 5 default.")
    nummines=5
num=0
while num<nummines:
    row=random.randint(0,4)
    col=random.randint(0,4)
    if board [row][col]==0:
        board[row][col]=1
        num=num+1



#code for displaying board.        
def displayboard():
    print("_"*21)
    for row in range(0,5):
        print(" | ",end="")
        for col in range(0,5):
            if boarddisplay[row][col]==-1:
                print(" ",end=" | ")
            else:
                print(boarddisplay[row][col],end="| ")
                
        print(" ")
        print("_"*21)
displayboard()


#code for displaying board with mines.   
def displaysol():
    for row in range(0,5):
       for col in range(0,5):
            print(board[row][col],end=" ")
       print(" ")

#code for checking mines.       
def checkminesarround(row,col):
    s=0
    m=row-1
    while m<=row+1:
        if m>=0 and m<5:
            n=col-1
            while n<=col+1:
                if n>=0 and n<5:
                    s=s+board [m][n]
                n=n+1
        m=m+1
    return s 

#code for checking whether the input contains mine or not.
guess=0
while guess < (25-nummines):
    row=int(input("guess a row no. between(1,5):"))-1
    col=int(input("guess a col no. between(1,5):"))-1
    if board[row][col]==1:
        print("Booooooooom!!! you hit a mine and you lost the game.")
        displaysol()
    else:
        boarddisplay[row][col]=checkminesarround(row,col)
        displayboard()
        
        
#----------------------------------------------------------------------------THE END--------------------------------------------------------------------------