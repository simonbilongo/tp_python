# saisi de nombre positif ou negatif
nombre = input("Veuillez saisir un nombre :")
# nombre_converti = int(nombre) # converssion en entier du nombre saisi par l'utilisateur
try:
    nombre_converti = float(nombre) # converssion en decimal du nombre saisi par l'utilisateur
    print(type(nombre_converti)) # affichage du type de variable

    if nombre_converti > 0:
        print(f'le nombre {nombre_converti} est positif')
    elif nombre_converti < 0:
        print(f'le nombre {nombre_converti} est negatif')
    else:
        print(f'le nombre {nombre_converti} est nul')
except:
    print("Vous n'avez pas saisi un entier")