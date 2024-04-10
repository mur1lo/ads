cellPhones = {
  "IPHONE 15": 5,
  "MOTOROLA G5": 7
}


def check():
  print("------------------ Celulares --------------------------")
  pattern = '{:>20}{:>20}'       
  print(pattern.format('Modelo','Quantidade'))
  print("")  
  for key, value in cellPhones.items():
    print(pattern.format(key.capitalize(), *str(value)))
  print("-------------------------------------------------------")  

def insert():
    model = input("Digite o modelo: ").upper()
    quantitity = int(input("Digite a quantidade: "))
    if model in cellPhones:
      quantitity += cellPhones[model]
      
    cellPhones.update({model: quantitity})
    
def remove():
    model = input("Digite o modelo: ")
    quantitity = int(input("Digite a quantidade: "))
    cellPhones.update({model: quantitity})