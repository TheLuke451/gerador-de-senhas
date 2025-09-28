# Bibliotecas
import secrets


# Perguntas ao usuário
tamanho_senha = input(int("Digite o tamanho da senha: "))
caracteres_especiais = input("Incluir caracteres especiais? (s/n): ")
numeros = input("Incluir números? (s/n): ")
maiusculas = input("Incluir letras maiúsculas? (s/n): ")
minusculas = input("Incluir letras minúsculas? (s/n): ")

# Geração da senha
caracteres = ""

if caracteres_especiais == 's' or caracteres_especiais == 'S':
    caracteres += "!@#$%^&*()-_=+[]{}|;:,.<>?/"
if numeros == 's' or numeros == 'S':
    caracteres += "0123456789"
if maiusculas == 's' or maiusculas == 'S':
    caracteres += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if minusculas == 's' or minusculas == 'S':
    caracteres += "abcdefghijklmnopqrstuvwxyz"

senha = "".join(secrets.choice(caracteres) for i in range(tamanho_senha))
print("Senha gerada:", senha)