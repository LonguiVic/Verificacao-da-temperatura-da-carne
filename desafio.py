'''
Criar um programa que dependendo da temperatura (em Celsius) 
do steak ele retorna o ponto de cozimento em português. O usuário deverá fornecer a temperatura.

Temperaturas - Cozimento:
120ºF ou 48ºC - Rare (Selada)
130ºF ou 54ºC - Medium rare (Ao ponto para o mal)
140ºF OU 60ºC - Medium (Ao ponto)
150ºF ou 65ºC - Medium well (Ao ponto para o bem)
160ºF ou 71ºC - Well done (Bem passada)
'''

temperatura = int(input('Qual é a temperatura da carne? (Em ºC) '))

if temperatura <= 47:
    print('Calma aí! Cozinhe a carne por mais tempo')
elif temperatura >= 48 and temperatura < 54:
    print('Rare (Selada)')
elif temperatura >= 54 and temperatura < 60:
    print('Medium rare (Ao ponto para o mal)')
elif temperatura >= 60 and temperatura < 65:
    print('Medium (Ao ponto)')
elif temperatura >= 65 and temperatura < 71:
    print('Medium well (Ao ponto para o bem)')
elif temperatura == 71:
    print('Well done (Bem passada)')
else:
    print('Essa não!!! A carne queimou!')