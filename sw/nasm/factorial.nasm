; Arquivo: Factorial.nasm
; Curso: Elementos de Sistemas
; Criado por: Luciano Soares
; Data: 27/03/2017

; Calcula o fatorial do número em R0 e armazena o valor em R1.

PREPARANDO:
    leaw $1, %A                     ; Joga 1 em A
    movw %A, %D                     ; Move 1 pra D
    movw %D, (%A)                   ; Move D pra RAM[1]

VAI:
    leaw $0, %A                     ; jogo 0 em A
    movw (%A), %D                   ; jogo RAM[0] em D
    leaw $2, %A                     ; jogo 2 em A
    subw %D, (%A), %D               ; subtari o valor de RAM[0] por RAM[2] (RAM[0] - RAM[2]) guarda valor em D
    leaw $END, %A
    je
    nop 

    leaw $2, %A                     ; Joga 2 em A
    movw (%A), %D                   ; Move RAM[2] pra D
    leaw $1, %A                     ; Joga 1 em A
    addw %D, %A, %D                 ; RAM[2] ++
    leaw $2, %A                     ; Joga 2 em A
    movw %D, (%A)                   ; Move D pra RAM[2]
    leaw $1, %A                     ; joga 1 em A
    movw %A, %D                     ; Joga 1 em D
    leaw $4, %A                     ; Joga 4 em A
    movw %D, (%A)                   ; RAM[4] == D
    leaw $1, %A                     ; Joga 1 em A
    movw (%A), %D                   ; Move RAM[1] pra D
    leaw $3, %A                     ; Joga 3 pra A
    movw %D, (%A)                   ; Move RAM[1] pra RAM[3]

CONTINUA:
    leaw $2, %A                     ; Joga 2 em A
    movw (%A), %D                   ; Joga RAM[2] em D
    leaw $4, %A                     ; Joga 4 em A
    subw %D, (%A), %D               ; Subtrai RAM[2] - RAM[4]
    leaw $VAI, %A
    je
    nop

    leaw $1, %A                     ; Joga 1 em A
    movw %A, %D                     ; Move 1 pra D
    leaw $4, %A                     ; Joga 4 em A
    movw (%A), %D                   ; Move RAM[4] pra D
    leaw $1, %A                     ; Joga 1 em A
    addw %D, %A,%D                  ; RAM[4] ++
    leaw $4, %A                     ; Joga 4 em A
    movw %D, (%A)                   ; Move D pra RAM[4]
    leaw $1, %A                     ; Joga 1 em A
    movw (%A), %D                   ; Move RAM[1] para D
    leaw $3, %A                     ; Joga 3 em A
    addw %D, (%A), %D               ; Adiciona em D o valor de D (RAM[1] + RAM[3])
    leaw $1, %A                     ; Joga 1 em A
    movw %D, (%A)                   ; Move valor de D pra RAM[1]
    leaw $CONTINUA, %A
    jmp
    nop

END: