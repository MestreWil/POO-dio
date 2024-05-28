def meu_gerador(numeros: list[int]):
  for numero in numeros:
    yield numero * 2

for i in meu_gerador(numeros=[1, 2, 3]):
  print(i)
  
# palavra reservada "yield" para retorno do gerador 
# vc usa gerador quando o codigo for simples
# quando o codigo for mais complexo (como uma arvore binaria) ai vc usa o iterador