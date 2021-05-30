from relogio import Relogio
from personagem import Personagem
from casa import Casa
import os
from playsound import playsound
from time import sleep

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
        '''for i in range(0,2):#for para executar o som duas vezes
            playsound('Projeto_final/alarme.mp3')#executa o som de dispertador '''
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
    atrasado = 'Você não esta atrado ainda!!!'
    if relogio.horas == 7 and relogio.minutos > 20:# verefica a hora que acordou e da uma mensagem 
        atrasado = 'Você esta atrado !!!'
    print(f'Você acordou as  {relogio} horas, {atrasado} ')#printa a hora e se esta atrasado ou não 
    print(f'{personagem}, Você precisa tomar banho ')#diz ao usuario o que ele precisa fazer 
    while True:#while criado para dar as opções do usuario 
        op = int(input('1-> Tomar banho \n'
                       '2-> Ver as noticias no celular \n'
                       '3-> Ver o mensagens do WhatsApp\n'
                       'Escolha :'))
        if op == 1 :
            personagem.tomar_banho()
            relogio.avancaTempo(20)#relogio avança 20 munutos 
            if relogio.horas == 7 and relogio.minutos >= 30:
                print('cuidado para não perder o ônibus das 08 horas !!!')
            print(f'{relogio} horas')
            break        
        elif op == 2:
            relogio.avancaTempo(5)#relogio oavança 5 minutos 
            if relogio.horas == 7 and relogio.minutos == 30:
                print('cuidado para não perder o ônibus das 08 horas !!!')
            print('Você ainda precisa tomar banho !!!')
            print(f'{relogio} horas')            
        elif op == 3:
            relogio.avancaTempo(10)#relogio avança 10 minutos 
            if relogio.horas == 7 and relogio.minutos >= 30:
                print('cuidado para não perder o ônibus das 08 horas !!!')
            print('Você ainda precisa tomar banho !!!')
            print(f'{relogio} horas')            
        else:
           print('Escolha invalida !!!')
    print(personagem)   
    while True:
        op = int(input('1-> Tomar café\n'
                       '2-> Ir rabalhar sem tomar café\n '
                       'Escolha :')) 
        if op == 1:
            valor = False
            personagem.comer()
            print('Você tomou café da manhã agora precisa ir trabalhar!!!')
            relogio.avancaTempo(10)
            break
        elif op == 2:
            print('Você não tomou café da manhã mesmo assim precisa ir trabalhar !!! ')
            break
        else:
            print('Escolha invalida !!!')
              
      
    if relogio.horas == 7 and relogio.minutos > 47:
        relogio.avancaTempo(15)
        print('Você leva 13 minutos para ir até o ponto para pegar o ônibus que sai as 08:00 horas ')
        print('Você acabou perdendo o ônibus para ir trabalhar !!! parabéns kkkk')
        while True:
            op = int(input('1-> Chamar um uber  R$80,00\n'
                       '2-> Chamar um Taxi R$150,00   \n'
                       '3-> Ir caminhando (desconto por cahegar atrasado!!)\n'
                       'Escolha :'))
            if op == 1:
                valor = 80
                minutos = 60 - relogio.minutos
                personagem.gasto(valor)
                relogio.avancaTempo(20 + minutos)
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
                relogio.avancaTempo(120)                
                print('Você não chegou no horario e vai perder o valor das horas de atraso e o sabados e domingos do mês R$250,00 Reais !!!!')
                break
            else:
                 print('Opção invlaida !!!')  
        print(personagem)           
    else:
        print('Você foi tranquilamente para o ponto de ônibus !!')
        print('Você pegou o ônibus para ir trabalhar !!')
        valor = 5
        minutos = 60 - relogio.minutos
        personagem.gasto(valor)
        relogio.avancaTempo(25 + minutos)
        print(personagem) 
    
    print(f'Chegou no trabalho as {relogio} horas, e começou suas atividades !!')
    horas = 240 - relogio.minutos 
    relogio.avancaTempo(horas)
    sleep(4)
    personagem.fome()
    print(f'{relogio} hora do almoço !!')
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
    print(personagem) 
            
    print(f'{relogio} horas terminou a hora do almoço !!\n iniciando o trabalho novamente !!')
    relogio.avancaTempo(240)
    print(f'{relogio} terminou seu dia de trablho !!! ')
    print('Seu curso começa as 19:00 horas !!!')
    while True:
        op = int(input('1-> Ir para casa\n'
                       '2-> Passar no mercado\n'
                       '3-> Ir ao shopping )\n'
                       '4-> Dar uma volta e comer churros\n '
                       'Escolha :'))
        if op == 1:
            while True:
                op = int(input('1-> Ir de ônibus R$5 mangos\n'
                       '2-> Passar no mercado\n'
                       '3-> Ir ao shopping )\n'
                       '4-> Dar uma volta e comer churros\n '
                       'Escolha :'))
                
    


