class Rectangle:
    def __init__(self,length,breadth):
        self.__length=length
        self.__breadth=breadth
    def area(self):
        return  self.__length*self.__breadth
    def __lt__(self,rect2):
        return self.area<rect2.area
r1=Rectangle(2,3)
r2=Rectangle(4,5)
r1area=r1.area()
r2area=r2.area()
print("area of first triangl is ",r1area)
print("area of second triangl is ",r2area)
if r1area<r2area:
    print("rect 1 smaller")
else:
    print("rect2 smaller")
