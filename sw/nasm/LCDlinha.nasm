; Arquivo: LCDQuadrado.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 28/3/2018
;
; Desenhe uma linha no LCD

leaw $18763, %A
movw %A, %D
leaw $1, %A
movw %D, (%A)

leaw $0, %A
movw %A, %D
notw %D

leaw $2, %A
movw %D, (%A)

WHILE:
    leaw $1, %A
    movw (%A), %D
    leaw $18783, %A
    subw %A, %D, %D
    leaw $END, %A
    je
    nop

    leaw $2, %A
    movw (%A), %D

    leaw $1, %A
    movw %D, (%A)

    movw (%A), %D
    addw %D, $1, %D
    movw %D, (%A)

    leaw $WHILE, %A
    jmp
    nop


END: