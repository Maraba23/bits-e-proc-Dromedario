; Arquivo: stringLength.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi 
; Data: 28/03/2018
;
; Assuma que uma string é um conjunto de caracteres terminado
; em NULL (0).
; 
; Supondo que temos uma string que começa no endereço 8 da RAM.
; Calcule o seu tamanho e salve o resultado na RAM[0].
;
; Os caracteres estão formatados em ASCII
; http://sticksandstones.kstrom.com/appen.html
; 
; Exemplo:
;
;   Convertido para ASCII
;             |
;             v
;  RAM[8]  = `o`
;  RAM[9]  = `i`
;  RAM[10] = ` `
;  RAM[11] = `b`
;  RAM[12] =  l`
;  RAM[13] = `z`
;  RAM[14] = `?`
;  RAM[15] = NULL = 0x0000


Preparando:
    leaw $8, %A ; coloca 8 na RAM[1], que será contador de RAM
    movw %A, %D
    leaw $1, %A
    movw %D, (%A)

    leaw $0, %A ; coloca 0 na RAM[0]
    movw $0, (%A)


WHILE:
    leaw $1, %A
    movw (%A), %D ; pega o contador da RAM[1] e salva em D
    movw %D, %A
    movw (%A), %D ; pega o caracter que está na RAM[contador]

    leaw $END, %A
    je ; se o caracter for NULL, pula para o final
    nop

    leaw $0, %A ; pega o tamanho
    movw (%A), %D
    addw %D, $1, (%A)

    leaw $1, %A
    movw (%A), %D
    addw %D, $1, (%A)

    leaw $WHILE, %A
    jmp
    nop


END:
