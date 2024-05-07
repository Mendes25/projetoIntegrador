# converta número da base decimal para hexadecimal 
# converta número da base hexadecimal para decimal

def decimal_para_hexadecimal(numero_decimal):
    # Função para converter decimal para hexadecimal
    hexadecimal = ""
    hex_digitos = "0123456789ABCDEF"

    while numero_decimal > 0:
        resto = numero_decimal % 16
        hexadecimal = hex_digitos[resto] + hexadecimal
        numero_decimal //= 16

    return hexadecimal

def hexadecimal_para_decimal(numero_hexadecimal):
    # Função para converter hexadecimal para decimal
    decimal = 0
    for digito in numero_hexadecimal:
        if digito.isdigit():
            valor = int(digito)
        else:
            valor = ord(digito.upper()) - ord('A') + 10
        decimal = decimal * 16 + valor
    return decimal

def main():
    # Função principal 
    while True:
        print("Escolha uma opção:")
        print("1. Converter decimal para hexadecimal")
        print("2. Converter hexadecimal para decimal")
        print("3. Sair")
        
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == "1":
            numero_decimal = int(input("Digite o número decimal: "))
            print("Hexadecimal:", decimal_para_hexadecimal(numero_decimal))
        elif opcao == "2":
            numero_hexadecimal = input("Digite o número hexadecimal: ")
            print("Decimal:", hexadecimal_para_decimal(numero_hexadecimal))
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chamar a função principal
main()





    




















