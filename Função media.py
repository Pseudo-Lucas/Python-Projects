def media(a, b, c):                 #função para exibir a media entre 3 números
    return(a+b+c)/3

x = float(input('Digite um número: '))
y = float(input('Digite mais um número: '))
z = float(input('Digite mais um número: '))

h = media(x, y, z)

print(f'A media entre os número {x}, {y} e {z} é igual a {h}')

