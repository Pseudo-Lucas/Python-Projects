# Funções #
def pede_idade(mensagem):
    idade = int(input('Digite sua idade: '))
    return idade

# Código Principal #
idade = pede_idade('Digite sua idade: ')

if idade > 18:
    print('Você tem mais de 18 anos')
else:
    print('Você tem menos de 18 anos')
print('fim')
