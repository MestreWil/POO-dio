#uma variavel de classe fica fora do construtor, ja uma variavel de instancia fica dentro do metodo construtor

class Estudante:
  escola = "DIO"
  
  def __init__(self, nome, matricula):
    self.nome = nome
    self.matricula = matricula
    
  def __str__(self):
    return f"{self.nome} - {self.matricula} - {self.escola}"
  
def mostrar_valores(*objs):
  for obj in objs:
    print(obj)
    
aluno_1 = Estudante("William", 1)
aluno_2 = Estudante("Giovanna", 2)

mostrar_valores(aluno_1, aluno_2)

aluno_1.matricula = 3

mostrar_valores(aluno_1, aluno_2)
Estudante.escola = "Senac"
mostrar_valores(aluno_1, aluno_2)

#perceba que num exemplo eu altero apenas uma instancia de codigo, o que nao altera a outra instancia, 
# ja quando eu mexo na variavel escola eu altero a variavel para ambas as instancias