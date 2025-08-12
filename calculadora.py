import sys
while True:
 print("---Calculadora---")

 n1 = int(input("\nEscolha o primeiro número: "))
 n2 = int(input("Escolha o segundo número: "))
 
 print("\nOperações---")
 print("Soma: +")
 print("Subtração: -")
 print("Multiplicação: *")
 print("Divisão: /")
 
 operacao = str(input("Escolha: "))
 
 if (operacao == "+"):
     print("\nResultado:", n1 + n2)
 elif (operacao == "-"):
     print("\nResultado:", n1 - n2)
 elif (operacao == "*"):
     print("\nResultado:", n1 * n2)
 elif (operacao == "/"):
     print("\nResultado:", n1 / n2)
 else:
     print("\nERRO!")
     sys.exit()

 print("\n")
     

