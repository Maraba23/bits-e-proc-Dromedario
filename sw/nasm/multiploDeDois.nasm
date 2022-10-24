; Arquivo: multiploDeDois.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 28/3/2019
;
; Verifica se o valor salvo no endereço RAM[5] é
; multiplo de dois, se for verdadeiro, salva 1
; em RAM[0] e 0 caso contrário.


leaw $5, %A
movw (%A), %D
leaw $1, %A
andw %D, %A, %D ; faz and com 1

leaw $ELSE, %A
je
nop

leaw $0, %A
movw $0, (%A)
leaw $END, %A
jmp
nop

ELSE:
    leaw $0, %A
    movw $1, (%A)


END: