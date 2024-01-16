# declation et affectation
# x =3
# y= 5
x,y,*a =[12,15,10,12,13] # affectation des variables par destructuration
print(a)
z=x*y
nombre = 0.17
test = 2 > 3
print(test)
# affichage et lecture
print(f"Le type de la variable x est: {type(x)}") # type() est une fonction python qui retourne le type d'une variable
print(f"Le type de la variable nombre est: {type(nombre)}") # type() est une fonction python qui retourne le type d'une variable
print(f"Le type de la variable test est: {type(test)}") # type() est une fonction python qui retourne le type d'une variable

print(f"Le produit de {x} et {y} donne : {z}")
print("Le produit de " + str(x)+" et "+str(y)+" donne : "+str(z)) # la fonction str() permet de convertir une varibale d'un autre type en string. Afin d'afficher le resultat

chaine = """
ma classe est bien jolie 
elle a deux porte
et deux fenetre
"""
# affectation ou affichage d'une chaine de caractere ou un memo sur plusieurs lignes
print(chaine)

# papa simon

# structure conditionnelle

if x > y:
    print(f"""{x} est superieur a {y}""")
elif x == y:
    print(f"{x} egale a {y}")
else:
    print(f'{x} est inferieur a {y}')
    
# structure iterative

# liste: tableau, tuple, liste en comprehension ["simon", 30, "Docteur"]

# dictionnaire {prenom:"simon", age:30, niveau_etude:"Docteur"}




