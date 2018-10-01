"""
You are given a m*n 2D grid initialized with three possibel val,
1. -1: an obstacle
2. 0: a gate
3. INF: an empty room, we use val 2^31 - 1 to represent INF, you may assume that the distance to a gate is less than INF
Fill each empty room with the distance to its nearest gate, if it is possible to reach a gate
"""

from collections import deque
def wallsAndGates(self, rooms):
	q =deque()
	s, INF, di, dj = 0, 2147483647, [-1, 0, 1, 0], [0, -1, 0, 1]
	for i in xrange(len(rooms)):
		for j in xrange(len(rooms[0])):
			if rooms[i][j] == 0:
				q.append((i,j))
				s += 1
	l = 0
	while q:
		i, j = q.popleft()
		s -= 1
		for d in xrange(4):
			ni, nj = i + di[d], j + dj[d]
			if 0 <= ni < len(rooms) and 0<= nj <len(rooms[0]) and rooms[ni][nj] == INF:
				rooms[ni][nj] = l+1
				q.append((ni, nj))
		if not s:
			l += 1
			s = len(q)
				
