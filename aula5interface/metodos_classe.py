class Pessoa:
  def __init__(self, nome=None, idade=None) -> None:
    self.nome = nome
    self.idade = idade
    
  #Metodo de classe é usado quando preciso de algo que se refere a classe  
  @classmethod 
  def criar_de_data_nascimento(cls, ano, mes, dia, nome):
    idade = 2022 - ano
    return cls(nome, idade)
  
  #Metodo estatico nao precisa de contexto e nem da instancia do objeto
  @staticmethod
  def e_maior_idade(idade):
    return idade >= 18
    
#p = Pessoa("Guilherme", 28)
#print(p.nome, p.idade)

p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(9))