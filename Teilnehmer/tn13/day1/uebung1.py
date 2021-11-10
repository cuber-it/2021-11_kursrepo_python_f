import os,glob,sys
import hashlib as hashlib
import pprint as pp

#E
path = os.path.dirname(sys.argv[0])+'/datapath'

#V
paths = os.listdir(path)

files = []
hashvalues = []

for p in paths:
    print(path+p+'/*.txt')
    files += (glob.glob(path+'/'+p+'/*.txt'))

for f in files:
    with open(f, "rb") as data: # opens TDMS file that shall be added to the database
        datatemp = data.read() # reads binary data from file
        hashvalues.append(hashlib.md5(datatemp).hexdigest()) # calculates md5 checksum

filedict = {}

for i in range(len(hashvalues)):
    try: 
        filedict[hashvalues[i]]
        filedict[hashvalues[i]] += [files[i]]
    except KeyError: 
        filedict[hashvalues[i]] = [files[i]]

#A
pp.pprint(filedict)