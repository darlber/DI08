import datetime
import logging
import re


def calcular_periodo_tiempo(ultimo_acceso, fecha_actual=None):
    """
    python -m doctest -v calcular_tiempo.py
    
    Método separado del resto para poder testearlo de forma independiente, sin necesidad de
    inicializar la aplicación.
    Args:
        ultimo_acceso (str): Cadena que describe el tiempo transcurrido desde el último acceso.
                                Ejemplo: "2 días 3 horas" o "5 segundos".
        fecha_actual (datetime, optional): Fecha y hora actual para cálculos (útil para pruebas).

    Returns:
        str: Fecha y hora formateada del último acceso o mensaje de error.

    # los siguientes >>> son para el caso de que la fecha actual sea 2025-04-25 12:00:00

    >>> from datetime import datetime
    >>> mock_now = datetime(2025, 4, 25, 12, 0, 0)
    
    
    # Ejemplos de uso:
    
    # uso correcto: Días, horas, minutos y segundos
    >>> calcular_periodo_tiempo("1 día 5 horas 45 minutos 30 segundos", mock_now)
    '24-04-25 06:14:30'
    
    # uso correcto: Días, horas y minutos
    >>> calcular_periodo_tiempo("3 días 5 horas 20 minutos", mock_now)
    '22-04-25 06:40:00'
    
    # uso correcto: Días, horas y segundos
    >>> calcular_periodo_tiempo("3 días 5 horas 45 segundos", mock_now)
    '22-04-25 06:59:15'
    
    # uso correcto: Días y horas
    >>> calcular_periodo_tiempo("2 días 4 horas", mock_now)
    '23-04-25 08:00:00'
    
    # uso correcto: Días y minutos
    >>> calcular_periodo_tiempo("2 días 30 minutos", mock_now)
    '23-04-25 11:30:00'
    
    # uso correcto: Días y segundos
    >>> calcular_periodo_tiempo("2 días 45 segundos", mock_now)
    '23-04-25 11:59:15'
    
    # uso correcto: Horas, minutos y segundos
    >>> calcular_periodo_tiempo("4 horas 30 minutos 45 segundos", mock_now)
    '25-04-25 07:29:15'
    
    # uso correcto: Horas y minutos
    >>> calcular_periodo_tiempo("4 horas 30 minutos", mock_now)
    '25-04-25 07:30:00'
    
    # uso correcto: Horas y segundos
    >>> calcular_periodo_tiempo("5 horas 45 segundos", mock_now)
    '25-04-25 06:59:15'
    
    # uso correcto: Minutos y segundos
    >>> calcular_periodo_tiempo("30 minutos 45 segundos", mock_now)
    '25-04-25 11:29:15'
    
    # uso correcto: Solo días
    >>> calcular_periodo_tiempo("2 días", mock_now)
    '23-04-25 12:00:00'
    
    # uso correcto: Solo horas
    >>> calcular_periodo_tiempo("5 horas", mock_now)
    '25-04-25 07:00:00'
    
    # uso correcto: Solo minutos
    >>> calcular_periodo_tiempo("45 minutos", mock_now)
    '25-04-25 11:15:00'
    
    # uso correcto: Solo segundos
    >>> calcular_periodo_tiempo("45 segundos", mock_now)
    '25-04-25 11:59:15'
    
    # uso incorrecto. ÚltimoAcceso es nulo:
    >>> calcular_periodo_tiempo(None, mock_now)
    'Error: Último acceso no especificado'
    
    # uso incorrecto. ÚltimoAcceso es vacío:
    >>> calcular_periodo_tiempo("", mock_now)
    'Error: Último acceso no especificado'
    
    # uso incorrecto. ÚltimoAcceso tiene un formato incorrecto:
    >>> calcular_periodo_tiempo("formato incorrecto", mock_now)
    'Error: Formato de último acceso no válido'
    
    # uso incorrecto. ÚltimoAcceso tiene un formato incorrecto (no válido o esperado):
    >>> calcular_periodo_tiempo("horas 5 minutos", mock_now)
    'Error: Formato de último acceso no válido'

    """
    try:
        if not ultimo_acceso or ultimo_acceso.strip() == "":
            return "Error: Último acceso no especificado"

        # Obtener la fecha actual
        fecha_actual = fecha_actual or datetime.datetime.now()

        # Inicializar variables
        dias = horas = minutos = segundos = 0

        # Expresión regular para extraer valores de tiempo
        # Este patrón de expresión regular busca coincidencias de tiempo en texto, como "2 días 3 horas 15 minutos 10 segundos".
    # Cada parte (días, horas, minutos, segundos) es opcional y puede aparecer en cualquier combinación.
        pattern = r"(?:(\d+)\s*días?)?\s*(?:(\d+)\s*horas?)?\s*(?:(\d+)\s*minutos?)?\s*(?:(\d+)\s*segundos?)?"
        match = re.fullmatch(pattern, ultimo_acceso.strip())

        if not match:
            return "Error: Formato de último acceso no válido"

        # Extraer valores de tiempo (si están presentes)
        dias, horas, minutos, segundos = (int(value) if value else 0 for value in match.groups())

        # Calcular la fecha y hora del último acceso
        delta = datetime.timedelta(days=dias, hours=horas, minutes=minutos, seconds=segundos)
        fecha_ultimo_acceso = fecha_actual - delta

        return fecha_ultimo_acceso.strftime("%d-%m-%y %H:%M:%S")

    except Exception as e:
        logging.error(f"Error al calcular el período de tiempo: {str(e)}")
        return "Error al calcular el tiempo"