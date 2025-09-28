# Bibliotecas
import secrets


# Perguntas ao usuário
tamanho_senha = input(int("Digite o tamanho da senha: "))
caracteres_especiais = input("Incluir caracteres especiais? (s/n): ")
numeros = input("Incluir números? (s/n): ")
maiusculas = input("Incluir letras maiúsculas? (s/n): ")
minusculas = input("Incluir letras minúsculas? (s/n): ")

# Gerar senha para o usuário
caracteres = ""

if caracteres_especiais == 's' or caracteres_especiais == 'S':
    caracteres += "!@#$%¨&*()_+{}[];:,.<>?/|"