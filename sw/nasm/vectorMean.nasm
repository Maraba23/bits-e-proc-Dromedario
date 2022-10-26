; ------------------------------------
; Calcule a média dos valores de um vetor
; que possui inicio em RAM[5] e tamanho
; defindo em RAM[4],
;
; 1. Salve a soma em RAM[1]
; 2. Salve a média em RAM[0]
; 
; ------------------------------------
; antes       | depois
;             |
; RAM[0]:     | RAM[0]:  2  : média 
; RAM[1]:     | RAM[1]:  8  : soma
; RAM[2]:     | RAM[2]:  
; RAM[3]:     | RAM[3]:  
; RAM[4]:  4  | RAM[4]:  4 
; RAM[5]:  1  | RAM[5]:  1 - 
; RAM[6]:  2  | RAM[6]:  2 | vetor
; RAM[7]:  1  | RAM[7]:  1 |
; RAM[8]:  4  | RAM[8]:  4 -
; ------------------------------------


PREPARANDO:
    leaw $2, %A
    movw $0, (%A) ; cria contador em RAM[2]


SOMA:
    leaw $2, %A
    movw (%A), %D
    leaw $4, %A
    subw %D, (%A), %D
    leaw $SEGUE, %A
    je
    nop


    leaw $2, %A
    movw (%A), %D
    leaw $5, %A
    addw %D, %A, %A
    movw (%A), %D
    leaw $1, %A
    addw (%A), %D, %D
    movw %D, (%A)


    leaw $2, %A
    addw $1, (%A), %D
    movw %D, (%A)


    leaw $SOMA, %A
    jmp
    nop


SEGUE:
    leaw $1, %A
    movw (%A), %D
    leaw $3, %A
    movw %D, (%A) ; cria cópia da soma para poder fazer divisão


DIV:
    leaw $3, %A
    movw (%A), %D
    leaw $END, %A
    jle
    nop


    leaw $4, %A
    movw (%A), %D
    leaw $3, %A
    subw (%A), %D, %D
    movw %D, (%A)


    leaw $0, %A
    addw (%A), $1, %D
    movw %D, (%A)


    leaw $DIV, %A
    jmp
    nop


END: