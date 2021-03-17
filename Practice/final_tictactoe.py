import sys

# Defining a function to check if any player won
def victory(matrix, player):

    # Row check
    for row in matrix:
        if row[0] == row[1] == row[2]:
            return player
            
    
    # Col check
    for col in range(3):
        if matrix[0][col] == matrix[1][col] == matrix[2][col]:
            return player
            
   
     # Diag check
    if matrix[0][0] == matrix[1][1] == matrix[2][2] or matrix[0][2] == matrix[1][1] == matrix[2][0]:
        return player


    if chance == 5:
        sys.exit("Draw")

    return 0


# 2-d list for the base structure
matrix= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

"""     
('  '.join(map(str,matrix[0])) joins the elements  
of matrix[0] but without the ' ' or [ ]

"""

print('  '.join(map(str,matrix[0])))
print('  '.join(map(str,matrix[1])))
print('  '.join(map(str,matrix[2])))

# Assigning that no one has won yet
winner = 0
# Initialising the player (Player 1 plays first)
player = 1
chance = 0 

while winner == 0:
    if player == 1:
        slot = input("Player 1: ")
        for list in matrix :        # Selects the 1-d list from the matrix
            for i in range(len(list)): # Selects the element from that 1-d list    
                if list[i] == int(slot):
                    list[i]='X'   # Converts the number into 'X'
                    chance += 1  
                    winner = victory(matrix, player)   # Passing through the defined function            
                    if winner :
                        sys.exit("Player 1 wins !!!")      # Comes out of the if loop. Player still remains 1
                    player = 2
            

    elif player == 2:
        slot = input("Player 2: ")
        for list in matrix :
            for i in range(len(list)):
                if list[i] == int(slot):
                    list[i]='O'
                    winner = victory(matrix, player) 
                    if winner :
                        sys.exit("Player 2 wins !!!")
                    player = 1
        

    # Printing the Updated Matrix
    print('  '.join(map(str,matrix[0])))
    print('  '.join(map(str,matrix[1])))
    print('  '.join(map(str,matrix[2])))

    
    
