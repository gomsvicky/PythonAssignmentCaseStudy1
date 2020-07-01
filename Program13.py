list1 = []
num = input("Enter number of elements in list: ")
num = int(num)

for i in range(1, num + 1):
    ele = input("Enter elements: ")
    list1.append(ele)
print("Entered elements ", list1)
max1 = list1[0]
for x in list1:
    if x > max1:
        max1 = x
        print("Biggest number is ", max1)
