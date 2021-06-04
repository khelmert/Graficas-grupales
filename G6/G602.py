import matplotlib.pyplot as plt

etiquetas = ["A", "B", "C", "D", "E", "F"]

#PORCENTAJE DE CADA PORCIÓN.    
porcentas = [14, 3, 8, 6, 9, 7]

#DEFINIMOS COLORES.
colores = ["#1abc9c", "#f1c40f", "#8e44ad", "#e74c3c", "#34495e", "#34983b"]

#DIBUJAMOS LA GRAFICA.
plt.pie(porcentas, labels = etiquetas, colors = colores, startangle = 90, explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1), radius=1.2, autopct="%1.2f%%")

plt.show()
