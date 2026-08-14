#Calculadora interactiva

nombre = input("Nombre de usuario: ")
print("Ingresa 5 aplicaciones que mas usas: ")
app1 = input("App 1: ")
app2 = input("App 2: ")
app3 = input("App 3: ")
app4 = input("App 4: ")
app5 = input("App 5: ")

print("Ingresa el tiempo que le dedicas a cada aplicación:")

t_app1 = float(input("Tiempo en horas de " + app1 + ": "))
t_app2 = float(input("Tiempo en horasde " + app2 + ": "))  
t_app3 = float(input("Tiempo en horas de " + app3 + ": "))
t_app4 = float(input("Tiempo en horas de " + app4 + ": "))
t_app5 = float(input("Tiempo en horas de " + app5 + ": "))

tiempo_total = t_app1 + t_app2 + t_app3 + t_app4 + t_app5
print("El tiempo total dedicado a las aplicaciones es de:", tiempo_total, "horas")

porcentaje_total = (tiempo_total / 24)* 100
print("El porcentaje del tiempo total dedicado a las aplicaciones es de:", porcentaje_total, "%")
print("Utilizas mucho el celular ponte a hacer algo productivo")
