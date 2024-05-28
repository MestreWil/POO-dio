from datetime import datetime, timedelta

tipo_carro = 'M' # P, M, G

tempo_pequeno = 130
tempo_medio = 2145
tempo_grande = 60

data_atual = datetime.now()

if tipo_carro == "P":
  data_estimada = data_atual - timedelta(days=tempo_pequeno)
  print(f"O carro chegou: {data_atual} e ficará pronto ás {data_estimada}")
elif tipo_carro == "M":
  data_estimada = data_atual - timedelta(days=tempo_medio)
  print(f"O carro chegou: {data_atual} e ficará pronto ás {data_estimada}")
else: 
  data_estimada = data_atual - timedelta(days=tempo_grande)
  print(f"O carro chegou: {data_atual} e ficará pronto ás {data_estimada}")