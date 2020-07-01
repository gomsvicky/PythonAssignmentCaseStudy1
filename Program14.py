namelist = ['one', 'two', 'three', 'four', 'five']
user = input("Enter a name: ")
if user in namelist:
    print("Given value is there using IN operator")
for i in namelist:
    if i == user:
        print("The Given name is in list without using IN operator")
for i in namelist[::-1]:
    print(i)