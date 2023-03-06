class Rectangle():
    def __init__(self, width, lenght):
        self.__width = width
        self.__lenght = lenght
        
    def get_width(self):
        return self.__width
    def get_lenght(self):
        return self.__lenght
    
    def set_width(self, width):
        self.__width = width
        print(self.__width)
    def set_lenght(self, lenght):
        self.__lenght = lenght
        print(self.__lenght)
        
    def perimeter(self):
        resultat= 2*(self.__width + self.__lenght)
        print(resultat)
        
    def area(self):
        resultat= self.__width * self.__lenght
        print(resultat)
        
        
class parallelopipede(Rectangle):
    def __init__(self, heigth):
        Rectangle.__init__(self, 2, 3)
        self.__heigth = heigth
    
    def volume(self):
        resultat= self.__heigth * (self.get_lenght() * self.get_width())
        print(resultat)
        
p=Rectangle(2, 3)
print(p.get_width())
print(p.get_lenght())
p.set_width(4)
p.set_lenght(5)
p.perimeter()
p.area()

para=parallelopipede(2)
para.volume()

        