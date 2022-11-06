#!/usr/bin/env python3

from myhdl import bin
from bits import nasm_test
import os.path
import math


def text_to_ram(text, offset=0):
    ram = {}
    for i in range(len(text)):
        ram[i + offset] = ord(text[i])
    return ram


def test_abs():
    ram = {1: -1}
    tst = {0: 1}
    assert nasm_test("abs.nasm", ram, tst)

    ram = {1: 35}
    tst = {0: 35}
    assert nasm_test("abs.nasm", ram, tst)


def test_max():
    ram = {0: 35, 1: 7}
    tst = {2: 35}
    assert nasm_test("max.nasm", ram, tst)

    ram = {0: 7, 1: 63}
    tst = {2: 63}
    assert nasm_test("max.nasm", ram, tst)


def test_mult():
    ram = {0: 2, 1: 2}
    tst = {3: 4}
    assert nasm_test("mult.nasm", ram, tst)

    ram = {0: 32, 1: 16}
    tst = {3: 512}
    assert nasm_test("mult.nasm", ram, tst, 10000)


def test_mod():
    ram = {0: 0, 1: 0}
    tst = {2: 0}
    assert nasm_test("mod.nasm", ram, tst)

    ram = {0: 0, 1: 5}
    tst = {2: 0}
    assert nasm_test("mod.nasm", ram, tst)

    ram = {0: 32, 1: 5}
    tst = {2: 2}
    assert nasm_test("mod.nasm", ram, tst, 10000)

    ram = {0: 1023, 1: 7}
    tst = {2: 1}
    assert nasm_test("mod.nasm", ram, tst, 10000)


def test_div():
    ram = {0: 0, 1: 5}
    tst = {2: 0}
    assert nasm_test("div.nasm", ram, tst)

    ram = {0: 4, 1: 2}
    tst = {2: 2}
    assert nasm_test("div.nasm", ram, tst)

    ram = {0: 30, 1: 5}
    tst = {2: 6}
    assert nasm_test("div.nasm", ram, tst, 10000)

    ram = {0: 46, 1: 5}
    tst = {2: 9}
    assert nasm_test("div.nasm", ram, tst, 10000)

    ram = {0: 1023, 1: 7}
    tst = {2: 146}
    assert nasm_test("div.nasm", ram, tst, 10000)


def test_isEven():
    ram = {0: 2, 5: 64}
    tst = {0: 1}
    assert nasm_test("isEven.nasm", ram, tst)

    ram = {0: 2, 5: 1023}
    tst = {0: 0}
    assert nasm_test("isEven.nasm", ram, tst)


def test_pow():
    ram = {0: 2, 1: 0}
    tst = {0: 0}
    assert nasm_test("pow.nasm", ram, tst)

    ram = {1: 2}
    tst = {0: 4}
    assert nasm_test("pow.nasm", ram, tst)

    ram = {1: 16}
    tst = {0: 256}
    assert nasm_test("pow.nasm", ram, tst, 10000)


def test_stringLenght():
    ram = {}
    text = "oi tudo bem?"
    ram = text_to_ram(text, 8)
    tst = {0: len(text)}
    assert nasm_test("stringLength.nasm", ram, tst, 10000)

    text = "o saci eh um ser muito especial"
    ram = text_to_ram(text, 8)
    tst = {0: len(text)}
    assert nasm_test("stringLength.nasm", ram, tst, 10000)


def test_palindromo():
    ram = text_to_ram("ararr", 10)
    ram[0] = 2
    tst = {0: 0}
    assert nasm_test("palindromo.nasm", ram, tst, 10000)

    ram = text_to_ram("arara", 10)
    ram[0] = 2
    tst = {0: 1}
    print(ram)
    assert nasm_test("palindromo.nasm", ram, tst, 10000)


def test_linha():
    ram = {}
    tst = {}
    nasm_test("LCDlinha.nasm", ram, tst, 10000)


def test_quadrado():
    ram = {}
    tst = {}
    nasm_test("LCDquadrado.nasm", ram, tst, 10000)


def test_letra():
    ram = {}
    tst = {}
    nasm_test("LCDletraGrupo.nasm", ram, tst, 10000)


def test_factorial():
    ram = {0: 0}
    tst = {1: math.factorial(ram[0])}
    assert nasm_test("factorial.nasm", ram, tst, 10000)

    ram = {0: 1}
    tst = {1: math.factorial(ram[0])}
    assert nasm_test("factorial.nasm", ram, tst, 10000)

    ram = {0: 2}
    tst = {1: math.factorial(ram[0])}
    assert nasm_test("factorial.nasm", ram, tst, 10000)

    ram = {0: 3}
    tst = {1: math.factorial(ram[0])}
    assert nasm_test("factorial.nasm", ram, tst, 10000)

    ram = {0: 4}
    tst = {1: math.factorial(ram[0])}
    assert nasm_test("factorial.nasm", ram, tst, 10000)

    ram = {0: 5}
    tst = {1: math.factorial(ram[0])}
    assert nasm_test("factorial.nasm", ram, tst, 10000)
    

def test_SWeLED():
    ram = {21185: 4}
    tst = {21184: 65530}

    assert nasm_test("SWeLED.nasm", ram, tst, 10000)

    ram = {21185: 12}
    tst = {21184: 65522}

    assert nasm_test("SWeLED.nasm", ram, tst, 10000)

    ram = {21185: 14}
    tst = {21184: 65520}

    assert nasm_test("SWeLED.nasm", ram, tst, 10000)

    ram = {21185: 416}
    tst = {21184: 65534}

    assert nasm_test("SWeLED.nasm", ram, tst, 10000)

    ram = {21185: 165}
    tst = {21184: 65530}

    assert nasm_test("SWeLED.nasm", ram, tst, 10000)

    ram = {0: 8}
    tst = {1: math.factorial(ram[0])}
    assert nasm_test("factorial.nasm", ram, tst, 10000)


def test_multiploDeDois():
    ram = {5: 4}
    tst = {0: 1}
    assert nasm_test("multiploDeDois.nasm", ram, tst, 10000)

    ram = {5: 5}
    tst = {0: 0}
    assert nasm_test("multiploDeDois.nasm", ram, tst, 10000)

    ram = {5: -4}
    tst = {0: 1}
    assert nasm_test("multiploDeDois.nasm", ram, tst, 10000)


def test_matrizDeterminante():
    ram = {1000: 3, 1001: 3, 1003: 1, 1004: 2}
    tst = {0: 3}
    assert nasm_test("matrizDeterminante.nasm", ram, tst, 10000)

    ram = {1000: 2, 1001: 2, 1003: 3, 1004: 4}
    tst = {0: 2}
    assert nasm_test("matrizDeterminante.nasm", ram, tst, 10000)


def test_vectorMean():
    ram = {4:4, 5:1, 6:2, 7:1, 8:8}
    tst = {0:3, 1:12}

    assert nasm_test("vectorMean.nasm", ram, tst, 10000)


def test_SWeLED():
    ram = {21185: 4}
    tst = {21184: 65530}

    assert nasm_test("SWeLED.nasm", ram, tst, 10000)

    ram = {21185: 12}
    tst = {21184: 65522}

    assert nasm_test("SWeLED.nasm", ram, tst, 10000)

    ram = {21185: 14}
    tst = {21184: 65520}

    assert nasm_test("SWeLED.nasm", ram, tst, 10000)

    ram = {21185: 416}
    tst = {21184: 65534}

    assert nasm_test("SWeLED.nasm", ram, tst, 10000)

    ram = {21185: 165}
    tst = {21184: 65530}

    assert nasm_test("SWeLED.nasm", ram, tst, 10000)


def test_SWeLED2():
    ram = {5: 24, 21185: 409} # 0000000110011001 -> SWs // 0000000000011000 -> RAM[5]
    tst = {21184: 318} # 0000000100111110 -> LEDs

    assert nasm_test("SWeLED2.nasm", ram, tst, 10000)

    ram = {5: 23, 21185: 24} # 0000000000011000 -> SWs // 0000000000010111 -> RAM[5]
    tst = {21184: 180} # 0000000010110100 -> LEDs

    assert nasm_test("SWeLED2.nasm", ram, tst, 10000)