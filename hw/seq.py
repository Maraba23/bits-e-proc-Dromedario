#!/usr/bin/env python3

from myhdl import *
from .components import mux2way
from .ula import inc


@block
def ram(dout, din, addr, we, clk, rst, width, depth):
    loads = [Signal(bool(0)) for i in range(depth)]
    outputs = [Signal(modbv(0)[width:]) for i in range(depth)]
    registersList = [None for i in range(depth)]

    for i in range(len(registersList)):
        registersList[i] = registerN(din, loads[i], outputs[i], width, clk, rst)
    
    @always_comb
    def comb():
        for a in range(len(registersList)):
            if a == addr:
                loads[a].next = we
            else:
                loads[a].next = 0

        dout.next = outputs[addr]

    return instances()


@block
def pc(increment, load, i, output, width, clk, rst):
    regIn = Signal(modbv(0)[width:])
    regOut = Signal(modbv(0)[width:])
    regLoad = Signal(bool(0))

    mux1out = Signal(modbv(0)[width:]) 
    mux2out = Signal(modbv(0)[width:])
    incout = Signal(modbv(0)[width:])

    reg = registerN(regIn, regLoad, regOut, width, clk, rst)

    incrementer = inc(regOut, incout)
    mux1 = mux2way(mux1out, 0, incout, increment)
    mux2 = mux2way(mux2out, mux1out, i, load)
    mux3 = mux2way(regIn, mux2out, 0, rst)

    @always_comb
    def comb():
        regLoad.next = rst or load or increment

        output.next = regOut

    return instances()


@block
def registerN(i, load, output, width, clk, rst):
    binaryDigitList = [None for n in range(width)]
    outputs = [Signal(bool(0)) for n in range(width)]

    for j in range(len(binaryDigitList)):
        binaryDigitList[j] = binaryDigit(i(j), load, outputs[j], clk, rst)

    @always_comb
    def comb():
        for k in range(len(outputs)):
            output.next[k] = outputs[k]

    return instances()


@block
def register8(i, load, output, clk, rst):
    binaryDigitList = [None for n in range(8)]
    output_n = [Signal(bool(0)) for n in range(8)]

    for j in range(len(binaryDigitList)):
        binaryDigitList[j] = binaryDigit(i(j), load, output_n[j], clk, rst)

    @always_comb
    def comb():
        for k in range(len(output_n)):
            output.next[k] = output_n[k]

    return instances()


@block
def binaryDigit(i, load, output, clk, rst):
    q, d, clear, presset = [Signal(bool(0)) for i in range(4)]

    flip_flop = dff(q, d, clear, presset, clk, rst)
    mux = mux2way(d, q, i, load)

    @always_comb
    def comb():
        output.next = q

    return instances()


@block
def dff(q, d, clear, presset, clk, rst):
    @always_seq(clk.posedge, reset=rst)
    def logic():
        if clear:
            q.next = 0
        elif presset:
            q.next = 1
        else:
            q.next = d

    return instances()
