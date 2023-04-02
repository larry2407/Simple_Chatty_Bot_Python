angle_1 = int(input())
angle_2 = int(input())
angle_3 = int(input())
prefix = "The triangle is "
suffix = "valid!" if angle_1 + angle_2 + angle_3 == 180 else "not valid!"
print(prefix + suffix)
