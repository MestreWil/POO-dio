from abc import ABC, abstractmethod

#toda classe que imprementa uma classe abstrata elas obrigatoriamente terao que implementar os metodos abstratos da classe abstrata
#Classe abstrata é um contrato que faz com que as classes que implementao essa classe abstrata precisem ter aqueles metodos

class ControleRemoto(ABC):
  
  @abstractmethod
  def ligar(self):
    pass
  
  @abstractmethod
  def desligar(self):
    pass
  
  @property
  @abstractmethod
  def marca(self):
    pass
  
class ControleTV(ControleRemoto):
  def ligar(self):
    print("Ligando a Tv")
    
  def desligar(self):
    print("Desligando Tv")
  
  @property  
  def marca(self):
    return "LG"
  
class ArCondicionado(ControleTV):
  def ligar(self):
    print("Ligando a Ar condicionado")
    
  def desligar(self):
    print("Desligando Arcondicionado")
  
  @property  
  def marca(self):
    return "Samgsung"
    
controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)
ar = ArCondicionado()
ar.ligar()
ar.desligar()
print(ar.marca)