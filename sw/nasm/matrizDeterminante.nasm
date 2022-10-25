; Arquivo: matrizDeterminante.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 03/2019
;
; Calcula o determinante de uma matriz 2x2 (RAM[1000]) e
;  salva seu resultado no endereço RAM[0]
;
; Calcula o determinante de uma matriz 2x2 (RAM[1000]) na forma
; [ a0, a1 ]
; [ b0, b1 ]
;
; Salva o resultado no endereço RAM[0]
;
; A matriz é salva na memória da seguinte maneira:
; RAM[1000] = a0
; RAM[1001] = a1
; RAM[1003] = b0
; RAM[1004] = b1


Preparando:
    leaw $1, %A 
    movw $0, (%A) ; salva 0 em RAM[1]
    leaw $2, %A
    movw $0, (%A) ; salva 0 em RAM[2]


; Step 1: multiplica a0 e b1

WHILE:
    leaw $1000, %A
    movw (%A), %D
    leaw $END, %A
    je
    nop


    leaw $1004, %A ; soma
    movw (%A), %D
    leaw $1, %A
    addw (%A), %D, %D
    movw %D, (%A)


    leaw $1000, %A ; decresce 1 do contador
    subw (%A), $1, %D
    movw %D, (%A)


    leaw $WHILE, %A
    jmp
    nop


END:


; Step 2: multiplica a1 e b0

WHILE2:
    leaw $1001, %A
    movw (%A), %D
    leaw $END2, %A
    je
    nop


    leaw $1003, %A ; soma
    movw (%A), %D
    leaw $2, %A
    addw (%A), %D, %D
    movw %D, (%A)


    leaw $1001, %A ; decresce 1 do contador
    subw (%A), $1, %D
    movw %D, (%A)


    leaw $WHILE2, %A
    jmp
    nop


END2:


; Step 3: subtrai os valores de RAM[1] - RAM[2]

leaw $1, %A
movw (%A), %D
leaw $2, %A
subw %D, (%A), %D
leaw $0, %A ; salva o resultado do determinante em RAM[0]
movw %D, (%A)