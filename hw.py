class rectangle:
    def __init__(self, list_of_dots []):
        self.dots = list_of_dots
    def square(self):
        if self.list_of_dots[1][1] =! self.list_of_dots[2][1]:
            a = self.list_of_dots[1][1] - self.list_of_dots[2][1]
        elif self.list_of_dots[1][1] =! self.list_of_dots[3][1]:
            a = self.list_of_dots[1][1] - self.list_of_dots[3][1]
        else:
            a = self.list_of_dots[1][1] - self.list_of_dots[4][1]

        return(a*a)
    def perimeter(self):
        return(a*4)