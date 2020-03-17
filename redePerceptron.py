class redePerceptron:
   def identificaEntrada(entradas):
        if(entradas == "AND"):
            entradaAnd = [      [0, 0, 0],
                                [0, 1, 0],
                                [1, 0, 0],
                                [1, 1, 1]]
            for l in range(0,len(entradaAnd)):
                print()
                for c in range(0,3):
                    print(f'[{entradaAnd[l][c]}]', end='')                    
            return entradaAnd                  
        elif(entradas == "OR"):
            entradaOr = [       [0, 0, 0],
                                [0, 1, 1],
                                [1, 0, 1],
                                [1, 1, 1]]
            return entradaOr
   def pegarOsPesos(pesoA, pesoB):
        pesoA = pesoA
        pesoB = pesoB

        return 'Pesos Iniciais: \n Peso A: ' + pesoA + '\n Peso B: ' + pesoB
        