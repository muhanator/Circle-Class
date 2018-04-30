#Muhammad Saad Mujtaba
#March 22, 2017

from CircleClass1 import Circle

from PointClass1 import Point, isclose

c1=Circle(radius=10)

c2=Circle(x=10)

c3=Circle(x=20,radius=10)

c4=Circle(x=5,radius=5)

c5=Circle(x=30)

#Externally Tangent
print(c1.tangent(c3))
print(c1.external_tangent(c3))
print(c1.internal_tangent(c3))
print()


#Internally Tangent
print(c1.tangent(c4))
print(c1.external_tangent(c4))
print(c1.internal_tangent(c4))
