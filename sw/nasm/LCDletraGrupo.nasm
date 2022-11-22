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
leaw $19093, %A
movw %D, (%A)

; Desenhando as linhas verticais
leaw $15, %A
movw %A, %D
leaw $1, %A
movw %D, (%A)

leaw $18793, %A     ; Endereco LCD
movw %A, %D
leaw $0, %A
movw %D, (%A)


WHILE:
leaw $1, %A
movw (%A), %D
leaw $END, %A
je
nop

leaw $32769, %A
movw %A, %D
leaw $0, %A
movw (%A), %A
movw %D, (%A)

leaw $0, %A
movw (%A), %D
leaw $20, %A
addw %D, %A, %D
leaw $0, %A
movw %D, (%A)

leaw $1, %A
movw (%A), %D
subw %D, $1, %D
movw %D, (%A)

leaw $WHILE, %A
jmp
nop

END:

; Desenhando perna do D
leaw $16, %A
movw %A, %D
leaw $1, %A
movw %D, (%A)

leaw $18453, %A     ; Endereco LCD
movw %A, %D
leaw $0, %A
movw %D, (%A)

WHILEI:
leaw $1, %A
movw (%A), %D
leaw $ENDI, %A
je
nop

leaw $1, %A
movw %A, %D
leaw $0, %A
movw (%A), %A
movw %D, (%A)

leaw $0, %A
movw (%A), %D
leaw $20, %A
addw %D, %A, %D
leaw $0, %A
movw %D, (%A)

leaw $1, %A
movw (%A), %D
subw %D, $1, %D
movw %D, (%A)

leaw $WHILEI, %A
jmp
nop

ENDI: