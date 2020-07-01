num=[10,20,30]
print("the numbers are : ", num)
if num[0] > num[1]:
    if num[0] > num[2]:
        print("biggest number is ", num[0])
elif num[2] > num[1]:
    if num[2] > num[0]:
        print("biggest number is ", num[2])
else:
    print("biggest number is ", num[1])