emp_file = open("employees.txt", "r")    ## Read file

# open("employees.txt", "w")             ## Write to file

# open("employees.txt", "a")             ## Append to file (Can't change anything, Only appending to file)

# open("employees.txt", "r+")            ## Read from and write to file

print(emp_file.readable())               ## True

print("                                        ")
print("                                        ")

## print(emp_file.read())                ## Read the entire file

print("                                        ")
print("                                        ")

print(emp_file.readline())               ## Read the first line
print("                                        ")
print("                                        ")

print(emp_file.readlines())              ## Read all lines and put them in an array
                                         ## ['Casillas - Manager\n', 'Ronaldo - Footballer\n', 'Modric - Artist\n']

## Important Note: Using .readline() after .read() will print nothing

emp_file.close()




