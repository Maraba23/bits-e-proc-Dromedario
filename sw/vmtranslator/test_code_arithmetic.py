#!/usr/bin/env python3

from myhdl import bin
from bits import nasm_test, createDir
from .VMTranslate import VMTranslate
import os.path

SP = 0
STACK = 256
TEMP = {0: 5, 1: 6, 2: 7, 3:8, 4:9, 5:10, 6:11, 7:12}
TRUE = -1
FALSE = False

def abs_path(file):
    dir_test = os.path.dirname(__file__)
    return os.path.join(dir_test, file)

def vm_to_nasm(vm, nasm):
    createDir(nasm)
    fNasm = open(nasm, "w")
    v = VMTranslate(vm, fNasm)
    v.run()

def vm_test(vm, ram, test, time=10000):
    nasm = os.path.join("nasm", vm + ".nasm")
    vm_to_nasm(vm, nasm)
    return nasm_test(nasm, ram, test, time)

def test_add():
    x = 4; y = 8
    ram = {0: 258, 256: x, 257: y}
    tst = {0: 257, 256: x + y}
    assert vm_test(abs_path("test_assets/add.vm"), ram, tst)

def test_sub():
    x = 8; y = 4
    ram = {0: 258, 256: x, 257: y}
    tst = {0: 257, 256: x - y}
    assert vm_test(abs_path("test_assets/sub.vm"), ram, tst)

def test_orr():
    x = 8; y = 7
    ram = {0: 258, 256: x, 257: y}
    tst = {0: 257, 256: x | y}
    assert vm_test(abs_path("test_assets/or.vm"), ram, tst)

def test_andd():
    x = 8; y = 7
    ram = {0: 258, 256: x, 257: y}
    tst = {0: 257, 256: x & y}
    assert vm_test(abs_path("test_assets/and.vm"), ram, tst)

def test_nott():
    x = 8;
    ram = {0: 257, 256: x}
    tst = {0: 257, 256: ~x}
    assert vm_test(abs_path("test_assets/not.vm"), ram, tst)

def test_neg():
    x = 8;
    ram = {0: 257, 256: x}
    tst = {0: 257, 256: -x}
    assert vm_test(abs_path("test_assets/neg.vm"), ram, tst)

def test_eq_false():
    x = 8; y = 7
    ram = {0: 258, 256: x, 257: y}
    tst = {0: 257, 256: FALSE}
    assert vm_test(abs_path("test_assets/eq.vm"), ram, tst)

def test_eq_true():
    x = 8; y = 7
    ram = {0: 258, 256: x, 257: x}
    tst = {0: 257, 256: TRUE}
    assert vm_test(abs_path("test_assets/eq.vm"), ram, tst)

def test_gt_false():
    x = 8; y = 7
    ram = {0: 258, 256: y, 257: x}
    tst = {0: 257, 256: FALSE}
    assert vm_test(abs_path("test_assets/gt.vm"), ram, tst)

def test_gt_true():
    x = 8; y = 7
    ram = {0: 258, 256: x, 257: y}
    tst = {0: 257, 256: TRUE}
    assert vm_test(abs_path("test_assets/gt.vm"), ram, tst)

def test_lt_false():
    x = 8; y = 7
    ram = {0: 258, 256: x, 257: y}
    tst = {0: 257, 256: FALSE}
    assert vm_test(abs_path("test_assets/lt.vm"), ram, tst)

def test_lt_true():
    x = 8; y = 7
    ram = {0: 258, 256: y, 257: x}
    tst = {0: 257, 256: TRUE}
    assert vm_test(abs_path("test_assets/lt.vm"), ram, tst)
