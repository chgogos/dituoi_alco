a_dict = {}
for _ in range(10):
    i = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    a_dict[i] = name

while True:
    i = int(input("Enter student ID: "))
    if i in a_dict:
        print("Hello ", a_dict[i])
    else:
        break
