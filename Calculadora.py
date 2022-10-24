class Calculadora:
    def __init__(self, num1, num2, operacao):
        self.num1 = num1
        self.num2 = num2
        self.op = operacao
        
    def soma(self):
        soma = float(self.num1)+float(self.num2)
        return soma
        
    def subtracao(self):
        subtracao = float(self.num1)-float(self.num2)
        return subtracao
        
    def multiplicacao(self):
        multiplicacao = float(self.num1)*float(self.num2)
        return multiplicacao
        
    def divisao(self):
        divisao = float(self.num1)/float(self.num2)
        return divisao
        
print("Calculadora feita por Marcos Vinicius")

num1 = ''
num2 = ''
operacao = ''

while True:
    if num1 == '':
        while True:
            num1i = input("Digite o primeiro número: ")
            if not num1i.isnumeric():
                print("Você precisa digitar um número")
                
            
            else:
                num1 = num1i
                break
    
    if operacao == '':   
        while True:
            operacaoi = input("Digite a operação: ")
            if operacaoi not in ('+', '-', '*', '/'):
                print("Operação inválida")
                
            else:
                operacao = operacaoi
                break
    
    if num2 == '':   
        while True:
            num2i = input("Digite o segundo número: ")
            if not num2i.isnumeric():
                print("Você precisa digitar um número")
                
            else:
                if operacao == '/' and num2i == int(0):
                    print("Divisor não pode ser zero")
                    
                else:
                    num2 = num2i
                    break
    
    break
                
print("Calculando o resultado de", num1, operacao, num2)

if operacao == '+':
    print("O resultado é", Calculadora(num1, num2, operacao).soma())
    
elif operacao == '-':
    print("O resultado é", Calculadora(num1, num2, operacao).subtracao())
    
elif operacao == '*':
    print("O resultado é", Calculadora(num1, num2, operacao).multiplicacao())
    
else:
    print("O resultado é", Calculadora(num1, num2, operacao).divisao())