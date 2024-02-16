import os
# Write a program that opens a text file and reads the contents of the file.
curr_dir=os.getcwd()
file_path=os.path.join(curr_dir,'Day7/sample.txt')
file=open(file_path,'r')
print(file.read())
file.close()



# Write a program that opens a text file and writes some text to the file.
file=open(file_path,'w')
file.write("this is a sample text to check the writing operation")
file.close()


# Write a program that opens a binary file and reads the first 10 bytes of the file.
file_path2=os.path.join(curr_dir,'Day7/sample2.bin')
f = open(file_path2,"rb")
data = f.read()
print(type(data))
print(data)
f.close()


# Write a program that creates a new text file, writes some text to the file, and then renames the file.
file_path=os.path.join(curr_dir,'Day7/sample3.txt')
f=open(file_path,'w')
f.write("this is a used to creating file and writing the content on the file at the same time")
f.close()
os.rename(file_path,'new_sample3.txt')


# Write a program that deletes a text file.
os.remove('new_sample3.txt')