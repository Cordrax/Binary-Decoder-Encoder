def convert_binary_decimal(num):
  index = 0
  num = num[::-1]
  for i in range(len(num)):
    if num[i] != "0" and num[i] != "1":    #Vérifie que l'entrée n'a pas d'erreur
      return "wrong"
    elif num[i] == "1":
      index += 2**i   #Convertit en décimal
  return index

def decode_binary(ipt):
  num_index=0   #Sert à prendre l'index du nombre commençant après un "/" dans une entrée à décoder
  ee=""
  decoded=""
  nums=[]
  char=" abcdefghijklmnopqrstuvwxyz0123456789+-*/.,()[]:;_%"
  for i in range(len(ipt)):
    if ipt[i] == "/":
      nums.append(ipt[num_index:i])   #Rajoute le nombre précédent à la liste des nombres
      num_index = i+1   #Prend l'index du nombre commençant après le "/"
  nums.append(ipt[num_index:len(ipt)])  #Ajoute le dernier nombre
  for number in nums:
    cap = 0
    if number[-1] != "0" and number[-1] != "1":
      cap = int(number[-1])   #Utilisé pour savoir s'il faut ou non écrire le caractère en majuscule
      number = number[0:-1]   #Sert à retirer les caractères de séparation ou de majuscule
    char_index = convert_binary_decimal(number)   #Renvoie l'index de la chaine "char" auquel correspond le nombre
    if char_index == "wrong":
      return "Votre entrée est invalide"
    if cap == 2:
      decoded += char[char_index].upper()
    else:
      decoded += char[char_index]
  return decoded


