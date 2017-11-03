
if __name__ == '__main__':
    with open('caltech_person.txt') as f:
	lis = f.readlines()
    for li in lis:
	li = li[:-1]
        listr = li.split(' ')
        with open('caltech_person1.txt','a+') as f:
 	    f.write(listr[0]+' '+listr[1]+' '+str(int(float(listr[2])))+' '+str(int(float(listr[3])))+' '+str(int(float(listr[4])))+' '+str(int(float(listr[5])))+'\n')

