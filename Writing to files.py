Players_file = open("Players.txt", "a")  ## Appending text to file

Players_file.write("Sergio Ramos")

"""
If you run the previous line two times, your file will be like this:
Sergio RamosSergio Ramos
"""

Players_file.write("\nDaniel Carvajal")
"""
Sergio Ramos
Daniel Carvajal
"""

"""

Players_file = open("Players.txt", "w")   ## Overwriting a file
Players_file.write("Luka Modric")

"""

"""

Players_file = open("Players1.txt", "w")   ## Create a new file
Players_file.write("Luka Modric")          ## Write this text inside the file

"""


Players_file.close()
