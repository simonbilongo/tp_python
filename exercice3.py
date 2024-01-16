# Saisie de 2 nombres entiers
# Structure conditionnelle

nombre1=float(input("Saisissez un premier nombre : "))
nombre2=float(input("Saisissez un dexieme nombre : "))
# resultat=nombre1*nombre2

# le produit de deux entiers n1 et n2 est positif si n1 > 0 et n2 > 0 ou n1 < 0 et n2 < 0
# le produit de deux entiers n1 et n2 est negatif si n1 > 0 et n2 < 0 ou n1 < 0 et n2 > 0

if (nombre1 > 0 and nombre2 >0) or (nombre1 < 0 and nombre2 < 0):
    print(f'La multiplication donne un nombre positif')
elif (nombre1 > 0 and nombre2 <0) or (nombre1 < 0 and nombre2 > 0):
    print(f'La multiplication donne un nombre negatif')
