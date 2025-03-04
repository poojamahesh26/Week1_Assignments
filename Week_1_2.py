#Display numbers at the odd indices of a list

list1 = [2,3,7,8,4,3,2,1,0,6,4,5,8]
for i in range(len(list1)):
    if(i % 2 != 0):
        print(list1[i])