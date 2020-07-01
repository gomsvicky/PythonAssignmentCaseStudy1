def big(list1):
    max = list1[0]
    for x in list1:
        if x > max:
            max = x
    return max


def small(list1):
    small = list1[0]
    for x in list1:
        if x < small:
            small = x
    return small


list1 = []
num = input("Enter number of elements in list: ")
num = int(num)

for i in range(1, num + 1):
    ele = input("Enter elements: ")
    list1.append(ele)
print("Largest element is:", big(list1))
print("Smallest element is:", small(list1))
