board = [
	[0,8,5,4,0,0,1,2,0],
	[6,0,0,0,7,5,0,0,9],
	[0,0,0,6,0,1,0,7,8],
	[0,0,7,0,4,0,0,6,0],
	[2,0,1,0,5,0,9,3,0],
	[0,0,4,0,6,0,0,0,5],
	[0,7,0,3,0,0,0,1,2],
	[1,2,0,0,0,7,4,0,0],
	[3,4,0,2,0,6,0,5,7]
]

def final_solution(bo):       #recursion

	find= find_empty_spaces(bo)
	if not find:
		return True			#found the solution
	else:	
		row, col = find

	for i in range(1,10):           #try each number from 1 to 9
		if validate(bo, i, (row,col)):
			bo[row][col] = i

			if final_solution(bo):
				return True

			bo[row][col] = 0     #invalid value so retry this position by resetting it to 0

	return False

def validate(bo, num, pos):
	
	#Check row
	for i in range(len(bo[0])):
		if bo[pos[0]][i]== num and  pos[1]!= i: # if the positon has that number and if the position is already inserted then ignore 
			return False

	#check column
	for i in range(len(bo)):
		if bo[i][pos[1]]== num and  pos[0]!= i: # Same as above but goes down every single row and ignore if already filled or has same number
			return False

	#Check which box we are in 
	box_a = pos[1] // 3           #gives 0,1,2  rows,columns of box(0,1,2)
	box_b = pos[0] // 3

	for i in range(box_b*3, box_b*3+3):
		for j in range(box_a*3, box_a*3+3):
			if bo[i][j] == num and (i,j)!=pos: 
				return False

	return True

def print_board(bo):	

	for i in range(len(bo)):
		if i % 3 ==0 and i != 0:	#after every 3 rows there will be  the below line
			print("- - - - - - - - - - - - -")

		for j in range(len(bo[0])):
			if j % 3 == 0 and j != 0 :  #after every 3 columns there will be  the below line
				print(" | ", end="")

			if j == 8:
				print(bo[i][j])		
			else:
				print(str(bo[i][j])+ " ", end="")

def find_empty_spaces(bo):

	for i in range(len(bo)):
		for j in range(len(bo[0])):
			if bo[i][j] == 0:
				return (i, j) #row & column
	return None    #no empty space

print("\nThe initial Board\n")
print_board(board)

final_solution(board)

print("\nThe Final Board using Back Tracking\n")
print_board(board)