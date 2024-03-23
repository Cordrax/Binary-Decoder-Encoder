def convert_decimal_binary(num):
  power = 1   #Puissance à laquele élever 2 correspondant
  num_bin = ""    #Le nombre en binaire
  while 2**power <= num:
    power += 1
  for i in range(power):    #Convertit en binaire
    power -= 1
    if num - 2**power >= 0:   #On soustrait si l'on peut la puissance de 2 et on la rajoute dans le nombre binaire convertit
      num -= 2**power
      num_bin += "1"
    else:
      num_bin += "0"
  return num_bin



def encode_binary(to_encode):
  encoded=""
  char=" abcdefghijklmnopqrstuvwxyz0123456789+-*/.,()[]:;_%"
  for i in range(len(to_encode)):   #Parcourt tous les éléments de l'entrée à décoder
    for j in range(len(char)):    #Parcourt tous les éléments de la liste de caractères
      if to_encode[i] == char[j] or to_encode[i] == char[j].upper():
        encoded += convert_decimal_binary(j)    #Convertit la position du caractère dans la liste de caractères en décimal
        if to_encode[i] == char[j].upper() and char[j].upper() != char[j]:    #Vérifie si le caractère est en majuscule
          encoded+="2"    #Sert à préciser que le caractère est en majuscule
        if i != len(to_encode)-1:
          encoded += "/"    #Rajoute un "/" pour séparer les nombres si ce n'est pas la fin de l'entrée
  return encoded



