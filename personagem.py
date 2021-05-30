class Personagem():
    def __init__(self):
        self.__nome = None
        self.__fome = True
        self.__sujo = True
        self.__dinheiro = 500
        self.__acordar = False
    
    def __str__(self):
         return "Você está " + ("sujo" if self.__sujo else "limpo")+", "+("com" if self.__fome else "sem")+" fome. Você tem R$"+str(self.__dinheiro)+" reais na sua conta."
    
    @property
    def nome(self):
        return self.__nome    
  
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def acordar(self):
        return self.__acordar
        
    def tomar_banho(self):
        self.__sujo = False
    
    def comer(self):
        self.__fome = False
    
    def acordar2(self):
        self.__acordar = True
    
    def jogar(self):
        self.jogar = True
     
     
    @property   
    def dinheiro(self):
        return self.__dinheiro()
    
    @dinheiro.setter
    def dinheiro(self,valor):
        self.__dinheiro = valor
        
    
        
    
    