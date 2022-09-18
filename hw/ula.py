#!/usr/bin/env python3

from myhdl import *


#estava com problema de importaçao, entao coloquei aqui
@block
def mux2way(q, a, b, sel):

    @always_comb
    def comb():
        if sel == 0:
            q.next = a
        else:
            q.next = b

    return comb

@block
def barrelShifter(a, dir, size, q):

    @always_comb
    def comb():
        if dir == 0:
            q.next = a >> size
        else:
            q.next = a << size

    return comb




@block
def ula(x, y, c, zr, ng, saida, width=16):

    zx_out = Signal(intbv(0)[width:])
    nx_out = Signal(intbv(0)[width:])
    zy_out = Signal(intbv(0)[width:])
    ny_out = Signal(intbv(0)[width:])
    and_out = Signal(intbv(0)[width:])
    add_out = Signal(intbv(0)[width:])
    mux_out = Signal(intbv(0)[width:])
    no_out = Signal(intbv(0)[width:])

    c_zx = c(5)
    c_nx = c(4)
    c_zy = c(3)
    c_ny = c(2)
    c_f = c(1)
    c_no = c(0)

    zx = zerador(c_zx, x, zx_out)
    zy = zerador(c_zy, y, zy_out)

    nx = inversor(c_nx, zx_out, nx_out)
    ny = inversor(c_ny, zy_out, ny_out)
    
    a = add(nx_out, ny_out, add_out)
    a2 = nx_out & ny_out

    mux = mux2way(mux_out, a2, add_out, c_f)
    
    no = inversor(c_no, mux_out, no_out)

    c = comparador(no_out, zr, ng, width)

    @always_comb
    def comb():
        saida.next = no_out

    return instances()


# -z faz complemento de dois
# ~z inverte bit a bit
@block
def inversor(z, a, y):
    @always_comb
    def comb():
        if z:
            y.next = ~a
        else:
            y.next = a

    return instances()


@block
def comparador(a, zr, ng, width):
    # width insica o tamanho do vetor a
    @always_comb
    def comb():
        if a.val == 0:
            zr.next = 1
        else:
            zr.next = 0
        if a[width - 1] == 1:
            ng.next = 1
        else:
            ng.next = 0

    return instances()


@block
def zerador(z, a, y):
    @always_comb
    def comb():
        if z:
            y.next = 0
        else:
            y.next = a   

    return instances()


@block
def add(a, b, q):
    @always_comb
    def comb():
        soma = a + b
        if soma > 65535: #255:
            q.next = 0
        else:
            q.next = soma

    return instances()


@block
def inc(a, q):
    a = add(a, Signal(intbv(1)), q)

    return instances()


# ----------------------------------------------
# Conceito B
# ----------------------------------------------


@block
def halfAdder(a, b, soma, carry):
    s = Signal(bool())
    c = Signal(bool())

    @always_comb
    def comb():
        s = a ^ b
        c = a & b

        soma.next = s
        carry.next = c

    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    s = [Signal(bool(0)) for i in range(3)]
    haList = [None for i in range(2)]

    haList[0] = halfAdder(a, b, s[0], s[1])  # 2
    haList[1] = halfAdder(c, s[0], soma, s[2])  # 3

    @always_comb
    def comb():
        carry.next = s[1] | s[2]  # 4

    return instances()


@block
def addcla4(a, b, q):
    # 4-bit adder with carry lookahead
    s = [Signal(bool(0)) for i in range(4)]
    faList = [None for i in range(3)]

    faList[0] = fullAdder(a[0], b[0], 0, s[0], faList[1].carry)  # 2
    faList[1] = fullAdder(a[1], b[1], faList[0].carry, s[1], faList[2].carry)  # 3
    faList[2] = fullAdder(a[2], b[2], faList[1].carry, s[2], q[3])  # 4

    @always_comb
    def comb():
        q[0].next = s[0]
        q[1].next = s[1]
        q[2].next = s[2]

    return instances()


@block
def addcla16(a, b, q):
    # 16-bit adder with carry lookahead
    s = [Signal(intbv(0)[16:]) for i in range(4)]
    claList = [None for i in range(4)]

    claList[0] = addcla4(a[0:4], b[0:4], s[0])  # 2
    claList[1] = addcla4(a[4:8], b[4:8], s[1])  # 3
    claList[2] = addcla4(a[8:12], b[8:12], s[2])  # 4
    claList[3] = addcla4(a[12:16], b[12:16], s[3])  # 5

    @always_comb
    def comb():
        q[0:4].next = s[0]
        q[4:8].next = s[1]
        q[8:12].next = s[2]
        q[12:16].next = s[3]

    return instances()


# ----------------------------------------------
# Conceito A
# ----------------------------------------------


@block
def ula_new(x, y, c, zr, ng, sr, sf, bcd, saida, width=16):
    pass


@block
def bcdAdder(x, y, z):
    pass
