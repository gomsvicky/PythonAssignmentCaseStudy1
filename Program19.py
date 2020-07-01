num = 100
print("Even numbers from 1 to 100")
for i in range(num):
    if i % 2 == 0:
        print(i)
print("Break when number is 50")
for i in range(num):
    if i == 50:
        break
    else:
        print(i)

print("continue when 10,20,30,40,50")
for i in range(1, num):
    if i == 10 or i == 20 or i == 30 or i == 40 or i == 50:
        continue
    print(i)

print("print even numbers using while loop")
i = 1
while i < num:
    if i % 2 == 0:
        print(i)
    i += 1


print("Break when number is 90")
i = 1
while i < num:
    if i == 90:
      break
    print(i)
    i += 1


print("Continue when i is 60,70,80 or 90")
i = 1
while i < num:
    if i == 60 or i == 70 or i == 80 or i == 90:
      i += 1
      continue
    print(i)
    i += 1
