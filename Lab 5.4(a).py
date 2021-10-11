#Student ID:1201201282
#Student Name :TAY XI YANG

def rectangle(length, width):
    area=length*width
    return length*width

def triangle(length, width):
    area=(length *width)/2
    return (length *width)/2

width=float(input("Enter width :"))
length=float(input("Enter length: "))

totalarea_rectangle=rectangle(length, width)
totalarea_triangle=triangle(length, width)

print("Rectangle area : {:.2f}".format(totalarea_rectangle))
print("Triangle area  : {:.2f}".format(totalarea_triangle))
