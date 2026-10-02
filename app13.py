# Iterando dicionário
import os
os.system('cls')

prods = {
    "cod": "123abc", # Antes do : se chama chave. Depois do : é valor
    "name": "Caixa de sapato vazia",
    "fabr": "Caixeiro Viajante",
    "preco": 120.99
}

print(prods)
print()

for prod in prods:
   # print(prods[prod])
   print(f' • {prod} - {prods[prod]}')

print()
print('------', prods.keys()) # esse metodo keys, pega a chave do dicionario, o valor antes do :
for prod in prods.keys(): 
    print(prod)

print()
print('------', prods.values()) #esse metodo values, pega o valor do dicionario, o valor após :
for prod in prods.values():
    print(prod)     

# Para exibir os dois valores
'''
print()
print('------', prods.items())
for prod_key, prod_value in prods.items():
    print(f' • {prod_key.capitalize()} - {prod_value}')
'''

print()
print('------', prods.items())
for x, y in prods.items(): # o x, y é a chave e o valor do dicionario. 
   print(f' • {x.capitalize()} - {y}')


