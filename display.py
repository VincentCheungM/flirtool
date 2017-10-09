import numpy as np
import matplotlib.pyplot as plt
import sys

if __name__=='__main__':

    file = 'data.txt'
    if(len(sys.argv)>1):
        print ('displaying {}'.format(sys.argv[1]))
        file=sys.argv[1]
    #read matrix
    img = np.loadtxt(file)
    #new figure
    fig = plt.figure()
    ax_0 = fig.add_subplot(111)
    ax_0 = plt.imshow(img,cmap='gray',norm=plt.Normalize(vmin=np.min(img),vmax=np.max(img)))
    plt.show()
