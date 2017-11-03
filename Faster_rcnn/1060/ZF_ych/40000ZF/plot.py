import matplotlib.pyplot as plt
import pylab as pl

if __name__ == '__main__':
    with open('2_fsrcnntrainloss.txt') as f:
	lines = f.readlines()
    X = []
    Y = []
    for li in lines:
	li = li[:-1]
	x = li.strip().split(' ')[0]
	y = li.strip().split(' ')[1]
	print x,y
	X.append(x)
	Y.append(y)

    pl.plot(X, Y, 'b')
    plt.ylim(0, 2)
    pl.show()



