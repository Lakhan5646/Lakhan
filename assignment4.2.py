text1=input("Enter text to write to the file: ")
file1=open("putput.txt","w")
file1.write(text1 + "\n")
file1.close
text2=input("Enter additional text to append:")
file2=open("output.txt","a")
file2.write(text2 + "\n")
file2.close
file3= open("output.txt","r")
print("Final content of output:")
reading_file=file3.read()
print(reading_file)
file3.close