'''
如题
matplotlib 是受MATLAB的启发构建的。
MATLAB是数据绘图领域广泛使用的语言和工具。
MATLAB语言是面向过程的。
利用函数的调用，MATLAB中可以轻松的利用一行命令来绘制直线，然后再用一系列的函数调整结果。

matplotlib有一套完全仿照MATLAB的函数形式的绘图接口
在matplotlib.pyplot模块中。
这套函数接口方便MATLAB用户过度到matplotlib包。下面，我们调用该模块绘制一条直线。

plot
英 [plɒt]   美 [plɑ:t]
n.
地基，基址图;（戏剧、小说等的）情节;一块地;测算表
vt.
密谋;以图表画出，制图;把…分成小块;为（文学作品）设计情节
vi.
设计作品情节;标示于图表上;密谋，暗中策划
'''

from matplotlib.pyplot import *
plot([0, 1], [0, 1]) # plot a line from (0,0) to (1,1)
title('a strait line') # x axis name
xlabel('x value')
ylabel('y value')
savefig("demo.pdf") # save picture
show()






