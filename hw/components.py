#!/usr/bin/env python3

from myhdl import *


@block
def and16(a, b, q):
    """
    a: 16 bits
    b: 16 bits
    q: 16 bits

    and bit a bit entre a e b
    """
    foo = Signal(0)

    @always_comb
    def comb():
        q.next = a and b

    return comb


@block
def or8way(a, b, c, d, e, f, g, h, q):
    """
    a, b, c, ... h: 1 bit

    or bit a bit entre a e b
    """
    foo = Signal(intbv(0))

    @always_comb
    def comb():
        q.next = (((((((a or b) or c) or d) or e) or f) or g) or h)

    return comb


@block
def orNway(a, q):
    """
    a: 16 bits
    q: 1 bit

    or bit a bit dos valores de a: a[0] or a[1] ...
    """
    foo = Signal(intbv(0))

    @always_comb
    def comb():
        q.next = a[0] or a[1] or a[2] or a[3] or a[4] or a[5] or a[6] or a[7] or a[8] or a[9] or a[10] or a[11] or a[12] or a[13] or a[14] or a[15]
        
    return comb


@block
def barrelShifter(a, dir, size, q):
    """
    a: 16 bits
    dir: 1 bit
    size: n bits
    q: 16 bits

    se dir for 0, shifta para direita `size`
    se dir for 1, shifta para esquerda `size`

    exemplo: a = 0000 1111 0101 1010, dir = 0, size = 3
             q = 0111 1010 1101 0000
    """


    @always_comb
    def comb():
        if dir == 0:
            q.next = a >> size
        else:
            q.next = a << size

    return comb


@block
def mux2way(q, a, b, sel):
    """
    q: 16 bits
    a: 16 bits
    b: 16 bits
    sel: 2 bits

    Mux entre a e b, sel é o seletor
    """

    @always_comb
    def comb():
        list=[a, b]
        q.next = list[sel]

    return comb


@block
def mux4way(q, a, b, c, d, sel):
    """
    q: 16 bits
    a: 16 bits
    b: 16 bits
    c: 16 bits
    d: 16 bits
    sel: 4 bits

    Mux entre a, b, c, d sel é o seletor
    """

    @always_comb
    def comb():
        list=[a, b, c, d]
        q.next = list[sel]

    return comb


@block
def mux8way(q, a, b, c, d, e, f, g, h, sel):
    """
    Mux de 8 entradas, simular aos anteriores.
    """


    @always_comb
    def comb():
        list=[a, b, c, d, e, f, g, h]
        q.next = list[sel]

    return comb


@block
def deMux2way(a, q0, q1, sel):
    """
    deMux de 2 saídas e uma entrada.

    - Lembre que a saída que não está ativada é 0

    Exemplo:

    a = 0xFFAA, sel = 0
    q0 = 0xFFAA
    q1 = 0
    """

    foo = Signal(intbv(0))

    @always_comb
    def comb():

        saida = [q0, q1]

        for i in range(2):
            if i == sel:
                saida[i].next = a
            else:
                saida[i].next = 0

    return comb


@block
def deMux4way(a, q0, q1, q2, q3, sel):
    """
    deMux de 4 saídas e uma entrada.

    - Lembre que a saída que não está ativada é 0
    """

    foo = Signal(intbv(0))

    @always_comb
    def comb():
        saidas = [q0, q1, q2, q3]

        for i in range(4):
            if i == sel:
                saidas[i].next = a
            else:
                saidas[i].next = 0

    return comb


@block
def deMux8way(a, q0, q1, q2, q3, q4, q5, q6, q7, sel):
    """
    deMux de 8 saídas e uma entrada.

    - Lembre que a saída que não está ativada é 0
    """

    foo = Signal(intbv(0))

    @always_comb
    def comb():
        saidas = [q0, q1, q2, q3, q4, q5, q6, q7]

        for i in range(len(saidas)):
            if i == sel:
                saidas[i].next = a
            else:
                saidas[i].next = 0


    return comb


# -----------------------------#
# Conceito B
# -----------------------------#
#
@block
def bin2hex(hex0, sw):
    """
    importar do lab!
    """

    @always_comb
    def comb():
        if sw[4:0] == 0:
            hex0.next = "1111110"
        elif sw[4:0] == 1:
            hex0.next = "0110000"
        elif sw[4:0] == 2:
            hex0.next = "1101101"
        elif sw[4:0] == 3:
            hex0.next = "1111001"
        elif sw[4:0] == 4:
            hex0.next = "0110011"
        elif sw[4:0] == 5:
            hex0.next = "1011011"
        elif sw[4:0] == 6:
            hex0.next = "1011111"
        elif sw[4:0] == 7:
            hex0.next = "1110001"
        elif sw[4:0] == 8:
            hex0.next = "1111111"
        elif sw[4:0] == 9:
            hex0.next = "1110011"
        elif sw[4:0] == 10:
            hex0.next = "1110111"
        elif sw[4:0] == 11:
            hex0.next = "0011111"
        elif sw[4:0] == 12:
            hex0.next = "1001110"
        elif sw[4:0] == 13:
            hex0.next = "0111101"
        elif sw[4:0] == 14:
            hex0.next = "1001111"
        elif sw[4:0] == 15:
            hex0.next = "1000111"
        else:
            hex0.next = "0000000"

    return instances()


@block
def bin2bcd(b, bcd1, bcd0):
    """
    componente que converte um vetor de b[8:] (bin)
    para dois digitos em BCD

    Exemplo:
    bin  = `01010010`
    BCD1 = 8
    BCD0 = 2
    """
    

    @always_comb
    def comb():

        for i in range(7):
            b = b << 1
            if int(b[12:8]) > 4:
                b += (2**8)*3
        
        b = b << 1

        bcd0.next = b[12:8]
        bcd1.next = b[16:12]

        #bcd0.next = int(str(int(bin(b), 2))[1])
        #bcd1.next = int(str(int(bin(b), 2))[0])

    return comb


# -----------------------------#
# Conceito A
# -----------------------------#
