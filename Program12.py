n= input("Enter the numbers ")
numberlist = n.split()
print("All Entered numbers ", numberlist)
sum=0
count = count1 = count2 = 0

for num in numberlist:
    sum=sum+int(num)
    avg=sum/len(numberlist)

print("average of entered numbers", avg)
for num in numberlist:
    if int(num) > int(avg):
        count = count + 1
    elif int(num) < int(avg):
        count1 = count1 + 1
    else:
        count2 = count2 + 1
print(count, " is number which are less than average")
print(count1, " is number which are high than average")
print(count2, " is number which are equal to average")

