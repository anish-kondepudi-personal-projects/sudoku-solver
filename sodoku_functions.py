# This .py file is a list of function that will be used to build the recursive backtracking algorithm for the Sodoku Solver


# Creates Sodoku Board || 0 = Empty 
def create_board():
	board = [[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0]]
	return board


# Prints Board
def print_board(board):
	print("-------------------------")
	for r in range(3):
		print("| " + str(board[r][0]) + " " + str(board[r][1]) + " " + str(board[r][2]) + " | " + str(board[r][3]) + " " + str(board[r][4]) + " " + str(board[r][5]) + " | " + str(board[r][6]) + " " + str(board[r][7]) + " " + str(board[r][8]) + " | ")
	print("|-------|-------|-------|")
	for r in range(3,6):
		print("| " + str(board[r][0]) + " " + str(board[r][1]) + " " + str(board[r][2]) + " | " + str(board[r][3]) + " " + str(board[r][4]) + " " + str(board[r][5]) + " | " + str(board[r][6]) + " " + str(board[r][7]) + " " + str(board[r][8]) + " | ")
	print("|-------|-------|-------|")
	for r in range(6,9):
		print("| " + str(board[r][0]) + " " + str(board[r][1]) + " " + str(board[r][2]) + " | " + str(board[r][3]) + " " + str(board[r][4]) + " " + str(board[r][5]) + " | " + str(board[r][6]) + " " + str(board[r][7]) + " " + str(board[r][8]) + " | ")
	print("-------------------------")


# Dictionary to Convert Between Quadrant and Row/Column
quad_to_rc = {
			1:[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]],
			2:[[0,3],[0,4],[0,5],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5]],
			3:[[0,6],[0,7],[0,8],[1,6],[1,7],[1,8],[2,6],[2,7],[2,8]],
			4:[[3,0],[3,1],[3,2],[4,0],[4,1],[4,2],[5,0],[5,1],[5,2]],
			5:[[3,3],[3,4],[3,5],[4,3],[4,4],[4,5],[5,3],[5,4],[5,5]],
			6:[[3,6],[3,7],[3,8],[4,6],[4,7],[4,8],[5,6],[5,7],[5,8]],
			7:[[6,0],[6,1],[6,2],[7,0],[7,1],[7,2],[8,0],[8,1],[8,2]],
			8:[[6,3],[6,4],[6,5],[7,3],[7,4],[7,5],[8,3],[8,4],[8,5]],
			9:[[6,6],[6,7],[6,8],[7,6],[7,7],[7,8],[8,6],[8,7],[8,8]]
			}
"""
 Outline for How Quadrants are Structured
 [1,2,3]
 [4,5,6]
 [7,8,9]
"""


def get_quad(row, column):
	if row <= 2:
		# Quad 1,4,7
		if column <= 2:
			# Quad 1
			return 1
		elif column <= 5:
			# Quad 2
			return 2
		else:
			# Quad 3
			return 3
	elif row <=5:
		# Quad 2,5,8
		if column <= 2:
			# Quad 4
			return 4
		elif column <= 5:
			# Quad 5
			return 5
		else:
			# Quad 6
			return 6
	else:
		# Quad 3,6,9
		if column <= 2:
			# Quad 7
			return 7
		elif column <= 5:
			# Quad 8
			return 8
		else:
			# Quad 9
			return 9
	# Double Else (Nested Elses) Return Quadrant 9 - This May Lead to Errors
	# Keep in Mind for Future Reference


# Given Board, Row, and Column as Input -> Determines if value satisfies Sodoku Rules
def is_valid(board, row, column):
	if row_valid(board, row, column) and column_valid(board, row, column) and quad_valid(board, row, column):
		return True
	return False


# Given board, row, and column as input -> Determines if value satisfies Sodoku Rules for a Valid Row
def row_valid(board, row, column):
	val = board[row][column]
	if val == 0:
		# Unsure of what type of Error to Raise
		# Using Print Statement and Returning Error for now
		# Will likely remove this portion of code later
		print("Error - Value of Position is 0")
		return "ERROR"
	board[row][column] = 0
	li = []
	for col in board[row]:
		li.append(col)
	if val in li:
		board[row][column] = val
		return False
	board[row][column] = val
	return True


# Given board, row, and column as input -> Determines if value satisfies Sodoku Rules for a Valid Column
def column_valid(board, row, column):
	val = board[row][column]
	if val == 0:
		# Unsure of what type of Error to Raise
		# Using Print Statement and Returning Error for now
		# Will likely remove this portion of code later
		print("Error - Value of Position is 0")
		return "ERROR"
	board[row][column] = 0
	li = []
	for r in board:
		li.append(r[column])
	if val in li:
		board[row][column] = val
		return False
	board[row][column] = val
	return True


# Given board, row, and column as input -> Determines if value satisfies Sodoku Rules for a Valid Quadrant
def quad_valid(board, row, column):
	v = board[row][column]
	if v == 0:
		# Unsure of what type of Error to Raise
		# Using Print Statement and Returning Error for now
		# Will likely remove this portion of code later
		print("Error - Value of Position is 0")
		return "ERROR"	
	board[row][column] = 0
	quad = get_quad(row, column)
	quad_indices = quad_to_rc[quad]
	li = []
	for indices in quad_indices:
		r = indices[0]
		c = indices[1]
		val = board[r][c]
		li.append(val)
	board[row][column] = v
	if v in li:
		return False
	return True


# Creates List of all Row/Column Coordinates for All Filled Positions on the Board
def fixed_values(board):
	li = []
	r = 0
	c = 0
	while r != 9:
		if board[r][c] != 0:
			li.append([r,c])
		if c == 8:
			r += 1
			c = 0
		else:
			c += 1
	return li


# Creates List of all Row/Column Coordinates for All Empty Positions on the Board
def empty_values(board):
	li = []
	r = 0
	c = 0
	while r != 9:
		if board[r][c] == 0:
			li.append([r,c])
		if c == 8:
			r += 1
			c = 0
		else:
			c += 1
	return li


# Backtracking algorithm which solves the Sodoku Puzzle
def solve_board(board):
	empty_values_list = empty_values(board)
	i = 0
	l = len(empty_values_list)
	while i < l:
		board[empty_values_list[i][0]][empty_values_list[i][1]] += 1
		if is_valid(board, empty_values_list[i][0], empty_values_list[i][1]) and board[empty_values_list[i][0]][empty_values_list[i][1]] <= 9:
			i += 1
		elif board[empty_values_list[i][0]][empty_values_list[i][1]] >= 9:
			board[empty_values_list[i][0]][empty_values_list[i][1]] = 0
			i -= 1
