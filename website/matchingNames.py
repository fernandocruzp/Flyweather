from thefuzz import process
from flask import abort

"""
Regresa el nombre de la ciudad recibido en el tipo adecuado para su búsqueda
"""

def matchea_ciudades(recibido):
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

"""
De la lista de ciudades, regresa el código IATA de aquella que tiene mayor parecido a el nombre de la ciudad recibida
"""


def mejor_match(ciudadd):
    ciudadd.lower()

    if es_valido(ciudadd):
        abort(500)

    closest, ratio = process.extractOne(ciudadd, ciudades_real)

    if ratio < 75:
        abort(500)

    """
    En caso de que se haya ingresado un código IATA
    """
    if len(ciudadd) == 3 or len(closest) == 3:
        return closest
    index = ciudades_real.index(closest)
    return ciudades_real[index + 1]

def es_valido(nombre):
    return any(char.isdigit() for char in nombre)

