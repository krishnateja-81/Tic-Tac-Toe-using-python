import random as r

def check(board):
    win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in range(8):
        if board[win[i][0]] != 0 and board[win[i][0]] == board[win[i][1]] and board[win[i][0]] == board[win[i][2]]:
            return board[win[i][0]]
    return 0

def algorithm(board, p):
    a = check(board)
    if a != 0:
        return a * p
    position = -1
    v = -2
    for i in range(9):
        if board[i] == 0:
            board[i] = p
            s = -algorithm(board, p * -1)
            board[i] = 0
            if s > v:
                v = s
                position = i
    if position == -1:
        return 0
    return v

def ai(board):
    position = -1
    v = -2
    for i in range(9):
        if board[i] == 0:
            board[i] = 1
            s = -algorithm(board, -1)
            board[i] = 0
            if s > v:
                v = s
                position = i
    board[position] = 1

def easy_ai(board):
    p = r.randint(1, 9)
    if board[p - 1] != 0:
        easy_ai(board)
    else:
        board[p - 1] = 1

def display(board):
    print("Current Board:")
    for i in range(9):
        if i > 0 and i % 3 == 0:
            print("\n")
        if board[i] == 0:
            print("_", end=" ")
        if board[i] == -1:
            print("X", end=" ")
        if board[i] == 1:
            print("O", end=" ")
    print("\n\n")

def user1(board):
    position = int(input("\nUser1 Turn"))
    if board[position - 1] != 0:
        print("Wrong Move")
        user1(board)
    else:
        board[position - 1] = -1

def user2(board):
    position = int(input("\nUser2 Turn"))
    if board[position - 1] != 0:
        print("Wrong Move")
        user2(board)
    else:
        board[position - 1] = 1

def game():
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    choice = int(input("Enter 1 for single and 2 for multiple "))
    if choice == 1:
        print("Computer: O Vs You: X")
        level = int(input("Enter 1 for Easy and 2 for Hard\n"))
        if level == 1:
            p = int(input("Enter 1 to play 1(st) or 2(nd)"))
            for i in range(9):
                if check(board) != 0:
                    break
                if (i + p) % 2 == 0:
                    easy_ai(board)
                else:
                    display(board)
                    user1(board)
        elif level == 2:
            p = int(input("Enter 1 to play 1(st) or 2(nd)"))
            for i in range(9):
                if check(board) != 0:
                    break
                if (i + p) % 2 == 0:
                    ai(board)
                else:
                    display(board)
                    user1(board)
        else:
            print("Enter the correct level")
    elif choice == 2:
        for i in range(9):
            if check(board) != 0:
                break
            if i % 2 == 0:
                display(board)
                user2(board)
            else:
                display(board)
                user1(board)
    else:
        print("Check the input!!!")

    x = check(board)
    if x == 0:
        display(board)
        print("Draw")
    elif x == -1:
        display(board)
        print("X wins")
    elif x == 1:
        display(board)
        print("O wins")

game()
