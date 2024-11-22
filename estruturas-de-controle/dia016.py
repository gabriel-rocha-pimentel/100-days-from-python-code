# Ordenação de Lista
# Crie uma função que ordene uma lista em ordem crescente

def ordenar_lista(lista):
  lista_ordenada = []
  
  contador = 0

  while contador < len(lista):
    ecnontrar_numero = lista.index(min(lista))
    menor_numero = lista.pop(ecnontrar_numero)
    lista_ordenada.append(menor_numero)

  print(f"Estes são os seus números ordenados {lista_ordenada}")

ordenar_lista([2,35,13,51,51,3,5,13,20,152])
