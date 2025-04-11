"""
# TUTORIAL DE CURSOR: EL IDE CON INTEGRACIÓN DE IA
# =================================================

# Cursor es un IDE moderno basado en VSCode que integra modelos de IA avanzados
# como Claude y GPT para asistir en el desarrollo de software. Este tutorial
# explicará sus principales características y cómo aprovecharlas.

# 1. FUNCIONALIDADES BÁSICAS DE CURSOR
# ------------------------------------

# 1.1 Interfaz de usuario
# Cursor mantiene una interfaz similar a VSCode, con:
# - Explorador de archivos en el panel lateral izquierdo
# - Editor de código en el panel central
# - Terminal integrada
# - Barra de estado inferior
# - Paleta de comandos (Ctrl+Shift+P)

# 1.2 Gestión de proyectos
# - Apertura de carpetas y espacios de trabajo
# - Control de versiones con Git integrado
# - Extensiones compatibles con VSCode

# 2. INTEGRACIÓN CON IA
# ---------------------

# 2.1 Chat con IA (Comando: Ctrl+L)
# El chat con IA permite interactuar directamente con el modelo, pudiendo:
# - Hacer preguntas sobre código
# - Solicitar explicaciones
# - Pedir sugerencias para resolver problemas

def ejemplo_chat():
    # Puedes preguntar a la IA:
    # "¿Cómo puedo optimizar esta función?"
    # "Explica cómo funciona este algoritmo"
    # "¿Cómo implementaría un sistema de autenticación en Python?"
    pass

# 2.2 Generación de código (Comando: Alt+/)
# Cursor puede generar código automáticamente basado en comentarios o instrucciones

def ejemplo_generacion():
    # Escribe un comentario como:
    # "Crea una función que ordene una lista de diccionarios por el valor de la clave 'fecha'"
    # Y la IA generará el código correspondiente
    
    # Ejemplo de código que la IA podría generar:
    def ordenar_por_fecha(lista_diccionarios):
        from datetime import datetime
        return sorted(lista_diccionarios, 
                     key=lambda x: datetime.strptime(x['fecha'], '%Y-%m-%d'))

# 2.3 Completado de código inteligente
# Cursor predice y sugiere código mientras escribes, más allá de lo que hacen
# los completados tradicionales

def ejemplo_completado():
    # Al escribir el comienzo de una función, Cursor puede sugerir
    # la implementación completa basada en el nombre y contexto
    
    # Por ejemplo, al escribir "def validar_email(email):"
    # Cursor podría sugerir una implementación completa con regex
    pass

# 3. EDICIÓN ASISTIDA POR IA
# --------------------------

# 3.1 Refactorización de código
# Para refactorizar código con IA, selecciona el código y usa Ctrl+Shift+L

def codigo_para_refactorizar():
    # Código con problemas de legibilidad o eficiencia
    n = 10
    r = []
    for i in range(n):
        if i % 2 == 0:
            r.append(i * i)
    return r

    # Después de refactorizar con IA, podría verse así:
    # return [i * i for i in range(10) if i % 2 == 0]

# 3.2 Explicación de código
# Selecciona código y pregunta a la IA "¿Qué hace este código?"

def codigo_complejo(data, threshold=0.5):
    result = {}
    for key, values in data.items():
        filtered = [v for v in values if v > threshold]
        if filtered:
            result[key] = sum(filtered) / len(filtered)
    return result
    
    # Puedes seleccionar esta función y preguntar a la IA
    # para obtener una explicación detallada

# 3.3 Corrección de errores y debugging
# La IA puede ayudar a identificar y corregir errores en tu código

def funcion_con_error():
    try:
        result = 10 / 0
        return result
    except Exception as e:
        # Puedes preguntar a la IA sobre este error
        # "¿Cómo puedo manejar correctamente esta división por cero?"
        pass

# 4. FUNCIONALIDADES AVANZADAS
# ---------------------------

# 4.1 Análisis de código en repositorios
# Cursor puede analizar grandes repositorios y entender su estructura

def ejemplo_analisis_repo():
    # Puedes preguntar a la IA:
    # "¿Dónde se implementa la función X en este repositorio?"
    # "Resume la arquitectura de este proyecto"
    pass

# 4.2 Creación de tests automatizados
# La IA puede generar tests para tu código

def suma(a, b):
    return a + b

# Puedes pedir: "Genera tests unitarios para esta función"
# Y la IA creará tests como:
"""
import unittest

class TestSuma(unittest.TestCase):
    def test_suma_positivos(self):
        self.assertEqual(suma(2, 3), 5)
        
    def test_suma_negativos(self):
        self.assertEqual(suma(-1, -1), -2)
        
    def test_suma_mixto(self):
        self.assertEqual(suma(-1, 1), 0)
"""

# 4.3 Documentación automática
# Cursor puede generar documentación para tu código

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        
    def cambiar_email(self, nuevo_email):
        # Validar email
        if '@' in nuevo_email:
            self.email = nuevo_email
            return True
        return False

# Puedes pedir: "Documenta esta clase con docstrings"

# 5. CONSEJOS Y BUENAS PRÁCTICAS
# -----------------------------

# 5.1 Dar contexto a la IA
# Cuanto más contexto des a la IA, mejores serán sus respuestas

# 5.2 Usar comentarios para guiar la generación
# Los comentarios claros ayudan a la IA a entender tus intenciones

# 5.3 Iterar sobre las respuestas
# Si la primera respuesta no es perfecta, refina tu pregunta

# 5.4 Combinar la IA con tu experiencia
# La IA es una herramienta, tu criterio sigue siendo esencial

# 6. ATAJOS DE TECLADO IMPORTANTES
# -------------------------------
# Ctrl+L: Abrir chat con IA
# Alt+/: Completar código con IA
# Ctrl+Shift+L: Enviar código seleccionado a la IA
# Ctrl+Enter: Ejecutar código en terminal integrada
# Ctrl+Shift+P: Paleta de comandos

# CONCLUSIÓN
# ----------
# Cursor combina las mejores características de un IDE moderno con la potencia
# de la IA, permitiendo aumentar significativamente la productividad de los
# desarrolladores. La clave está en aprender a formular las preguntas correctas
# y a integrar la IA en tu flujo de trabajo de programación.
"""
