import pickle

# dumping(serializing) the data in pickel1 file

# li =  [1,2,3,4,5]
# file  =open("pickel1.txt","wb")
# pickle.dump(li,file)
# file.close()

# loading(de-serializing) the data from pickel1 file

file = open("pickel1.txt","rb")
li = pickle.load(file)
print(li)