import stock

menuActions = {
  "1": stock.check,
  "2": stock.insert,
  "3" : stock.remove,
  "0": quit
} 

menus = [
    "1 - Conferir estoque",
    "2 - Inserir celular",
    "3 - Saida celular",    
    "0 - Sair"
]

while True:
    for menu in menus:
        print(menu, end="\n")
    key = input("Digite o numero do menu: ")    
    if key in menuActions:
        action = menuActions[key]
        action()
    else:
         print("Menu invalido: %s" %action)
