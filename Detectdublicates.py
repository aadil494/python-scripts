import hashlib
import numpy
import matplotlib.pyplot as plt
import os 

# Creating a list to  store dublicates
dublicates = []

# Creating a dict to store hashes and indexes of the images
hash_keys = dict()

#changing current working directory
os.chdir("C:\\Users\\Aadil\\Pictures\\Nature")

#Listing out all the files in a current working directory
file_list = os.listdir(".")

# Looping over all  the files creating a hexadecimal fingerprint of each file
for index,filename in enumerate(file_list):
	if os.path.isfile(filename):#checking if the filename is actually a file 
		with open(filename,'rb') as f:
			#md5 is a hashing function which takes a byte of data and returns a 128 bit hash value
			filehash = hashlib.md5(f.read()).hexdigest() #Hexdigest returns the encoded data in hexadecimal format
		if filehash not in hash_keys: #if this hash already exists in the dictionary then it is a dublicate , add it to dublicate list
			hash_keys[filehash] = index
		else :
			dublicates.append((index,hash_keys[filehash]))

print(dublicates)



for file_indexes in dublicates:
	try:
		plt.subplot(121)
		plt.imshow(plt.imread(file_list[file_indexes[1]]))

		plt.subplot(122)
		plt.imshow(plt.imread(file_list[file_indexes[0]]))
		plt.show()
	except:
		pass


for file_indexes in dublicates:
	os.remove(file_list[file_indexes[0]])