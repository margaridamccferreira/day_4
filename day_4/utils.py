'''
Created on Feb 6, 2018

@author: Maggy
'''
def reverter_sequencia(qualquer_sequencia):
    return qualquer_sequencia[::-1]

def complementar_sequencia(qualquer_sequencia):
    sequencia_complemento = ""
    for i in qualquer_sequencia:
        if (i == 'A' or i == 'a'): sequencia_complemento += 'T'
        elif (i == 'C' or i == 'c'): sequencia_complemento += 'G'
        elif (i == 'G' or i == 'g'): sequencia_complemento += 'C'
        elif (i == 'T' or i == 't' or i == 'U' or i == 'u'): sequencia_complemento += 'A'
        else: sequencia_complemento += i
    return sequencia_complemento


def is_number(valor):
    """
    param: any value
    return: int if value is integer
    """
    try: 
        return int(valor)
    except:
        return None
    
def is_float(valor):
    """
    param: any value
    return: float if value is real
    """
    try: 
        return float(valor)
    except:
        return None

