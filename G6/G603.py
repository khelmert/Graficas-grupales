import matplotlib.pyplot as plt

#CREAMOS LAS LISTAS.
turistas = [86.9, 81.8, 75.5, 60.4, 58.2, 39.3, 37.2, 37.4, 37.8, 35.8]
paises = ["Francia", "España", "EE.UU", "China", "Italia", "Mexico", "Reino Unido", "Turquia", "Alemania", "Tailandia"]
explode = [0, 0.2, 0, 0, 0, 0.4, 0, 0, 0, 0]

plt.pie (turistas, labels=paises, explode=explode, autopct="%1.1f%%", shadow=True, startangle=90)
plt.title("TOP 10 DESTINOS TURISTICOS EN 2017")
plt.show()