#decoradores genericos utilizam args e kwargs

def meu_decorador(funcao):
  def envelope(*args, **kwargs):
    print('faz algo antes de executar')
    funcao(*args, *kwargs)
    print('faz algo depois de executar')
  return envelope

@meu_decorador
def ola_mundo(nome):
  print(f'Olá, mundo {nome}!')
  
ola_mundo("Mestre_will")