class car:
    def __init__(self,a,b,c):
        self.brand=a
        self.model=b
        self.color=c
    def show(self):
        print(self.brand)
        print(self.model)
        print(self.color)
obj=car(1,2,3)
obj.show()