from dataclasses import dataclass
from datetime import datetime
print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

print(datetime(2021,10,12))
data_postagem_foto = datetime.strptime(input('Quando devo postar a foto: '),'%d/%m/%Y')
print(type(data_postagem_foto))
print()


