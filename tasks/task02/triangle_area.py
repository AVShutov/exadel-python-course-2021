import math

def area_base_height():
    values = input("Enter base and height: ").split(" ")
    if len(values) != 2 or not all(i.isdigit() for i in values) or not all(int(i) >= 0 for i in values):
        print(f"\nCheck values (only two positive numbers greater than zero are allowed).\n")
        return area_base_height()
    else:
        base = int(values[0])
        height = int(values[1])
        return (height * base) / 2

def area_2sides_angle():
    values = input("Enter 2 sides and angle(degrees) between them: ").split(" ")
    if len(values) != 3 or not all(i.isdigit() for i in values) or not all(int(i) >= 0 for i in values):
        print(f"\nCheck values (only three positive numbers greater than zero are allowed).\n")
        return area_2sides_angle()
    else:
        side1 = int(values[0])
        side2 = int(values[1])
        angle = int(values[2])
        return (side1 * side2 * math.sin(math.radians(angle))) / 2

print ("Welcome to the triangle area calculation tool.\n")

menu = '''Menu:
1. Calculate triangle area by base and height
2. Calculate triangle area by 2 sides and angle between them
3. Exit'''

menu_item = 0

while menu_item != 3:
    print(menu)
    menu_item = int(input("Enter menu item number: "))
    if menu_item == 1:
        area = area_base_height()
        print(f"\nTriangle Area is:  {area:.2f}\n")
    elif menu_item == 2:
        area = area_2sides_angle()
        print(f"\nTriangle Area is:  {area:.2f}\n")
    elif menu_item == 3:
        break
    else:
        print("\nMenu item number is not correct\n")