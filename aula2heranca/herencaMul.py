class Animal:
  def __init__(self, nro_patas):
    self.nro_patas = nro_patas
  def __str__(self):
    # Essa é uma solucao para metodo str onde podemos alterar a classe sem alterar o metodo str
    return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
  # **kv é uma forma de passar todos os argumentos da classe pai sem precisar passar todos os argumentos de forma manual
  # para isso vc deve jogar o **kv dentro do init da classe e dentro do init do metodo super 
  # porem com isso vc deve passar a instancia do objeto de forma nomeada, dando o valor para cada argumento da classe
  
  def __init__(self, cor_pelo, **kv):
    self.cor_pelo = cor_pelo
    super().__init__(**kv)

class Ave(Animal):
  def __init__(self, cor_bico, **kv):
    self.cor_bico = cor_bico
    super().__init__(**kv)

class Cachorro(Mamifero):
  pass

class Gato(Mamifero):
  pass

class Leao(Mamifero):
  pass

class Ornitorrinco(Mamifero, Ave):
  pass

g = Gato(nro_patas=4, cor_pelo="Frajola")
print(g)

o = Ornitorrinco(nro_patas=2, cor_pelo="Vermelho", cor_bico="Laranja")
print(o)

# o metodo __mro_ mostra o caminho que a classe fez para pegar o metodo que esta sendo utilizado, dando os nomes das classes que ela verificou ate chegar no output
# é muito bom utilizar em um metodo de uma classe que herda de varias classes, pois isso faz com que seja facil de rastrear de onde a instancia da classe
# ta puxando o metodo