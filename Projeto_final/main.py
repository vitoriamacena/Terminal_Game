from warnings import simplefilter
from relogio import Relogio
from personagem import Personagem
from casa import Casa
import os
from playsound import playsound
from time import sleep
from tqdm import tqdm
from prova import Prova

os.system("cls")
if(__name__ == "__main__"): 
    relogio = Relogio()#estancia a classe relogio
    personagem = Personagem()#estancia a calsse personagem 
    casa = Casa()# estabcia a classe casa 
    print(f'Vamos começar seu dia são exatamente {relogio} dispertador vai tocar as 7:00 horas')#aviso da hora e que logo vai dispertar o relogio
    sleep(3)   # gera um time de 3 segundos 
    relogio.avancaTempo(1)#avança um minuto no tempo para dispertar o relogio 
    print('7:00 horas, Hora de acordar !!!!')
    sleep(2)#espera 2 segundos para começar a dispertar 
    #faz um loop para simular um dispertador com o modo soneca
    while personagem.acordar == False:
        #for i in range(0,2):#for para executar o som duas vezes
        #    playsound('Projeto_final/alarme.mp3')#executa o som de dispertador 
        op = int(input('1-> Parar dispertador\n'#da a opção de escolha entre para e modo soneca 
                       '2-> Modo soneca\n'
                       'Escolha:'))                    
        if op == 1:#verefica qual foi a escolha 
            personagem.acordar2()
            break
        elif op == 2:   
            for i in range(0,10): #for criado para passar mais 10 minutos no tempo minuto a minuto
                relogio.avancaTempo(1)#avança o relogio em um minuto 
                print('Modo soneca !!')
                print(relogio)#printa a hora atual 
                sleep(1)#espera um segundo 
                os.system("cls")# limpa a tela 
            print(f'{relogio} horas, Hora de acordar !!!!')# diz que esta na hora de acordar e innicia o dispertador de novo 
        else:
            print('Escolha invalida !!!')
    os.system("cls")
    atrasado = 'Você não esta atrado ainda!!!'
    if relogio.horas == 7 and relogio.minutos > 20:# verefica a hora que acordou e da uma mensagem 
        atrasado = 'Você esta atrado !!!'
    print(f'Você acordou as  {relogio} horas, {atrasado} ')#printa a hora e se esta atrasado ou não 
    print(f'{personagem}, Você precisa tomar banho ')#diz ao usuario o que ele precisa fazer 
    os.system("cls")
    while True:#while criado para dar as opções do usuario 
        op = int(input('1-> Tomar banho \n'
                       '2-> Ver as noticias no celular \n'
                       '3-> Ver o mensagens do WhatsApp\n'
                       'Escolha :'))
        if op == 1 :
            personagem.tomar_banho()#chama a função tomar banho que deixa o sujo como False
            relogio.avancaTempo(20)#relogio avança 20 munutos 
            if relogio.horas == 7 and relogio.minutos >= 30:#condicional que verefica se já é 07:30 ou mais para avisar sobre a hora do ônibus
                print('cuidado para não perder o ônibus das 08 horas !!!')
            print(f'{relogio} horas')#imprime a hora 
            break        
        elif op == 2:
            relogio.avancaTempo(5)#relogio oavança 5 minutos 
            if relogio.horas == 7 and relogio.minutos == 30:#condicional que verefica se já é 07:30 ou mais para avisar sobre a hora do ônibus
                print('cuidado para não perder o ônibus das 08 horas !!!')
            print('Você ainda precisa tomar banho !!!')
            print(f'{relogio} horas')            
        elif op == 3:
            relogio.avancaTempo(10)#relogio avança 10 minutos 
            if relogio.horas == 7 and relogio.minutos >= 30:#condicional que verefica se já é 07:30 ou mais para avisar sobre a hora do ônibus
                print('cuidado para não perder o ônibus das 08 horas !!!')
            print('Você ainda precisa tomar banho !!!')
            print(f'{relogio} horas')            
        else:
           print('Escolha invalida !!!')
    print(personagem)  
    os.system("cls") 
    while True:#laço de repetição para dar a escolha entre opções obrigando a escolher uma das duas
        op = int(input('1-> Tomar café\n'
                       '2-> Ir rabalhar sem tomar café\n '
                       'Escolha :')) 
        if op == 1:
            valor = False#valor recebe o valor logico False
            personagem.comer()#chama o métedo comer da classe personagem
            print('Toamndo café da manhã tranquilamente!!!\n')
            for i in tqdm(range(10)):
                sleep(1)
            sleep(3)
            print('Você tomou café da manhã agora precisa ir trabalhar!!!\n')
            relogio.avancaTempo(10)#chama o método avancatempo da classe relogio e avança 10 minutos 
            break
        elif op == 2:
            print('Você não tomou café da manhã mesmo assim precisa ir trabalhar !!! ')
            break
        else:
            print('Escolha invalida !!!')  
    sleep(5)
    os.system("cls")
    if relogio.horas == 7 and relogio.minutos > 47:#condicional que verefica se a hora é maior que 07:47 que se for não da mais tempo de ir ao ponto pegar o ônibus
        relogio.avancaTempo(15)#chama o metodo da classe relogio e avança 15 minutos no tempo
        print('\nVocê leva 13 minutos para ir até o ponto para pegar o ônibus que sai as 08:00 horas\n ')
        sleep(2)
        print('Você acabou perdendo o ônibus para ir trabalhar !!! parabéns kkkk')
        os.system("cls")
        while True:
            op = int(input('1-> Chamar um uber  R$80,00\n'
                       '2-> Chamar um Taxi R$150,00   \n'
                       '3-> Ir caminhando (desconto por cahegar atrasado!!)\n'
                       'Escolha :'))
            if op == 1:
                valor = 80
                minutos = 60 - relogio.minutos #calcula quantos minutos faltavam pra dar 8 horas quando voce sai de casa
                personagem.gasto(valor) #chama o método gasto para descontar o valor em conta o valor do uber
                relogio.avancaTempo(20 + minutos) #chama o metodo da classe relógio e passa como parametro o tempo que leva ara chegar no trabalho e soma com os minutos  
                print('Você chegou no horario ainda.... ufa!!!')
                break
            elif op == 2:
                valor = 150
                minutos = 60 - relogio.minutos
                relogio.avancaTempo(25 + minutos)
                personagem.gasto(valor)
                print('Você chegou no horario ainda.... ufa!!!')
                break
            elif op == 3:
                #relogio.avancaTempo(120)                
                print('Você não chegou no horario e vai perder o valor das horas de atraso e o sabados e domingos do mês R$250,00 Reais, que vai ser decontado no próximo pagamento!!')
                break
            else:
                 print('Opção invlaida !!!')  
        print(personagem)           
    else:
        print('Você foi tranquilamente para o ponto de ônibus !!\n')
        sleep(3)
        print('Você pegou o ônibus para ir trabalhar !!\n')
        sleep(3)
        valor = 5
        minutos = 60 - relogio.minutos
        personagem.gasto(valor)
        relogio.avancaTempo(25 + minutos)
        print(personagem) 
    print(f'Chegou no trabalho as {relogio} horas, e começou suas atividades !!\n')
    sleep(5)
    horas = 240 - relogio.minutos #calcula quantos minutos vc chegou atrasdo ou adiantado para que a hora do almoço seja ao meio dia 
    relogio.avancaTempo(horas)
    print('Realizando suas atividades do trabalho !!\n')
    for i in tqdm(range(10)):
        sleep(1)
        for i in tqdm(range(10)):
            sleep(1)
    print()
    sleep(5)
    os.system("cls")
    personagem.fome()
    print(f'{relogio} horas do almoço !!')
    print(personagem)     
    while True:
        op = int(input('1-> Almoçar restaurante prato do dia lasgosta R$222,55\n'
                       '2-> Almoçar restaurante popular buffet livre R$25,90   \n'
                       '3-> Almoçar na lanchonete X-salada R$15,90 )\n'
                       '4-> Almoçar uma coxinha R$5 mangos \n'
                       'Escolha :'))
        if op == 1:
            valor = 222.55
            relogio.avancaTempo(60)
            personagem.gasto(valor)
            personagem.comer()
            break
        elif op == 2:
            valor = 25.90
            relogio.avancaTempo(60)
            personagem.gasto(valor)
            personagem.comer()
            break
        elif op == 3:
            valor = 15.90
            relogio.avancaTempo(60)
            personagem.gasto(valor)
            personagem.comer()
            break
        elif op == 4:
            valor = 5
            relogio.avancaTempo(60)
            personagem.gasto(valor)
            personagem.comer()
            break    
        else:
            print('Opção invlaida !!! ')
    os.system("cls")
    print(personagem)             
    print(f'{relogio} horas terminou a hora do almoço !!\n iniciando o trabalho novamente !!')
    relogio.avancaTempo(240)
    print(f'{relogio} terminou seu dia de trabalho !!! ') 
    sleep(5)   
    personagem.fome()
    print(f'{personagem}')    
    print('Seu curso começa as 19:00 horas !!!')
    os.system("cls")
    while True:
        op = int(input('1-> Ir de ônibus\n'
                       '2-> Passar no mercado\n'
                       '3-> Ir ao shopping \n'
                       '4-> Dar uma volta e comer churros\n '
                       'Escolha :'))  
        if op == 1:
            relogio.avancaTempo(70)
            personagem.comer()
            personagem.gasto(9)
            print('Você tomou café em casa !!!')            
            break        
        elif op == 2:
            while True:
                op = int(input('1-> Comprar um pacote de Fandangos R$ 7,89 - 800Kg\n'
                               '2-> Comprar um Doritos R$ 14,95 - 800Kg\n'
                               '3-> Comprar um quilo de Banana R$ 2,99 - 1Kg\n'
                               'Escolha:'))
                if op == 1:
                    relogio.avancaTempo(70)
                    personagem.comer()
                    personagem.gasto(7.89)
                    op = input('Pegar uma lata de refrigerante R$ 4,99 - 350  (Sim/Não)').strip().upper()[0]
                    if op == 'S':
                        personagem.gasto(4.99)
                    break                    
                elif op == 2:
                    relogio.avancaTempo(40)
                    personagem.comer()
                    personagem.gasto(14.95)
                    op = input('Pegar uma lata de refrigerante R$ 4,99 - 350  (Sim/Não)').strip().upper()[0]
                    if op == 'S':
                        personagem.gasto(4.99)
                    break
                elif op == 3:
                    relogio.avancaTempo(70)
                    personagem.comer()
                    personagem.gasto(2.99)
                    op = input('Pegar uma lata de refrigerante R$ 4,99 - 350  (Sim/Não)').strip().upper()[0]
                    if op == 'S':
                        personagem.gasto(4.99)
                    break
                else:
                    print('Opção invlaida !!!')
            break                        
        elif op == 3:
            while True:
                op = int(input('1-> Comprar um Mclanche feliz R$19,90 com refri gratis\n'
                               '2-> Comprar um Mega Stacker 4.0 no burger king por R$ 24,50 com refri gratis\n'
                               '3-> Comprar um Pasteu da tenda do tio por 5 mangos (mais é um big pasteu)\n'
                               'Escolha:'))
                if op == 1:
                    relogio.avancaTempo(70)
                    personagem.comer()
                    personagem.gasto(19.90)
                    break
                elif op == 2:
                    relogio.avancaTempo(70)
                    personagem.comer()
                    personagem.gasto(24.50)
                    break
                elif op == 3:
                    relogio.avancaTempo(70)
                    personagem.comer()
                    personagem.gasto(5)
                    break
                else:
                    print('Opção invalida !!!')
            break
        elif op == 4:
            relogio.avancaTempo(70)
            personagem.comer()
            personagem.gasto(5)
            break
        else:
            print('Opção invalida !!!')
    print('Comendo tranquilamente !!!')
    for i in tqdm(range(10)):
        sleep(1)
    os.system("cls")
    while True:
        op = int(input('1->  Ir de ônibus\n'
                       '2->  Chamar um uber  R$80,00  \n'
                       '3->  Chamar um Taxi R$150,00\n'
                       '4->  Ir caminhando '
                       'Escolha :'))
        if op == 1:
            valor = 5            
            relogio.avancaTempo(50)
            personagem.gasto(valor) 
            print('Você chegou 10 minutos adiantados ')           
            break
        elif op == 2:
            valor = 40            
            personagem.gasto(valor) #chama o método gasto para descontar o valor em conta o valor do uber
            relogio.avancaTempo(50) #chama o metodo da classe relógio e passa como parametro o tempo que leva ara chegar no trabalho e soma com os minutos  
            print('Você chegou 10 minutos adiantados ')   
            break   
        elif op == 3:
            valor = 80            
            relogio.avancaTempo(50)
            personagem.gasto(valor) 
            print('Você chegou 10 minutos adiantados ')           
            break
        elif op == 4: 
            #relogio.avancaTempo(120)  
            relogio.avancaTempo(50)              
            print('Ainda bem que é perto e você chegou em cima da hora !!!')
            break
        else:
            print('Opção invlaida !!!') 
    sleep(5) 
    print('Você chegou no curso e terá uma teste avaliativo !!')
    relogio.avancaTempo(10)
    print(relogio)
    print('Iniciando o teste avaliativo !!') 
    sleep(3)
    prova = Prova()
    relogio.avancaTempo(150)
    os.system("cls")
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
    sleep(5) 
    os.system("cls")
    print(f'Você tirou {prova}') 
    print('Continuando a aula !!!')  
    for i in tqdm(range(10)):
        sleep(1) 
    os.system("cls")
    print('Hora de ir para casa !!! a aula acabou ')
    sleep(5)    
    while True:
        op = int(input('1->  Ir de ônibus\n'
                        '2->  Chamar um uber  R$80,00  \n'
                        '3->  Chamar um Taxi R$150,00\n'
                        '4->  Ir caminhando '
                        'Escolha :'))
        if op == 1:
            valor = 5            
            relogio.avancaTempo(20)
            personagem.gasto(valor)                        
            break
        elif op == 2:
            valor = 40            
            personagem.gasto(valor) #chama o método gasto para descontar o valor em conta o valor do uber
            relogio.avancaTempo(20) #chama o metodo da classe relógio e passa como parametro o tempo que leva ara chegar no trabalho e soma com os minutos                
            break   
        elif op == 3:
            valor = 80            
            relogio.avancaTempo(20)
            personagem.gasto(valor)                       
            break
        elif op == 4: 
            #relogio.avancaTempo(120)  
            relogio.avancaTempo(20) 
            break
        else:
            print('Opção invlaida !!!')   
    os.system("cls")           
    print(f'Você chegou em casa as {relogio} hora de dormir')
    print('Final do seu dia !!!')    
          
        