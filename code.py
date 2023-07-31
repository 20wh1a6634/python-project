def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

n = int(input())

vertices = []
for i in range(n):
    x, y = map(int, input().split())
    vertices.append((x, y))

max_distance = 0

for i in range(n):
    for j in range(i + 1, n):
        dist = distance(vertices[i][0], vertices[i][1], vertices[j][0], vertices[j][1])
        if dist > max_distance:
            max_distance = dist

print("%0.8f" % max_distance)
input 1:
7
0 20
40 0
40 20
70 50
50 70
30 50
0 50
output 1:
76.15773106
>>> 
input 2:
3
0 2017
-2017 -2017
2017 0
output:2
4510.14911062
