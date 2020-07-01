list1 = (10,22,33,54,65,76,87,98,39,110)
for i in range(len(list1)):
    print("print all elements ", i ," :", list1[i])
print("Slicing operator")
print(list1[0:5], list1[4:8], list1[2:6], list1[7:9])
print("Performed Repetition")
print(list1*100)
print("Concetenation")
print(list1[3:5]+list1[0:2]+list1[8:9])
