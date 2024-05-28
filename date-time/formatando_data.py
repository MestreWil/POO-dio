from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"
mascara_ptbr = "%d/%m/%Y %a"

print(data_hora_atual.strftime(mascara_ptbr))

# Com o datetime .strftime() e usando uma mascara com formato "%d/%m/%Y" vc consegue matipular o formato que sera exibido a data