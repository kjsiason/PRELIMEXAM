class Area:
    def __init__(self, l, w, r):
        self.l = l
        self.w = w
        self.r = r
    def __str__(self):
        return f"{self.l} {self.w} {self.r}"

circle = 3.14*(1*1)
rectangle = 2*2
p1 = Area("l= 0,", "w= 0," ,"r= 1")
p2 = Area("l= 2,", "w= 2,", "r= 0")
print(p1)
print("Area of circle is=", circle)
print(p2)
print("Area of rectangle is=", rectangle)