from thefuzz import process
from flask import abort

def matchea_ciudades(recibido):
    """
    Realiza una búsqueda de la ciudad más parecida a la entrada proporcionada y la devuelve en mayúsculas.
    
    Args:
        recibido (str): El nombre de la ciudad que se desea buscar.

    Returns:
        str: El nombre de la ciudad más parecida en mayúsculas.
    """
    return mejor_match(recibido).upper()

ciudades_real = ['toluca', 'tlc', 'monterrey', 'mty', 'ciudad de mexico', 'mex', 'tijuana', 'tij',
                 'hermosillo', 'hmo', 'ciudad del carmen', 'cme', 'chetumal', 'ctm',
                 'veracruz', 'ver', 'oaxaca', 'oax', 'huatulco', 'hux', 'ixtapa zihuatanejo', 'zih', 'puerto vallarta',
                 'pvr',
                 'lima', 'lim', 'havana', 'hav', 'bogota', 'bog', 'miami', 'mia', 'los ángeles', 'lax',
                 'new york', 'jfk', 'tampico', 'tam', 'torreón', 'trc', 'puerto escondido', 'pxm',
                 'acapulco', 'aca', 'mazatlan', 'mzt', 'guatemala', 'gua', 'aguascalientes', 'agu',
                 'cancun', 'cun', 'mérida', 'mid', 'villahermosa', 'vsa', 'belize', 'bze', 'guadalajara', 'gdl',
                 'dallas', 'dfw', 'cozumel', 'czm', 'chicago', 'ord', 'phoenix', 'phx', 'chihuahua', 'cuu',
                 'queretaro', 'qro', 'guanajuato', 'bjx', 'puebla', 'pbc', 'philadelphia', 'phl',
                 'san luis potosí', 'slp', 'charlotte', 'clt', 'toronto', 'yyz', 'houston', 'iah', 'vancouver',
                 'yvr', 'parís', 'cdg', 'ciudad juaréz', 'cjs', 'zacatecas', 'zcl', 'ámsterdam', 'ams',
                 'atlanta', 'atl', 'ciudad obregon', 'cen', 'madrid', 'mad', 'santiago', 'scl']

def mejor_match(ciudadd):
    """
    Encuentra la ciudad más parecida a la entrada proporcionada y la devuelve.
    
    Args:
        ciudadd (str): El nombre de la ciudad que se desea buscar.

    Returns:
        str: El nombre de la ciudad más parecida.
    """
    ciudadd.lower()

    if es_valido(ciudadd):
        abort(500)

    closest, ratio = process.extractOne(ciudadd, ciudades_real)

    if ratio < 75:
        abort(500)

    if len(ciudadd) == 3 or len(closest) == 3:
        return closest
    index = ciudades_real.index(closest)
    return ciudades_real[index + 1]

def es_valido(nombre):
    """
    Verifica si el nombre contiene dígitos numéricos.
    
    Args:
        nombre (str): El nombre a verificar.

    Returns:
        bool: True si el nombre contiene dígitos, False en caso contrario.
    """
    return any(char.isdigit() for char in nombre)


