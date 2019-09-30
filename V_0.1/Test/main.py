a,b = input().split()
print(int(a)+int(b))




'''
from itertools import combinations
n = int(input())
des = []
for i i range(n):
    des.append(list(map(int, input().split())))
Min = abs(des[0][0] - des[1][0]) + abs(des[0][1] - des[1][1])
for i in combinations(list(range(n)), 2):
    temp = abs(des[i[0]][0] - des[i[1]][0]) + abs(des[i[0]][1] - des[i[1]][1])
    if temp < Min:
        Min = temp
print(Min)
'''





'''
题目描述
Marvolo经常在节假日出去旅行，领略异国他乡的别样景色。

每到一个地方，Marvolo会在第一时间买一份当地的地图，在上面挑选好要去的景点后，就开始规划此次的旅行路线。因为时间精力有限，Marvolo自然希望能够节省体力，参观尽可能多的景点。在制定路线过程中，衡量景点间的距离十分重要。在这里Marvolo采用的是曼哈顿距离。对于点(x1,y1),(x2,y2)来说, 这两点间曼哈顿距离的定义是|x1-x2|+|y1-y2|。例如(1,2)和(3,5)之间的曼哈顿距离便是5。在旅行过程中，从一个景点走到另一个景点的距离便是这两点间的曼哈顿距离。

现在，Marvolo在地图上标出了n个景点，并且在地图上建立了一个直角坐标系，第i个景点的坐标是(xi,yi)​，景点间的坐标互不相同。Marvolo在第一天只打算参观两个景点，他想知道选择哪两个不同的景点，可以使他在这一天中在景点之间走过的距离最少。

因为是出去旅行，Marvolo并没有带电脑，所以他找到了会编程的你，希望你编程帮他解决这个问题。

输入格式
第一行一个整数n，表示景点的个数

接下来共n行，每行两个整数xi, yi，由空格隔开，表示第i​个点的坐标

输出格式
一行一个整数，表示走过的距离的最小值。如果有多对景点满足题意，输出任意一对景点间的距离即可。对距离的定义如题面所示。
'''
