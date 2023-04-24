from math import tan, cos, sin,radians,


def trigonometria(angulo):
    seno = sin(radians(angulo))
    cosseno = cos(radians(angulo))
    tangente = tan(radians(angulo))
    return print('seno: {}  cosseno: {}  tangente: {}'.format(seno, cosseno, tangente))