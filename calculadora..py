
print("ESTUDO DE TRATAMENTO DE ERROS COM TRY E EXCEPT".center(50))
print("--"*30)

print("Operadores aritméticos".center(50))

try:
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))
    operacao = input(
            "Escolha uma operação (+,-,*,/): "
                    
            )
    if operacao == "+":
        resultado = n1 + n2
    elif operacao == "-":
        resultado = n1 - n2
    elif operacao == "*":
        resultado = n1 * n2
    elif operacao == "/":
        if n2 !=0:
            resultado = n1 / n2
        else:
            print('Erro: não é possível dividir por zero.')
            resultado = None

    else:
        print("Operação inválida!")
        resultado = None
    if resultado is not None:
        print(f"Resultado: {resultado}")
    
except ValueError:
    print("Erro: digite um número válido.")
    

except TypeError:
    print("Erro: tipo de dado incompatível")
    