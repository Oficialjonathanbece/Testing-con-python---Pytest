import unittest
import datetime
import logging
        
class Greeter:
    def __init__(self):
# Configurar el registro
        logging.basicConfig(filename='greeter.log', level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')

    def greet(self):    
# Pide el nombre, Elimina espacios en blanco al principio y final, Coloca la primera letra mayuscula 
        name = input("¿Cómo te llamas? ").capitalize().strip()
# Obtener la hora actual
        current_time = datetime.datetime.now().hour
# Generar el saludo personalizado
        if 6 <= current_time <= 12:
            greeting = f"Buenos días, {name}!"
        elif 18 <= current_time <= 22:
            greeting = f"Buenas tardes, {name}!"
        else:
            greeting = f"Buenas noches, {name}!"
# Registrar la llamada a la función
        logging.info(f"Se llamó a greet() para {name} a las {current_time}:{datetime.datetime.now().minute}")
# Imprimir el saludo
        print(greeting)

# Logica de uso
greeter = Greeter()
greeter.greet()

def sum(a, b):
    return a + b


class SumTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)


if __name__ == '__main__':
    unittest.main()