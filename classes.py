
# Create the following python classes inside shapes.py

# Class Circle
# A Circle instance accepts attribute radius (r)
# It has a method area that returns the area (A) of the circle using the formula A=πr2
# It has a method to calculate circumference (c) using the formula C=2πr



class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius **2)
        
y = Circle(10)
print("circum of circle:",y.area())

def circumfrence(self):
   return 2*3.14 * (self.radius **2)

# Class Square
# A Square instance accepts the attribute side (a)
# It has method area that returns the area (A) of the square using the formula A=a2
# It has a method to calculate the perimeter (P) of the square using the formula P=4a

class Square:
   def __init__(self,side):
       self.side=side
         
   def area(self): 
     side = 12
     return side*side 
   def perimeter(self):
        return 4 * (self.side**2)
   
#    Class Rectangle
# A Rectangle instance accepts two sides of a rectangle (w,l)
# It has method to calculate the area (A) of the rectangle using the formula A=wl
# It has a method to calculate the perimeter (P) of the rectangle using the formula P=2(l+w)

class Rectangle:
    def __init__(self, width,length):
        self.width = width
        self.lenght=length
    def area(self):
        return self.width ** self.length
    def perimeter(self):
        return 2*(self.width + self.length)
#     Class Sphere
# A Sphere Instance accepts the radius of the sphere (r)
# It has a method to calculate the surface area (A) using the formula A=4πr2
# It has a method to calculate the volume (V) of the sphere using the formula V = 4/3(πr3)

class Sphere:
    def __init__(self,radius):
        self.radius=radius
            
    def surface_area(self):
            A=4*3.14*(self.radius**2)
            return A
    def volume(self):
            return  4/3*(3.14 *self.radius*self.radius*self.radius)
            
            
            
        
        
        
        
        
        
    
        








