class Cachorro:
  def __init__(self, nome, cor, acordado=True):
    self.nome = nome
    self.cor = cor
    self.acordado = acordado
    
  def __del__(self):
    #Executado quando o objeto é destruido
    print("Removendo a instância da classe.")
    
  def falar(self):
    print("auau")
    
c = Cachorro("Chappie", "amarelo")
c.falar()
    