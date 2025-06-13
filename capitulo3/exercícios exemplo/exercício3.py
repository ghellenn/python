def calculaDiametro(raio):
    return 2 * raio

def calculaCircunferencia(raio, pi):
    return (2 * raio) * pi

def calculaAreaCircunferencia(raio, pi):
    return pi * (raio ** 2)

# main
raio = int(input("Digite o valor do raio:"))
pi = 3.14159

diametro = calculaDiametro(raio)
circunferencia = calculaCircunferencia(raio, pi)
areaCircunferencia = calculaAreaCircunferencia(pi, raio)

print("O valor do Diametro é: ", diametro)
print("O valor da Circunferencia é: ", circunferencia)
print("O valor da Area da Circunferencia é: ", areaCircunferencia)
