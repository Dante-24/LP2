import sys
N = int(input())

def printsoln(board):
	for i in range(N):
		for j in range(N):
			print(board[i][j], end=" ")
		print()

def issafe(row, col, slc, bslc, rlook, slclook, bslclook):
	if slclook[slc[row][col]] or bslclook[bslc[row][col]] or rlook[row]:
		return False
	return True

def panda(board, col, slc, bslc, rlook, slclook, bslclook):
	if col >= N:
		return True

	for i in range(N):
		if issafe(i, col, slc, bslc, rlook, slclook, bslclook):
			board[i][col] = 1
			slclook[slc[i][col]] = True
			bslclook[bslc[i][col]] = True
			rlook[i] = True

			if panda(board, col + 1, slc, bslc, rlook, slclook, bslclook):
				return True

			board[i][col] = 0
			slclook[slc[i][col]] = False
			bslclook[bslc[i][col]] = False
			rlook[i] = False

	return False


board = [[0 for i in range(N)] for j in range(N)]
slc = [[0 for i in range(N)] for j in range(N)]
bslc = [[0 for i in range(N)] for j in range(N)]

rlook = [False] * N
slclook = [False] * (2 * N + 1)
bslclook = [False] * (2 * N + 1)

for i in range(N):
	for j in range(N):
		slc[i][j] = i + j
		bslc[i][j] = i - j + N - 1

if not panda(board, 0, slc, bslc, rlook, slclook, bslclook):
	print("No solution!")
else:
	printsoln(board)
