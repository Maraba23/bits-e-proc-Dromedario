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
def barrelShifter2(a, sr, sl, size, q):

    @always_comb
    def comb():
        a_ = a
        if sr == 1:
            a_ = a_ >> size
        if sl == 1:
            a_ = a_ << size
        
        q.next = a_

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
def addcla4(a, b, carry0, q):
    # 4-bit adder with carry lookahead
    a_ = [a(i) for i in range(4)]
    b_ = [b(i) for i in range(4)]

    @always_comb
    def comb():
        carry = [0 for i in range(5)]
        carry[0] = carry0
        for i in range(4):
            carry[i + 1] = (a_[i] & b_[i]) | ((a_[i] ^ b_[i]) & carry[i])
        
        for i in range(4):
            q.next[i] = (a_[i] ^ b_[i]) ^ carry[i]

    return instances()


@block
def addcla16(a, b, q):
    # 16-bit adder with carry lookahead
    a_ = [a(i) for i in range(16)]
    b_ = [b(i) for i in range(16)]
    
    #claList[0] = addcla4(a_[0], b_[0], carry[0], s[0])  # 2
    #claList[1] = addcla4(a_[1], b_[1], carry[1], s[1])  # 3
    #claList[2] = addcla4(a_[2], b_[1], carry[2], s[2])  # 4
    #claList[3] = addcla4(a_[3], b_[3], carry[3], s[3])  # 5

    @always_comb
    def comb():
        carry = [0 for i in range(17)]
        for i in range(16):
            carry[i + 1] = (a_[i] & b_[i]) | ((a_[i] ^ b_[i]) & carry[i])
        
        if carry[16] == 0:
            for i in range(16):
                q.next[i] = (a_[i] ^ b_[i]) ^ carry[i]
        else:
            q.next = 0

    return instances()


# ----------------------------------------------
# Conceito A
# ----------------------------------------------


@block
def ula_new(x, y, c, zr, ng, sr, sl, bcd, saida, width=16):
    sx_out = Signal(intbv(0)[width:])
    bcd_out = Signal(intbv(0)[width:])
    zx_out = Signal(intbv(0)[width:])
    nx_out = Signal(intbv(0)[width:])
    zy_out = Signal(intbv(0)[width:])
    ny_out = Signal(intbv(0)[width:])
    and_out = Signal(intbv(0)[width:])
    add_out = Signal(intbv(0)[width:])
    mux_out = Signal(intbv(0)[width:])
    mux1_out = Signal(intbv(0)[width:])
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
    
    sx = barrelShifter2(nx_out, sr, sl, ny_out, sx_out)

    a1 = bcdAdder(sx_out, ny_out, bcd_out)
    a2 = addcla16(sx_out, ny_out, add_out)
    a3 = sx_out & ny_out

    mux0 = mux2way(mux_out, add_out, bcd_out, bcd)

    mux1 = mux2way(mux1_out, a3, mux_out, c_f)
    
    no = inversor(c_no, mux1_out, no_out)

    c = comparador(no_out, zr, ng, width)

    @always_comb
    def comb():
        saida.next = no_out

    return instances()


DIG0 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
DIG1 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9)
@block
def bcdAdder(x, y, z):

    @always_comb
    def comb():
        soma = x + y

        if soma > 99:
            z.next = 0

        else:
            bc1 = intbv(DIG1[int(soma)])[4:]
            bc0 = intbv(DIG0[int(soma)])[4:]

            z.next = concat(bc1, bc0)


    return instances()