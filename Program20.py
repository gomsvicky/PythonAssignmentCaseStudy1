num = int(input("Enter number of elements : "))
a = 0
b = 1
if num <= 0:
  print("please enter positive number")
elif num == 1:
  print("Fibonacci series:", a)
elif num == 2:
  print(a)
  print(b)
else:
    print(a)
    print(b)

while (num > 2):
  numnext = a + b
  if numnext < 100:
    print(numnext)
    a = b
    b = numnext
    num = num - 1
  else:
      break



