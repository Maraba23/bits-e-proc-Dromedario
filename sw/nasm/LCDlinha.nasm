; Arquivo: LCDQuadrado.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 28/3/2018
;
; Desenhe uma linha no LCD

leaw $18763, %A     ; Endereco LCD
movw %A, %D
leaw $0, %A
movw %D, (%A)

leaw $20, %A        ; Contador Inicial
movw %A, %D
leaw $1, %A
movw %D, (%A)

WHILE:
    leaw $1, %A     ; Inicio do loop
    movw (%A), %D   ; Carrega 20 em D
    subw %D, 1, %D  ; Decrementa 1
    movw %D, (%A)   ; Salva o valor decrementado na memoria 1
    leaw $END, %A   ; Endereco de END
    je              ; Se o valor for 0 pula para END
    nop

    leaw $0, %A     ; Carrega endereco LCD em A
    movw (%A), %D   ; Carrega valor do LCD em D
    movw %D, %A     ; Salva valor do LCD em A
    movw $0, %D     ; Carrega 0 em D
    notw %D         ; Inverte D
    movw %D, (%A)   ; Salva o valor invertido no LCD

    leaw $0, %A     ; Carrega endereco LCD em A
    movw (%A), %D   ; Carrega valor do LCD em D
    addw %D, 1, %D  ; Incrementa 1
    movw %D, (%A)   ; Salva o valor incrementado no LCD

    leaw $WHILE, %A
    jmp
    nop

END: