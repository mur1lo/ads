#aqui definimos nossa base de dados em memoria, é um tipo de variavel que serve como um lista, onde vamos inserir nossos produtos
cellPhones = {
  "IPHONE 15": 10,
  "MOTOROLA G5": 7
}

# função check, faz a impressão na tela do que possui na nossa base dados
def check():
  print("------------------------------------------ Celulares ----------------------------------------------------------")
  pattern = '{: >20} {: >25}'       
  print(pattern.format('Modelo','Quantidade'))
  print("")  
  for key, value in cellPhones.items():
    print(f'{key :>20} {value :>25}')
  print("---------------------------------------------------------------------------------------------------------------")  

# funcao insert, faz a inclusao do produto na base de dados
def insert():
    model = input("Digite o modelo: ").upper()
    quantitity = int(input("Digite a quantidade: "))
    if model in cellPhones:
      quantitity += cellPhones[model]
      
    cellPhones.update({model: quantitity})
    
# funcao remove, faz a exclusao do produto na base de dados    
def remove():
    model = input("Digite o modelo: ")
    quantitity = int(input("Digite a quantidade: "))
    cellPhones.update({model: quantitity})

# aqui definimos a funcao que cria o menu
menus = {}
def menuAdd(option, name, func):
    menuName = f"{option} - {name}"
    menus[option] = [menuName, func]

# aqui criamos a sequencia dos menus seguido de digito, nome do menu, e a funcao que o menu executa
menuAdd("1", "Conferir estoque.", check)
menuAdd("2", "Inserir celular.", insert)
menuAdd("3", "Saida celular.", remove)
menuAdd("0", "Sair.", quit)

# aqui exibe os menus no console
while True:        
    for key, value in menus.items():
        print(value[0], end="\n")
    key = input("Digite o numero do menu: ")    
    if key in menus:
        action = menus[key]
        action[1]()
    else:
         print("Menu invalido: %s" %key)