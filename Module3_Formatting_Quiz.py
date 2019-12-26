Family_List = \
['Sergio Ramos', '4229  Beech Street', 'Antioch CA', '916.555.000']

My_List     = ['Daniel Carvajal', '3147  Doctors Drive', 'Los Angeles CA', '917.555.030']

Our_List    = ['Luka Jovic', '1455  Blvd County', 'Bedrock CA', '918.555.020']

His_List    = "Luka Modric,5823  Poplar Chase,New Meadows ID,919.555.010"


print("")
print("Name                 Address                 City                Phone")
print("------------------   ------------------      -----------------   -------")

print("{0:18}   {1:20}    {2:16}    {3:15}".format(Family_List[0],Family_List[1], Family_List[2], Family_List[3]).strip())
print("{0:18}   {1:20}    {2:16}    {3:15}".format(My_List[0],
                                                   My_List[1],
                                                   My_List[2],
                                                   My_List[3]).strip())

print("{0:18}   {1:20}    {2:16}    {3:15}".format(Our_List[0], Our_List[1], Our_List[2], Our_List[3]).strip())


list_1 = His_List.split(',')
print("{0:18}   {1:20}    {2:16}    {3:15}".format(list_1[0], list_1[1], list_1[2], list_1[3]).strip())
