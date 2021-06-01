class Prova:
    
    def __init__(self):
        self.__questao1 = 'A'
        self.__questao2 = 'A'
        self.__nota = 0 
    
    
    
    def __str__(self):
        return str(float(self.__nota))
     
    def CorrigeProva(self,resposta1 = ' ',resposta2 = ' '):        
        self.__nota = 0
        if self.__questao1 == resposta1:
            self.__nota += 5
        else:
            self.__nota += 0         
        if self.__questao2 == resposta2:
            self.__nota += 5 
        else:
            self.__nota += 0
            
        
        