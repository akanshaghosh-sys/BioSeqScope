# Import matplotlib library
import matplotlib.pyplot as plt
import numpy as np


bases = ["Adenine", "Thymine", "Guanine", "Cytosine"]


composition = [22068, 22309, 14785, 14146]


colors = ["Pink", "Cyan", "Lightgreen", "Orange"]


plt.pie(composition,
        labels=bases,
        colors=colors,
        autopct="%1.1f%%",
        startangle=90)

plt.title("Composition of Nitrogenous Bases")

plt.show()
