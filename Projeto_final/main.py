from relogio import Relogio
from personagem import Personagem
from casa import Casa
import os
from playsound import playsound
from time import sleep

os.system("cls")
if(__name__ == "__main__"): 
    relogio = Relogio()
    personagem = Personagem()
    casa = Casa()
    print(f'Vamos começar seu dia são exatamente {relogio} dispertador vai tocar as 7:00 horas')
    sleep(3)    
    relogio.avancaTempo(1)
    print('7:00 horas, Hora de acordar !!!!')
    sleep(2)
    while personagem.acordar == False:
        for i in range(0,2):
            playsound('Projeto_final/alarme.mp3')
            pass
        op = int(input('1-> Parar dispertador\n'
                       '2-> Modo soneca\n'
                       'Escolha:'))                    
        if op == 1:
            personagem.acordar2()
            break
        elif op == 2:   
            for i in range(0,10): 
                relogio.avancaTempo(1)
                print('Modo soneca !!')
                print(relogio)
                sleep(1)
                os.system("cls")
            print(f'{relogio} horas, Hora de acordar !!!!')
        else:
            continue
    atrasado = 'Você não esta atrado ainda!!!'
    if relogio.horas == 6 and relogio.minutos > 20:
        atrasado = 'Você esta atrado !!!'
    print(f'Você acordou as  {relogio} horas, {atrasado} ')
    print(f'{personagem}, Você precisa tomar banho ')
    while True:
        op = int(input('1-> Tomar banho \n'
                       '2-> Ver as noticias no celular \n'
                       '3-> Ver o mensagens do WhatsApp\n'
                       'Escolha :'))
        if op == 1 :
            relogio.avancaTempo(20)
            if relogio.horas == 6 and relogio.minutos >= 30:
                print('cuidado para não perder o ônibus das 07 horas !!!')
            print(f'{relogio} horas')
            break        
        elif op == 2:
            relogio.avancaTempo(5)
            if relogio.horas == 6 and relogio.minutos == 30:
                print('cuidado para não perder o ônibus das 07 horas !!!')
            print('Você ainda precisa tomar banho !!!')
            print(f'{relogio} horas')            
        elif op == 3:
            relogio.avancaTempo(10)
            if relogio.horas == 6 and relogio.minutos == 30:
                print('cuidado para não perder o ônibus das 07 horas !!!')
            print('Você ainda precisa tomar banho !!!')
            print(f'{relogio} horas')            
        else:
            continue
    
            
            

        
    


