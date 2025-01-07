class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        a=self.length*self.breadth
        return a
    def perimeter(self):
        b=2*(self.length+self.breadth)
        return b
rect1=Rectangle(2,3)
rect2=Rectangle(4,5)
if rect1.area()<rect2.area():
    print("rect 1 less than rect 2")
else:
    print("rect 2 is less that rect 1")
