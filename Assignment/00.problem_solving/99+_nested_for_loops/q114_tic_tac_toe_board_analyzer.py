while True:
    board = [["-","-","-"],["-","-","-"],["-","-","-"]]
    Board = [["7","8","9"],["4","5","6"],["1","2","3"]]
    count=0
    game_count=0
    while True:
        print("==========================================")
        count+=1
        for i in range(3):
            for j in range(3):print(board[i][j],end=" ")
            print("         ",end="")
            for j in range(3):print(Board[i][j],end=" ")
            print()
        print("==========================================")
        if board[0][0]==board[0][1]==board[0][2]=="O" or board[1][0]==board[1][1]==board[1][2]=="O" or board[2][0]==board[2][1]==board[2][2]=="O" or board[0][0]==board[1][0]==board[2][0]=="O" or board[0][1]==board[1][1]==board[2][1]=="O" or board[2][2]==board[0][2]==board[1][2]=="O" or board[2][2]==board[1][1]==board[0][0]=="O" or board[0][2]==board[1][1]==board[2][0]=="O":
            print("O wins")
            print("==========================================")
            game_count=count=0
            break
        if board[0][0]==board[0][1]==board[0][2]=="X" or board[1][0]==board[1][1]==board[1][2]=="X" or board[2][0]==board[2][1]==board[2][2]=="X" or board[0][0]==board[1][0]==board[2][0]=="X" or board[0][1]==board[1][1]==board[2][1]=="X" or board[2][2]==board[0][2]==board[1][2]=="X" or board[2][2]==board[1][1]==board[0][0]=="X" or board[0][2]==board[1][1]==board[2][0]=="X":
            print("X wins")
            print("==========================================")
            game_count=count=0
            break
        if count==10:
            print("Tie")
            print("==========================================")
            break
        if game_count%2==0:
            if count%2==0:ox="O"
            else:ox="X"
        elif game_count%2==0:
            if count%2==0:ox="X"
            else:ox="O"
        n=int(input("Enter number to fill the board: "))
        if n==1:board[2][0]=ox
        elif n==2:board[2][1]=ox
        elif n==3:board[2][2]=ox
        elif n==4:board[1][0]=ox
        elif n==5:board[1][1]=ox
        elif n==6:board[1][2]=ox
        elif n==7:board[0][0]=ox
        elif n==8:board[0][1]=ox
        elif n==9:board[0][2]=ox
        print("==========================================")
    game_count+=1
    ask=input("Q-to quit or anythin to play: ").strip()
    if ask.lower()=="q":
        break