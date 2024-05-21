class Bicicleta:
  def __init__(self, modelo, ano, cor, aro):
    self.modelo = modelo
    self.ano = ano
    self.cor = cor
    self.aro = aro
    
  def __str__(self):
    # Essa é uma solucao para metodo str onde podemos alterar a classe sem alterar o metodo str
    return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
  
bicicleta = Bicicleta('monark', 2000, 'rosa', 16)
print(str(bicicleta))