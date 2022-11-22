; Arquivo: SWeLED2.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
;
; Faça os LEDs exibirem 
; LED = SW[8] !SW[7] OFF ON ON RAM[5][3] ON SW[0] OFF
;
;                                ^            ^
;                                | TRUQUE!    | TRUQUE!

; 0000000000110100 - LED padrão

Preparando:
    leaw $52, %A
    movw %A, %D
    leaw $0, %A
    movw %D, (%A)


SW0:
    leaw $21185, %A
    movw (%A), %D

    leaw $1, %A
    andw %D, %A, %D     ; faz AND do SW[0] com 1

    subw %D, %A, %D     ; se o resultado do AND for 1, soma 2 no vetor dos leds (RAM[0])
    leaw $SW7, %A
    jne
    nop

    leaw $2, %A
    movw %A, %D
    leaw $0, %A
    addw (%A), %D, %D
    movw %D, (%A)


SW7:
    leaw $21185, %A
    movw (%A), %D
    
    leaw $128, %A
    andw %A, %D, %D     ; faz AND do SW[7] com 128 (2**7)

    subw %D, %A, %D     ; se o resultado do and for 128, skip o bloco
    leaw $SW8, %A
    je
    nop

    leaw $128, %A
    movw %A, %D
    leaw $0, %A
    addw (%A), %D, %D
    movw %D, (%A)


SW8:
    leaw $21185, %A
    movw (%A), %D

    leaw $256, %A
    andw %A, %D, %D     ; faz AND do SW[8] com 256 (2**8)

    subw %D, %A, %D     ; se o resultado do AND for 256, ele acende o LED
    leaw $SEGUE, %A
    jne
    nop

    leaw $256, %A
    movw %A, %D
    leaw $0, %A
    addw (%A), %D, %D
    movw %D, (%A)


SEGUE:
    leaw $5, %A
    movw (%A), %D

    leaw $8, %A
    andw %D, %A, %D     ; faz AND do bit 3 da RAM[5] com 8 (2**3)

    subw %D, %A, %D     ; se o resultado do AND for 8, ele acende o LED
    leaw $END, %A
    jne
    nop

    leaw $8, %A
    movw %A, %D
    leaw $0, %A
    addw (%A), %D, %D
    movw %D, (%A)


END:
    leaw $0, %A
    movw (%A), %D
    leaw $21184, %A
    movw %D, (%A)
