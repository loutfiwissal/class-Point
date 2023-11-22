class Point () :
    def __init__(self,abscisse=0,ordonne=0) :
        self.__abscisse = abscisse
        self.__ordonne = ordonne

#Getters
    def getabscisse(self):
        return self.__abscisse

    def getordonne(self):
        return self.__ordonne
    
    def set_abscisse(self,abscisse):
        self.__abscisse = abscisse
    
    def set_ordonne(self,ordonne):
        self.__ordonne = ordonne
    
    def distance(self,p):
        x1,y1=self.getabscisse(),self.getordonne()
        x2,y2=p.getabscisse(),p.getordonne()
        return ((x2-x1)**2+(y1-y2)**2)*0.5
    
    def norme (self):
        return ((self.__abscisse)**2+(self.__ordonne)**2)**0,5

p1 = Point()
p2 = Point ()
p3 = Point ()

p2.set_abscisse(3)
p2.set_ordonne(5)

p3.set_abscisse(6)
p3.set_ordonne(8)

print ("p1,x:",p1.getabscisse())
print ("p1,y:",p1.getordonne())

print ("p2,x:",p2.getabscisse())
print ("p2,y:",p2.getordonne())

print ("p3,x:",p3.getabscisse())
print ("p3,y:",p3.getordonne())

print("The distance between point 2 and point 3 :",p3.distance(p2))
print ("The distance between point 2 and the origin of the coordinate system:",p2.norme())