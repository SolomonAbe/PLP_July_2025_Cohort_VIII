# creating list in Python
my_list = []

# apending data to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)


#inserting value at second position
my_list.insert(1,15)


#extend more data to my list
my_list.extend([50,60,70])


#removing last list item
my_list.pop()


#sorting my list
my_list.sort()

#finding index and print
i= my_list.index(30)
print(i)