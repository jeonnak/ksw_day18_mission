class Graph():
	def __init__(self, size):
		self.SIZE = size
		self.graph = [[0 for x in range(size)] for x in range(size)]


# 그래프를 출력해준다.
def print_graph(g):
	print('	', end='')
	for v in range(g.SIZE):
		print("%9s" % store_array[v][0], end =' ')
	print()
	for row in range(g.SIZE):
		print("%9s" % store_array[row][0], end =' ')
		for col in range(g.SIZE):
			print("%8d" % g.graph[row][col], end = ' ')
		print()
	print()


G1 = None
store_array = [['GS25', 30], ['CU', 60], ['Seven11', 10], ['MiniStop', 90], ['Emart24', 40]]
GS25, CU, Seven11, MiniStop, Emart24 = 0, 1, 2, 3, 4

g_size = 5
G1 = Graph(g_size)

# 편의점 인접행렬
G1.graph[GS25][CU] = 1; G1.graph[GS25][Seven11] = 1
G1.graph[CU][GS25] = 1; G1.graph[CU][Seven11] = 1; G1.graph[CU][MiniStop] = 1
G1.graph[Seven11][GS25] = 1; G1.graph[Seven11][CU] = 1; G1.graph[Seven11][MiniStop] = 1
G1.graph[MiniStop][Seven11] = 1; G1.graph[MiniStop][CU] = 1; G1.graph[MiniStop][Emart24] = 1
G1.graph[Emart24][MiniStop] = 1

print('## 편의점 그래프 ##')
print_graph(G1)

stack = []
visited_array = []			# 방문한 편의점

current = 0			# 시작 편의점
max_store = current		# 최대 개수 편의점 번호(GS25)
max_count = store_array[current][1]	# 편의점의 허니버터 숫자
stack.append(current)
visited_array.append(current)

# 깊이 우선 탐색 방식
while (len(stack) != 0):
	next = None
	for vertex in range(g_size):
		if G1.graph[current][vertex] == 1:
			if vertex in visited_array:	# 방문한 적이 있는 편의점이면 탈락
				pass
			else:			# 방문한 적이 없는 편의점이면 다음 편의점으로 지정
				next = vertex
				break

	if next != None:				# 방문할 다음 편의점이 있는 경우
		current = next
		stack.append(current)
		visited_array.append(current)
		if store_array[current][1] > max_count:
			max_count = store_array[current][1]
			max_store = current
	else:					# 방문할 다음 편의점이 없는 경우
		current = stack.pop()

print('허니버터칩 최대 보유 편의점(개수) -->', store_array[max_store][0], '(', store_array[max_store][1], ')')