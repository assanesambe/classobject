"""class Point3D:
    def intialiser(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

# Create an instance of Point3D
my_point = Point3D(x=1, y=2, z=3)

# Print the instance
print(my_point)

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

# Create an instance of Rectangle
my_rectangle = Rectangle(width=3, length=4)

# Compute and print the area and perimeter
print("Area:", my_rectangle.area())
print("Perimeter:", my_rectangle.perimeter())

import math

class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def is_inside(self, x, y):
        # Compute the distance between the point (x, y) and the center (center_x, center_y)
        distance = math.sqrt((x - self.center_x) ** 2 + (y - self.center_y) ** 2)
        return distance <= self.radius

# Create an instance of Circle
my_circle = Circle(center_x=0, center_y=0, radius=5)

# Compute and print the area and perimeter
print("Area:", my_circle.area())
print("Perimeter:", my_circle.perimeter())

# Test if a point is inside the circle
point_x, point_y = 3, 4
print(f"Point ({point_x}, {point_y}) is inside the circle:", my_circle.is_inside(point_x, point_y))

class Banque:
    def __init__(self, solde_initial):
        self.solde = solde_initial

    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            print(f"Dépôt : ${montant:.2f}")
        else:
            print("Le montant du dépôt doit être positif.")

    def retirer(self, montant):
        if montant > 0:
            if montant <= self.solde:
                self.solde -= montant
                print(f"Retrait : ${montant:.2f}")
            else:
                print("Fonds insuffisants.")
        else:
            print("Le montant du retrait doit être positif.")

    def obtenir_solde(self):
        return self.solde

# Créer une instance de Banque
mon_compte = Banque(solde_initial=1000)

# Effectuer des opérations
mon_compte.deposer(200)    # Dépose 200$
mon_compte.retirer(150)    # Retire 150$
mon_compte.retirer(1200)   # Essaye de retirer plus que le solde

# Imprimer le solde final
print("Solde final : ${:.2f}".format(mon_compte.obtenir_solde()))

"""