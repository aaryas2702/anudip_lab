def read_file():
    #Open the file "ABC.txt" in read mode
    file = open("ABC.txt", "r")
    
    #Loop through each line in the file
    for line in file:

        #Print the current line after removing any extra spaces or newlines
        print(line.strip())
    
    #Close the file after reading
    file.close()

#output
    Hello, Good Morning.
