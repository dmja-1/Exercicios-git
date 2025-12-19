def calcularTempo(segundos):

    horas = segundos // 3600
    resto = segundos % 3600
    minutos = resto // 60
    resto_segundos = resto % 60

    return horas, minutos, resto_segundos

seg = int(input("Digite quantos segundos a fábrica ficou ativa: "))

tempo = calcularTempo(seg)

horas, minutos, resto_segundos = tempo

print(f"A fábrica ficou ativa por {horas} horas, {minutos} minutos e {resto_segundos} segundos")

''' // é para pegar o valor inteiro sem virgula do quociente, % é para pegar o resto, por logica, 3600 = 60 * 60 '''