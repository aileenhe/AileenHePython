#Functions:#
def helloworld():
      print("\n----Start of Output ---------------------------")
      print("\nHello World")
      print("\n----End of Output -----------------------------")

def goodbyeworld():
      print("\n----Start of Output ---------------------------")
      print("\nGoodbye World")
      print("\n----End of Output -----------------------------")

def goodbyeperson():
      print("\n----Start of Output ---------------------------")
      print("\nHello") 
      name = input("What is your name ? ")
      print("Goodbye",name)
      print("\n----End of Output -----------------------------")
    
def goodteacher():
      print("\n----Start of Output ---------------------------\n")
      name = input("Teacher's name (try Mr Horan) ")
      if  name == "Mr Horan":
        print("You are lucky, he is a great teacher") 
      else:
        print(name,"is an okay teacher.")
      
def forloop():
      print("\n----Start of Output ---------------------------\n")
      for x in range(1,500):
          print(x)
      print("\n----End of Output -----------------------------")
      
def whileloop():
      print("\n----Start of Output ---------------------------\n")
      ans = input("What is the name of this class? ")
      while ans != ("IST"):
          print("Not correct - try again")
          ans = input("What is the name of this class? ")
          continue
      else:
          print("\nCongratulations!!")

def stringloop():
  print("\n----Start of Output ---------------------------")
  str1 = input ("\nWhat is your string? ")
  for i in range(len(str1)):
    print(str1[i])
  print("\n----End of Output -----------------------------")

def convert():
    print("\n----Start of Output ---------------------------")
    str1 = input ("\nWhat is your string? ")
    ascii_values = []
    equal_sign = ('=')
    for character in str1:
        ascii_values.append(ord(character))
    for i in range(len(str1)): 
      print(str1[i],equal_sign,ascii_values[i], sep="")
    print("\n----End of Output -----------------------------")

def invalid():
      print("\n----Start of Output ---------------------------")
      print("\ninvalid option")
      print("\n----End of Output -----------------------------")

def exit():
      print("\n----Start of Output ---------------------------")
      print("\n----End of Output -----------------------------")

#Printing The Box:#
while True:
  # main program
  print(" ------------------------------------------------") 
  print("|                                                |")
  print("|    07Menu                                      |")
  print("|    Name : Aileen He                            |") 
  print("|    Version : 01                                |")
  print("|                                                |")
  print(" ------------------------------------------------")

  #Printing The Variables:#
  print("1. Hello World")
  print("2. Goodbye World")
  print("3. Goodbye Person")
  print("4. Good Teacher")
  print("5. forLoop")
  print("6. whileLoop")
  print("7. stringLoop")
  print("8. Convert to ascii")
  print("9. Encode a string")
  print("x. To Exit")

  #User imputs:#
  option = input("Enter an option ")
  if option == ("1"):
    helloworld()
    clear = input("\n\n\nPress Enter to continue")
    if clear == "":
      continue

  if option == ("2"):
    goodbyeworld()
    clear = input("\n\n\nPress Enter to continue")
    if clear == "":
      continue
              
  if option == ("3"):
    goodbyeperson()
    clear = input("\n\n\nPress Enter to continue")
    if clear == "":
      continue
              
  if option == ("4"):
    goodteacher()
    clear = input("\n\n\nPress Enter to continue")
    if clear == "":
      continue
              
  if option == ("5"):
    forloop()
    clear = input("\n\n\nPress Enter to continue")
    if clear == "":
      continue
              
  if option == ("6"):
    whileloop()
    clear = input("\n\n\nPress Enter to continue")
    if clear == "":
      continue
  
  if option == ("7"):
    stringloop()
    clear = input("\n\n\nPress Enter to continue")
    if clear == "":
      continue

  if option == ("8"):
    convert()
    clear = input("\n\n\nPress Enter to continue")
    if clear == "":
      continue
    
  if option == ("9"):
    invalid()
    clear = input("\n\n\nPress Enter to continue")
    if clear == "":
      continue
              
  if option == ("x"):
    clear = input("\n\n\nPress Enter to continue")
    if clear == "":
      break

  else:
    print("\n----Start of Output ---------------------------")
    print("\ninvalid option")
    print("\n----End of Output -----------------------------") 
    clear = input("\n\n\nPress Enter to continue")
    if clear == "":
      continue