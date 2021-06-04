import matplotlib.pyplot as plt

#DEFINIMOS LAS ETIQUETAS
manzanas = [20, 10, 15, 30]
nombres = ["Ana","Juan","Maycol", "Alysson"]

# DIBUJAMOS LA GRAFICA 
plt.pie(manzanas, labels=nombres, autopct="%0.1f %%")

# MOSTRAMOS LA GRAFICA 
plt.show()