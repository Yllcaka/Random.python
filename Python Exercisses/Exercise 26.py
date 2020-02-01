def CHECK(makarena):
	for x in range(3):
		row = set([makarena[x][0],makarena[x][1],makarena[x][2]])
		if len(row) == 1 and makarena[x][0] !=0:
			return makarena[x][0]


	for x in range(3):
		row = set([makarena[0][x],makarena[1][x],makarena[2][x]])
		if len(row) == 1 and makarena[x][0] !=0:
			return makarena[x][0]


	diag1 = set([makarena[0][0],makarena[1][1],makarena[2][2]])
	diag2 = set([makarena[2][0],makarena[1][1],makarena[0][2]])
	if len(diag1) or len(diag2) and makarena[1][1] != 0:
		return makarena[1][1]
	return 0
game = [[2,2,1],
	[1,1,2],
	[1,2,1]]
print(CHECK(game))