; Arquivo: Abs.nasm
; Curso: Elementos de Sistemas
; Criado por: Luciano Soares
; Data: 27/03/2017

; Multiplica o valor de RAM[1] com RAM[0] salvando em RAM[3]
; Assuma valores inteiros


Preparando:
    leaw $3, %A
    movw $0, (%A)


WHILE:
    leaw $0, %A
    movw (%A), %D
    leaw $END, %A
    je
    nop


    leaw $1, %A ; soma
    movw (%A), %D
    leaw $3, %A
    addw (%A), %D, %D
    movw %D, (%A)

    leaw $0, %A ; decresce 1 do contador
    subw (%A), $1, %D
    movw %D, (%A)



    leaw $WHILE, %A
    jmp
    nop


END: