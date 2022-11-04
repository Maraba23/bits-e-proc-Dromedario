#!/usr/bin/env python3

import os
from .ASMparser import Parser

dir_test = os.path.dirname(__file__)
MULT_NASM = os.path.join(dir_test, 'test_assets/mult.nasm')
SYMBOL_NASM = os.path.join(dir_test, 'test_assets/symbol.nasm')
LABOL_NASM = os.path.join(dir_test, 'test_assets/labol.nasm')


def test_advanced():
    fnasm = open(MULT_NASM, 'r')
    ptest = Parser(fnasm)

    assert ptest.advanced() is True
    assert ptest.command() == ['leaw', '$3', '%A']

    assert ptest.advanced() is True
    assert ptest.command() == ['movw', '$0', '(%A)']

    assert ptest.advanced() is True
    assert ptest.command() == ['loop:']

    assert ptest.advanced() is True
    assert ptest.command() == ['leaw', '$0', '%A']

    assert ptest.advanced() is True
    assert ptest.command() == ['movw', '(%A)', '%D']

    assert ptest.advanced() is True
    assert ptest.command() == ['end:']

    assert ptest.advanced() is False


def test_commandType():
    fnasm = open(MULT_NASM, 'r')
    ptest = Parser(fnasm)

    ptest.currentCommand = ['leaw', '$2', '%A']
    assert ptest.commandType() == ptest.CommandType['A']

    ptest.currentCommand = ['movw', '$1', '%A']
    assert ptest.commandType() == ptest.CommandType['C']

    ptest.currentCommand = ['WHILE:']
    assert ptest.commandType() == ptest.CommandType['L']

    ptest.currentCommand = ['leaw', '$31', '%A']
    assert ptest.commandType() == ptest.CommandType['A']

    ptest.currentCommand = ['addw', '%D', '%A', '%D']
    assert ptest.commandType() == ptest.CommandType['C']

    ptest.currentCommand = ['rsubw', '%D', '%A', '%D']
    assert ptest.commandType() == ptest.CommandType['C']

    ptest.currentCommand = ['negw', '%D']
    assert ptest.commandType() == ptest.CommandType['C']

    ptest.currentCommand = ['subw', '%D', '%A', '(%A']
    assert ptest.commandType() == ptest.CommandType['C']

    ptest.currentCommand = ['jmp']
    assert ptest.commandType() == ptest.CommandType['C']

    ptest.currentCommand = ['label:']
    assert ptest.commandType() == ptest.CommandType['L']

    ptest.currentCommand = ['leaw', '$32796', '%A']
    assert ptest.commandType() == ptest.CommandType['A']



def test_symbol():
    fnasm = open(SYMBOL_NASM, 'r')
    ptest = Parser(fnasm)

    assert ptest.advanced() is True
    assert ptest.symbol() == '1'

    assert ptest.advanced() is True
    assert ptest.symbol() == '3'

    assert ptest.advanced() is True
    assert ptest.symbol() == '45'

    assert ptest.advanced() is False


def test_labol():
    fnasm = open(LABOL_NASM, 'r')
    ptest = Parser(fnasm)

    assert ptest.advanced() is True
    assert ptest.label() == 'OI'

    assert ptest.advanced() is True
    assert ptest.advanced() is True
    assert ptest.label() == 'END'

    assert ptest.advanced() is True

    assert ptest.advanced() is True
    assert ptest.label() == 'WHILE_1'

    assert ptest.advanced() is True
    assert ptest.advanced() is False
