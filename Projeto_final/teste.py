from prova import Prova

prova = Prova()
while True:
    op = int(input('1-> Pedir cola ao seu amigo \n'
                    '2-> Fazer a prova sem colar\n '
                    'Escolha :'))
    if op == 1:
        print('Você tentou colar na prova e o foi pego pelo prefessor, sua prova foi zerada e recebeu uma bela adivertencia !!!')
        break
    elif op == 2:
        resposta = 'A'
        resposta2 = 'A'
        op1 = int(input('Qual dos nomes de variáveis abaixo não é um nome válido de variável em Python?\n'
                            '1-> Global\n'
                            '2-> a12b\n'
                            '3-> x_3\n'
                            '4-> _x\n'
                            '5-> A\n'
                            'Escolha:'))
        
        op2 = int(input('O que é um IDE?\n'
                            '1-> Um ambiente de desenvolvimento integrado\n'
                            '2-> Um plugin para Python\n'
                            '3-> Uma biblioteca de programação\n'
                            '4-> Uma plataforma de execução de programas.\n'
                            '5-> Um ambiente de depuração integrado.\n'
                            'Escolha:'))
        prova.CorrigeProva(resposta,resposta2)
        break

print(f'Você tirou {prova}')    
        