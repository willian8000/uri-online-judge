from datetime import timedelta

diaInicio = input().split(" ")
horainicio = input().split(" : ")
diaFim = input().split(" ")
horFim = input().split(" : ")

# valor de 1 dia em segundos 86.400
# valor de 1 hora em segundos 3.600
# valor de 1 minuto em segundos 60 

# Obeter o total do inicio e fim em segundos
# Substrair total do fim com o total do inicio
# Converter os valores respectivamente em dias, horas, minutos e segundos

segundos = (
    ((int(diaFim[1]) * 86400) + (int(horFim[0]) * 3600) 
    + (int(horFim[1]) * 60) + int(horFim[2])) -
    ((int(diaInicio[1]) * 86400) + (int(horainicio[0]) * 3600) 
    + (int(horainicio[1]) * 60) + int(horainicio[2]))
    )

dias, segundos = int(segundos / 86400), segundos - (int(segundos / 86400) * 86400)
horas, segundos = int(segundos / 3600), segundos - (int(segundos / 3600) * 3600)
minutos, segundos = int(segundos / 60), segundos - (int(segundos / 60) * 60)

print('{0} dia(s)\n{1} hora(s)\n{2} minuto(s)\n{3} segundo(s)'.
format(dias, horas, minutos, segundos))