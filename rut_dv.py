#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Calculo del Digito Validador del RUT (Rol Único Tributario, Chile). 
Compatible con Python2 y Python3

Licencia: Public Domain
Author: Daniel Aguayo Catalan <daniel_aguayo_catalan@lavabit.com>

El siguiente código se puede reducir eliminando las partes de
intención didáctica.
"""

# El RUT como STRING desde entrada por teclado 
rut_string = str(eval(repr(input())))

rut = [number for number in rut_string][:8]# usa sólo los 8 primeros caracteres

def rut_dv(rut):
    val = 2*list(range(4,10)[::-1])[:8] #val = [9,8,7,6,5,4,9,8]
    rut.reverse()
    dv = sum([int(r)*n for r,n in zip(rut,val)]) % 11
    if dv == 10: dv = 'k'
    return(dv)

print(rut_dv(rut))
