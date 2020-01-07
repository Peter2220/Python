## Creating a list, All elements same Data Type
My_Friends     = ['Kevin', 'Carvajal', 'Ramos']

My_Friends_2   = ['Casillas', 'Varane', 'Ronaldo' , 'Varane']

Random_Numbers = [ 4, 9, 65, 35, 88, 2, 62, 1]


## Multiple Data Types
Random_List = ['Wallace', False, 3 , 5.9 ]

Random_List_2 = ['Kevin', True, 555 , 904.2 ]

print(My_Friends[0])  ## Kevin

print(My_Friends[-1]) ## Ramos

print(My_Friends[1:]) ## ['Carvajal', 'Ramos']


## Modifying an element in a list

My_Friends[1] = 'Modric'

print(My_Friends)     ## ['Kevin', 'Modric', 'Ramos']


## Extend, Append, Insert, Remove, Clear and Pop functions

Random_List.extend(My_Friends) ## ['Wallace', False, 3, 5.9, 'Kevin', 'Modric', 'Ramos']

Random_List_2.append("Ramos")  ## ['Kevin', True, 555, 904.2, 'Ramos']

My_Friends_2.insert(1,'Nacho') ## ['Casillas', 'Nacho', 'Varane', 'Ronaldo', 'Varane']

## My_Friends_2.remove('Casillas') ## Remove an element from My_Friends_2 list

## My_Friends_2.clear()        ## Remove all elements from any list(empty list)

## My_Friends_2.pop()          ## Remove the last element from a list

My_Friends_2.index('Varane')   ## 1

My_Friends_2.count('Varane')   ## 2 

Random_Numbers.sort()          ## [1, 2, 4, 9, 35, 62, 65, 88]

Random_Numbers.reverse()       ## Reverse the order of a list

Random_Numbers_2 = Random_Numbers.copy()
print(Random_Numbers_2)
