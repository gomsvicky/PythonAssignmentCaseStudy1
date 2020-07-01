num = input("enter number of employees :")
num = int(num)

list1 = []
list2 = []
for i in range(1, num + 1):
    ele = int(input("Enter Emp ID: "))
    list1.append(ele)
for i in range(1, num + 1):
    ele = input("Enter Emp Name: ")
    list2.append(ele)

print("Emp ID of all users: ", list1)
print("Emp Name of all users :", list2)

search = int(input("enter any index number "))
print("emp id: ", list1[search])
print("emp ID: ", str(list1[search]) + " and Emp Name: ", str(list2[search]))
print("emp ID: ", str(list1[3:9]) + " and Emp Name: ", str(list2[3:9]))
print("emp ID: ", str(list1[2:]) + " and Emp Name: ", str(list2[2:]))
print("emp id : ", str(list1) + "and emp name: ", str(list2))
i=0
while i < num:
    print(str(list1[i]), str(list2[i]))
    i += 1
