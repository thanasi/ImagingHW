import numpy as np

#convert integer to binary number string
def int2bin(n, pad=1):
    if n==0: return '0'*pad
    nbits = int(np.ceil(np.log2(n+1)))
    binrep = np.zeros(nbits)
    temp = n    
    for i in np.arange(nbits)[::-1]:
        if temp < 2**i:
            pass
        else:
            binrep[i]=1
            temp -= 2**i
    binstr = ''
    for i in binrep[::-1]:
        binstr += str(int(i))

    #if the bin number has too few characters
    #then pad the front with zeros
    if pad>len(binstr):
        binstr = '0'*(pad-len(binstr))+binstr
    return binstr
    
with open('out4.txt','w') as outfile:
    for i in range(16):
        outfile.write('{}\t{}\t'.format(i,int2bin(i,4)))
        outfile.write('\n'*(i%2))
