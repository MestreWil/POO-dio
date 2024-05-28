class MeuIterador:
  
  def __init__(self, numeros: list[int]):
    self.numeros = numeros
    self.contador = 0
  
  def __iter__(self):
    return self
  
  def __next__(self):
    try: 
      numero = self.numeros[self.contador]
      self.contador += 1
      return numero * 2
    except IndexError:
      raise StopIteration
  
for i in MeuIterador(numeros= [38, 13, 11, 2, 3]):
  print(i)
  
# Trabalhando com objetos dos tipos iteraveis

# O python tem mecanismos para trabalhar com objetos iteraveis(um objeto que contem um numero contavel de valores que podem ser iterados, 
# que significa que vc pode percorrer todos os valores) para criar um objeto iteravel vc precisa de dois metodos especiais (__iter__() e __next__())

