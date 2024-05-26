def pai():
  print("Escrevendo da pai() funcao")
  def filho1():
    print("Escrevendo da filho1() funcao")
    
  def filho2():
    print("Escrevendo da filho2() funcao")
    
  filho1()
  filho2()
  
pai()

#é possivel escrever funcoes dentro de uma funcao, e isso nos chamamos de inner functions