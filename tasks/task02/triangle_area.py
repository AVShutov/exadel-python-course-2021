import math

def area_base_height():
    values = input("Enter base and height: ").split(" ")
    if len(values) != 2 or not all(i.isdigit() for i in values) or not all(int(i) >= 0 for i in values):
        print("Check values (only two positive numbers greater than zero are allowed).")
        return area_base_height()
    else:
        base = int(values[0])
        height = int(values[1])
        return (height * base) / 2

def area_by_sides_and_angle():
    values = input("Enter 2 sides and angle(degrees) between them: ").split(" ")
    if len(values) != 3 or not all(i.isdigit() for i in values) or not all(int(i) >= 0 for i in values):
        print("Check values (only three positive numbers greater than zero are allowed).")
        return area_by_sides_and_angle()
    else:
        side1 = int(values[0])
        side2 = int(values[1])
        angle = int(values[2])
        return (side1 * side2 * math.sin(math.radians(angle))) / 2

print ("Welcome to the triangle area calculation tool.")

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
        print(f"Triangle Area is:  {area:.2f}")
    elif menu_item == 2:
        area = area_by_sides_and_angle()
        print(f"Triangle Area is:  {area:.2f}")
    elif menu_item == 3:
        break
    else:
        print("Menu item number is not correct")
