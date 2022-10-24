; Arquivo: LCDQuadrado.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 28/3/2018
;
; Desenhe um quadro no LCD

; Desenhando a linha horizontal superior
leaw $0, %A
movw %A, %D
notw %D
leaw $18773, %A
movw %D, (%A)

; Desenhando a linha horizontal inferior
leaw $0, %A
movw %A, %D
notw %D
leaw $19088, %A
movw %D, (%A)

; Desenhando as linhas verticais
leaw $32769, %A
movw %A, %D
leaw $2, %A
movw %D, (%A)

leaw $18794, %A
movw %A, %D
leaw $1, %A
movw %D, (%A)

WHILE:
    leaw $1, %A
    movw (%A), %D
    leaw $19088, %A
    subw %A, %D, %D
    leaw $END, %A
    je
    nop

    leaw $2, %A
    movw (%A), %D

    leaw $1, %A
    movw %D, (%A)

    movw (%A), %D
    addw %D, $21, %D
    movw %D, (%A)

    leaw $WHILE, %A
    jmp
    nop

END: