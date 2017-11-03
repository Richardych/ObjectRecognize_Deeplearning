# coding=utf-8
import matplotlib.pyplot as plt
import pylab as pl

if __name__ == '__main__':
    with open('1_fsrcnntrainloss.txt') as f1:
	lines1 = f1.readlines()
    X = []
    Y = []
    for li in lines1:
	li = li[:-1]
	x = li.strip().split(' ')[0]
	X.append(x)
    with open('1_fsrcnntrainclsloss.txt') as f2:
        lines2 = f2.readlines()
    temp = 0.8
    for li in lines2:
        li = li[:-1]
        y = li
        Y.append(y)
	temp = y

    print X,Y
    plt.xlabel("Iteration")
    plt.ylabel("loss")
    plt.title('ZF Net Classification loss')
    pl.plot(X, Y, 'b')
    plt.ylim(0, 1.5)
    plt.legend()
    pl.show()



