# crie uma variável de string que receba uma frase qualquer. crie uma segunda variável, agora contendo
# a metade da string digitada. Imprima na tela somente os dois ultimos
# caracteres da segunda variável do tipo string

# len é tipo length

frase = input('Digite uma frase: ')
tam = len(frase)

frase2 = frase[:int(tam/4)]
print(frase2[-2:])
