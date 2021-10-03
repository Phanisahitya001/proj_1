import math
rad=float(input("Input the radius of the circle :"))
res=math.pi * (rad ** 2)
print("The area of the circle with radius",rad,"is:",res)


#code for finding the file extension

filename=input("Input the filename: ")
filexten=filename.split(".")
if(filexten[-1]=="py"):
    print("The extension of the file is : "+repr("python"))
else:
    print("The extension of the file is : "+repr("filexten[-1"))
