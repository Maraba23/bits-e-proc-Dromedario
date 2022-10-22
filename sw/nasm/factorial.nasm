; Arquivo: Factorial.nasm
; Curso: Elementos de Sistemas
; Criado por: Luciano Soares
; Data: 27/03/2017

; Calcula o fatorial do número em R0 e armazena o valor em R1.

PREPARANDO:
    leaw $0, %A
    movw (%A), %D

    leaw $NULO, %A
    je %D
    nop

    leaw $1, %A
    subw %D, %A, %D
    leaw $NULO, %A
    je %D
    nop

VAI:
    leaw $0, %A
    movw (%A), %D
    leaw $2, %A
    subw %D, (%A), %D
    leaw $END, %A
    jl %D
    nop 

    leaw $2, %A
    incw (%A)
    leaw $1, %A
    movw %A, %D
    leaw $4, %A
    movw %D, (A%)

CONTINUA:
    leaw $2, %A
    movw (%A), %D
    leaw $4, %A
    subw %D, (%A), %D
    leaw $VAI, %A
    je %D
    nop

    incw (%A)
    leaw $1, %A
    movw (%A), %D
    leaw $2, %A
    addw %D, (%A), %D
    leaw $1, %A
    movw %D, (%A)
    leaw $CONTINUA, %A
    jmp
    nop

NULO:
    leaw $1, %A
    incw (%A)

END: