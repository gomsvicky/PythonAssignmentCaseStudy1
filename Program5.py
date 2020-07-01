import sys
print(sys.argv)
print("length of arguments ", len(sys.argv))
for i in sys.argv:
    print("arugment is ", i)
if sys.argv[3] > sys.argv[1] and sys.argv[3] > sys.argv[2]:
    print("biggest number is ", sys.argv[3])
elif sys.argv[2] > sys.argv[1] and sys.argv[2] > sys.argv[3]:
    print("biggest number is ", sys.argv[2])
else:
    print("biggest number is ", sys.argv[1])
