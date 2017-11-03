import re

if __name__ == '__main__':
    with open('2_fsrcnntrain.txt') as f:
        lines = f.readlines()
    for li in lines:
	li = li[:-1]
	li = re.findall(r'loss_cls = (\d+\.?\d*)', li)
	if li:
	    print li
	    with open('2_fsrcnntrainclsloss.txt', 'a+') as f:
	        f.write(li[0] +'\n')
