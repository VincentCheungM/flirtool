import csv
import numpy as np
import glob


def mkdir(path):
    import os
    #remove blank
    path=path.strip()
    #remove last \\
    path=path.rstrip("\\")
    #check file exist?
    isExists=os.path.exists(path)
 
    # not exists then create
    if not isExists:
        os.makedirs(path) 
 
        print ('{} create sucess').format(path)
        return True
    else:
        print ('{} create failed, folder exists').format(path)
        return False

if __name__=='__main__':
    OUTPUT_PATH = './outputs'
    mkdir(OUTPUT_PATH)

    for filename in glob.glob('*.csv'):
        print ('performing {}').format(filename)
        file = filename.split('.csv')[0]
        #matrix is 240x320
        mat = np.zeros((240,320))
        with open(filename,'rb') as f:
            reader = csv.reader(f)
            offset = 0
            temp = open(filename,'rb')
            if len(temp.readlines()) == 251:
                offset = 8
            # two kinds csv: 1. 251 rows with parameters
            #                2. 243 rows without parameters

            i = 0
            for row in reader:
                i+=1    
                if i >=3+offset and i <= 242+offset:
                    #only row 3 - row 242 is temperature
                    mat[i-3-offset] = row[1:321]
        #print len(lis)
        #print mat
        np.savetxt(OUTPUT_PATH+'/'+file+'.txt',mat,fmt='%.3f')  
        print ('saved '+OUTPUT_PATH+'/'+file+'.txt')
    print('Done')