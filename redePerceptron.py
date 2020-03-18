from math import ceil
class redePerceptron:

    
    pesoA = 0
    pesoB = 0

    def __init__(self):
        
        self.pesoA = 0
        self.pesoB = 0

    def pegarOsPesos(self,pesoA, pesoB):
        
        self.pesoA = pesoA
        self.pesoB = pesoB

        return 'Pesos Iniciais: \n Peso A: ' + self.pesoA + '\n Peso B: ' + self.pesoB

    def calculoSomaPonderada(self,entrada,pesoA,pesoB):
        self.soma = [0,0,0,0]
        self.pesoA = int(pesoA)
        self.pesoB = int(pesoB)
        self.colunas = ceil(len(entrada)/2)
        self.xDaSoma = 0

       
        for l in range(0,len(entrada)):
            for c in range(0,1):
                    self.soma[l] = (entrada[l][c] * self.pesoA) + (entrada[l][c+1] * self.pesoB)
     
        return self.soma
    
    def identificaEntrada(self,entradas):
       
        if(entradas == "AND"):
            entradaAnd = [      [0, 0, 0],
                                [0, 1, 0],
                                [1, 0, 0],
                                [1, 1, 1]]
            resultadoSomaPonderada = redePerceptron.calculoSomaPonderada(self,entradaAnd,self.pesoA,self.pesoB)                            
            for l in range(0,len(entradaAnd)):
                print()
                for c in range(0,3):
                    print(f'[{entradaAnd[l][c]}]', end='')                    
            return str(entradaAnd) + '\n' + 'SOMA: ' + str(resultadoSomaPonderada)                 
        elif(entradas == "OR"):
            entradaOr = [       [0, 0, 0],
                                [0, 1, 1],
                                [1, 0, 1],
                                [1, 1, 1]]
            return entradaOr

    
        