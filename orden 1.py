# ordem crecente ou decrecente
print("valor A")
y = int(input())
print("valor B")
x = int(input())
print("valor C")
z = int(input())
if y < x < z:
    print(y ,x ,z)
elif y > x >z:
    print(z,x,y)
elif z < y < x:
    print(z,y,x)
elif x < z < y:
    (x,y,z)
elif z > y > x:
    print(x,y,z)
else:
    print(y,z,x)