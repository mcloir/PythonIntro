# 1. Prompt the user for input and store it as a string
idade_str = input("Digite sua idade: ")

# 2. Check if the string consists only of digits to prevent errors during conversion
if idade_str.isdigit():
    
    # 3. Convert the string to an integer
    idade = int(idade_str)
    
    # 4. Validate the input against a logical, real-world range
    if 0 <= idade <= 150:
        # 5. Output the result if the validation passes (the "Happy Path")
        print(f"Você tem {idade} anos")
    else:
        # 6. Handle the case where the number is technically valid, but logically incorrect
        print("Idade fora do intervalo válido (0-150)")

else:
    # 7. Handle the case where the user input contains non-numeric characters
    print("Entrada inválida. Digite um número.")