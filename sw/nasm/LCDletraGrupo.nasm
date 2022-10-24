; Arquivo: LCDletraGrupo.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 28/3/2018
;
; Escreva no LCD a letra do grupo de vocês
;  - Valide no hardawre
;  - Bata uma foto!

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
    leaw $ENDI, %A
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

ENDI:

; Desenhando linha vertical superior
leaw $1, %A
movw %A, %D
leaw $2, %A
movw %D, (%A)

leaw $18416, %A
movw %A, %D
leaw $1, %A
movw %D, (%A)

WHILE:
    leaw $1, %A
    movw (%A), %D
    leaw $18773, %A
    subw %A, %D, %D
    leaw $ENDII, %A
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

ENDII: