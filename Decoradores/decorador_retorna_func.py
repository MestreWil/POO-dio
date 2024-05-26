def meu_decorador(funcao):
  def envelope(*args, **kwargs):
    print('faz algo antes de executar')
    resultado = funcao(*args, *kwargs)
    print('faz algo depois de executar')
    return resultado
  return envelope

@meu_decorador
def ola_mundo(nome, outro_argumento):
  print(f'Olá, mundo {nome}!')
  return outro_argumento
  
resultado = ola_mundo("Mestre_will", 100)
print(resultado)
# as vezes com o decorador, queremos que a funcao execute um comportamento e retorne um valor 
# porem quem executa a funcao é o decorador, e ele sempre retornara None por padrao, 
# para muar isso, vc pode da um return no funcao a ser executada pelo decorador e salvar o 
# retorno da funcao em uma variavel tbm, e retornando essa variavel