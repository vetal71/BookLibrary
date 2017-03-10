"""
    Функции
"""

def separateRight(str, delim="="):
    if len(str) == 0:
        return ''
    pos = str.index(delim)
    if pos == 0:
        return str
    else:
        return str[pos + 1:]

def separateLeft(str, delim="="):
    if len(str) == 0:
        return ''
    pos = str.index(delim)
    if pos == 0:
        return str
    else:
        return str[:pos - 1]