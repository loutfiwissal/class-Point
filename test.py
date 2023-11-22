from Point import Point

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