import functools

def meu_decorador(funcao):
  @functools.wraps(funcao)
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
print(ola_mundo.__name__)

# O functools mantem o nome da funcao para que vc não perca a capacidade de introspeccao, usando o @functools.wraps(argumento) e passando uma argumento