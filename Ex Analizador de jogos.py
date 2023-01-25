print('ANALIZADOR DE PARTIDAS DO \033[32mCAMPEONATO \033[33mBRASILEIRO\033[m')
time1 = str(input('\nInforme o primeiro time: ')).title().strip()
time2 = str(input('Informe o segundo time: ')).title().strip()
gol_time1 = int(input(f'\nQuantos gols o {time1} fez? '))
gol_time2 = int(input(f'Quantos gols o {time2} fez? '))
diferenca = gol_time1 - gol_time2
print(21 * '-')
print(f'DIFERENÇA DE GOLS: {diferenca}')
if diferenca == 0:
    print('Empate!')
elif diferenca <= 3:
    print('Jogo Normal')
else:
    print('GOLEADA')
print(21 * '-')
