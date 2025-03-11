# x  = True
# y = False 
# print("x or y is", not y)

# for i in range(100, 126, 2):
#     print(i)

# while number < 125:
#     number = number + 1
#     print(number)

# lists = [1, 30, 40, 50, 60, 70, 100, 920]
# lists.sort()
# print(lists[0])

# fruit_list = ['apple', 'orange', 'pear', 'bannan', 'apple', 'apple', 'bannan', 'pear', 'orange']
# fruit_count = {}

# for fruit in fruit_list:
#     if fruit in fruit_count:
#         fruit_count[fruit] += 1
#     else:
#         fruit_count[fruit] = 1
# print(fruit_count)

def area_tri(length, breath):
    area = 0.5 * length * breath
    print(area)

user_input_1 = int(input("Enter the length of the triangle: "))
user_input_2 = int(input("Enter the breath of the triangle: "))
area_tri(user_input_1, user_input_2) 