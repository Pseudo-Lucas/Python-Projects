#Programa criado com if e else para descobrir se posso dirigir
#ou não ou se preciso renovar minha CNH
#com base na idade do usuário

idade = int(input('Qual a sua idade? '))
if idade >= 18:
    cnh = input('Você tem CNH? (s/n)')
    if cnh == 's':
        cnh_valida = input ('Ela está válida? (s/n)')
        if cnh_valida == 's':
            print('Você pode dirigir.')
        else:
            print('Você precisa renovar sua CNH.')
    else:
        print('Você precisa tirar a CNH para dirigir.')
else:
    print('Você ainda não pode dirigir.')
    tempo_falta = 18 - idade
    if tempo_falta <= 2:
        print('Falta pouco tempo para você poder dirigir.')
    else:
        print('Demorará para você poder dirigir.')
    print('Mas você pode dirigir um kart se quiser.')
print('Fim!')
