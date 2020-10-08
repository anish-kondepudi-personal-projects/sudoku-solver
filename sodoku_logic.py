from sodoku_functions import is_valid, empty_values, print_board

# Sodoku Board || 0 = Empty 
board = [[8,0,0,0,0,0,0,0,0],
		[0,0,3,6,0,0,0,0,0],
		[0,7,0,0,9,0,2,0,0],
		[0,5,0,0,0,7,0,0,0],
		[0,0,0,0,4,5,7,0,0],
		[0,0,0,1,0,0,0,3,0],
		[0,0,1,0,0,0,0,6,8],
		[0,0,8,5,0,0,0,1,0],
		[0,9,0,0,0,0,4,0,0]]

# This is temporary. Once UI is constructed, the create_board()
# function from sodoku_function will be used to create a board
# and the existing values will be entered via the UI...

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

solve_board(board)

print_board(board)