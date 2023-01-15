class Calc:

    # construtor
    def __init__(self, a, b):

        self.a=a
        self.b=b

    # metodo (é uma função dentro da classe)
    def soma(self):
        return self.a+self.b

    def soma_tres_numeros(self,c):
        return self.a+self.b + c
    
    def __repr__(self):
        return str(self.soma())

# instanciar um objeto em tempo de execução
calculadora=Calc(a=1,b=2) # Calc é uma classe que contém o método soma

calculadora.soma()

resultdois = calculadora.soma_tres_numeros(4)

# função em tempo de execução (não é um método)
print(calculadora)
# print(resultdois)

