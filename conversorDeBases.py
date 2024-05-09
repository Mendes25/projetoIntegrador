# converta número da base decimal para hexadecimal 
# converta número da base hexadecimal para decimal

def decimalParaHexadecimal(numeroDecimal):
    # Função para converter decimal para hexadecimal
    hexadecimal = ""
    hexDigitos = "0123456789ABCDEF"

    while numeroDecimal > 0:
        resto = numeroDecimal % 16
        hexadecimal = hexDigitos[resto] + hexadecimal
        numeroDecimal //= 16

    return hexadecimal

def hexadecimalParaDecimal(numeroHexadecimal):
    # Função para converter hexadecimal para decimal
    decimal = 0
    for digito in numeroHexadecimal:
        if digito.isdigit():
            valor = int(digito)
        else:
            valor = ord(digito.upper()) - ord('A') + 10
        decimal = decimal * 16 + valor
    return decimal

def decimalParaOctal(numeroDecimal):
    # Função para converter decimal para octal
    octal = ""
    while numeroDecimal > 0:
        resto = numeroDecimal % 8
        octal = str(resto) + octal
        numeroDecimal //= 8
    return octal

def octalParaDecimal(numeroOctal):
    # Função para converter octal para decimal
    decimal = 0
    for digito in numeroOctal:
        decimal = decimal * 8 + int(digito)
    return decimal

def decimalParaBinario(numeroDecimal):
    # Função para converter decimal para binário
    binario = ""
    while numeroDecimal > 0:
        resto = numeroDecimal % 2
        binario = str(resto) + binario
        numeroDecimal //= 2
    return binario

def binarioParaDecimal(numeroBinario):
    # Função para converter binário para decimal
    decimal = 0
    for digito in numeroBinario:
        decimal = decimal * 2 + int(digito)
    return decimal

def main():
    # Função principal 
    while True:
        print("Escolha uma opção:")
        print("1. Converter decimal para hexadecimal")
        print("2. Converter decimal para octal")
        print("3. Converter decimal para binário")
        print("4. Converter hexadecimal para decimal")
        print("5. Converter octal para decimal")
        print("6. Converter binário para decimal")
        print("7. Sair")
        
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == "1":
            numeroDecimal = int(input("Digite o número decimal: "))
            print("Hexadecimal:", decimalParaHexadecimal(numeroDecimal))
        elif opcao == "2":
            numeroDecimal = int(input("Digite o número decimal: "))
            print("Octal:", decimalParaOctal(numeroDecimal))
        elif opcao == "3":
            numeroDecimal = int(input("Digite o número decimal: "))
            print("Binário:", decimalParaBinario(numeroDecimal))
        elif opcao == "4":
            numeroHexadecimal = input("Digite o número hexadecimal: ")
            print("Decimal:", hexadecimalParaDecimal(numeroHexadecimal))
        elif opcao == "5":
            numeroOctal = input("Digite o número octal: ")
            print("Decimal:", octalParaDecimal(numeroOctal))
        elif opcao == "6":
            numeroBinario = input("Digite o número binário: ")
            print("Decimal:", binarioParaDecimal(numeroBinario))
        elif opcao == "7":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chamar a função principal
main()





    




















