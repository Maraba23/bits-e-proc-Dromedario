; Arquivo: isEven.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 28/3/2019
;
; Verifica se o valor salvo no endereço RAM[5] é
; par. Se for verdadeiro, salva 1
; em RAM[0] e 0 caso contrário.

Preparando:
    leaw $0, %A                                                   ; carrega const 0 em A
    movw $0, (%0)                                                 ; troca RAM[0] para 0

WHILE:
    leaw $5, %A                                                   ; carrega const 5 em A
    movw (%A), %D                                                 ; copia RAM[5] para D
    leaw $ENDWHILE, %A                                            ; carrega endereco de ENDWHILE em A
    jle %A                                                        ; se RAM[0] <= 0, pula para ENDWHILE
    nop

    leaw $5, %A                                                   ; carrega const 5 em A
    movw (%A), %D                                                 ; copia RAM[5] para D
    leaw $2, %A                                                   ; carrega const 2 em A
    subw D, %A, %D                                                ; subtrai 2 de RAM[5] e armazena em D
    movw %D, (%A)                                                 ; copia D para RAM[0]

    leaw $WHILE, %A                                               ; carrega endereco de WHILE em A
    jmp %A                                                        ; pula para WHILE
    nop

ENDWHILE:

leaw $0, %A                                                       ; carrega const 0 em A
movw (%A), %D                                                     ; carrega RAM[0] em D
leaw $END, %A                                                     ; carrega endereco de END em A
jl %A                                                             ; se RAM[0] < 0, pula para END
nop

leaw $0, %A                                                       ; carrega const 1 em A
movw $1, (%A)                                                     ; carrega 1 em RAM[1]

END:
