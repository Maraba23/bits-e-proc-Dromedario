; Arquivo: Abs.nasm
; Curso: Elementos de Sistemas
; Criado por: Luciano Soares
; Data: 27/03/2017

; Copia o valor de RAM[1] para RAM[0] deixando o valor sempre positivo.

Preparando:
    leaw $1, %A
    movw (%A), %D


leaw $ELSE, %A; checa se é positivo
jl
nop

leaw $0, %A
movw %D, (%A)
leaw $END, %A
jmp
nop

ELSE:
    negw %D; faz complemento de 2 do número
    leaw $0, %A
    movw %D, (%A)

END: