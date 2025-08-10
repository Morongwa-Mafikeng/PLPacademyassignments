#creating an empty list
my_list = []

#adding values to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#adding value to the second element in the list
my_list[1] = 15

#extending the list
my_list1 = [50, 60, 70]
my_list.extend(my_list1)

#removing the last element of the list
my_list.remove(my_list[-1])

#sorting the list in ascending order
my_list.sort()

#finding the index of the value 30 in the list

for element in range(len(my_list)):
    if my_list[element] == 30:
        print(element)