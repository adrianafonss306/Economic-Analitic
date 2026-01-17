# #def mezcla(lista1,lista2):
# resultado = []
# lista1 = [1,5,12,56,98,102]
# lista2 = [2,3,13,78,98,102,105,123,256]

# i,j = 0,0
# while i < len(lista1) and j < len(lista2):
#     if lista1[i] < lista2[j]:
#         resultado.append(lista1[i])
#         i += 1
#     else:
#         resultado.append(lista2[j])
#         j += 1
# while i < len(lista1):
#     resultado.append(i)
#     i += 1
# while j < len(lista2):
#     resultado.append(lista2[j])
#     j += 1

# print(resultado)

# #mezcla(lista1,lista2)    



import json

with open ("./proyecto_icd.json","r", encoding = "utf-8") as file:
    data = json.load(file)
    
    mipymes = data["mipymes"]
    
    for i in mipymes:
        print(i)