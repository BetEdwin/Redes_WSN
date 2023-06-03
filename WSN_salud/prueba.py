import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QTimer
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import numpy
import pandas
import math
import os
import sys
import datetime
import random

from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
from matplotlib import *
import random

from PyQt5 import QtCore, QtGui, Qt, QtWidgets, uic
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super (MainWindow, self).__init__()
        uic.loadUi('interfaz.ui',self)
        
        # Carga los datos del archivo de texto y muestra en la tabla
        self.load_data_to_table()
        self.grafic.clicked.connect(self.graficar)
        self.led.clicked.connect(self.toggle_led)
        
        self.LED_PIN = 7
        self.BUTTON_PIN = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.LED_PIN, GPIO.OUT)
        GPIO.setup(self.BUTTON_PIN, GPIO.IN)
        GPIO.output(self.LED_PIN, GPIO.LOW)

    def load_data_to_table(self):
        # Ruta del archivo de texto
        file_path = "C:/Users/Fabian/Documents/TELECO-2023/REDES DE SENSORES AD HOC/datos_sensores.txt"  # Reemplaza "ruta_del_archivo.txt" con la ruta real de tu archivo

        # Leer el contenido del archivo de texto
        with open(file_path, "r") as file:
            content = file.readlines()

        # Eliminar los caracteres de salto de línea y dividir en columnas
        data = [line.strip().split(",") for line in content]

        # Establecer el número de filas y columnas de la tabla
        num_rows = len(data)
        num_cols = len(data[0])
        self.table.setRowCount(num_rows)
        self.table.setColumnCount(num_cols)

        # Agregar los datos a la tabla
        for i, row in enumerate(data):
            for j, value in enumerate(row):
                item = QTableWidgetItem(value)
                self.table.setItem(i, j, item)


    def graficar(self):
            # Sensores de la UCI
            sensores = ['Sensor1', 'Sensor2', 'Sensor3', 'Sensor4']
            # Generar datos simulados para los 4 que se requieren clinicamente
            num_datos = 200
            datos_sensores = []
            for sensor in sensores:
                datos_sensor = [random.uniform(0, 1) for _ in range(num_datos)]
                datos_sensores.append(datos_sensor)
            # Subplots para cada sensor
            fig, axs = plt.subplots(len(sensores), 1, figsize=(12, 9))
            for i, datos_sensor in enumerate(datos_sensores):
                axs[i].plot(datos_sensor, 'darkblue')
                axs[i].set_ylabel('m Volts')
                axs[i].set_title(sensores[i])
                
            plt.xlabel('Seg')
            plt.tight_layout()
            plt.show()
            
    def toggle_led(self):
        #if self.led.isChecked==True:
        if GPIO.input(self.BUTTON_PIN) == GPIO.HIGH:
            GPIO.output(self.LED_PIN, GPIO.HIGH)
            self.label_5.setText("LED encendido")
        else:
            GPIO.output(self.LED_PIN, GPIO.LOW)
            self.label_5.setText("LED apagado")  

# Crea una instancia de la aplicación Qt
app = QApplication(sys.argv)

# Crea una instancia de tu clase MainWindow
main_window = MainWindow()

# Muestra la ventana principal
main_window.show()

# Ejecuta el bucle principal de la aplicación
sys.exit(app.exec_())


if __name__=="__main__":
     main()
     
