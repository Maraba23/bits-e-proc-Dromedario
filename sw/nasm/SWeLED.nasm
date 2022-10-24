; Arquivo: SWeLED.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 28/3/2018
;
; Faça os LEDs exibirem 
; LED = OFF OFF OFF OFF OFF OFF OFF ON ON ON ON ON !SW3 !SW2 !SW1 0

; fluxo :
; sws = 010101011 - sw3 = 1 sw2 = 0 e sw1 = 1
; base = 111110000
; and entre sws e base = 010100000
; sub entre sws e (and result) = 000001011
; not do (sub result) = 111110100 - led3 = 0, led2 = 1 e led1 = 0

leaw $1008, %A
movw %A, %D
leaw $21185 , %A
andw (%A) , %D , %D
subw (%A) , %D , %D
notw %D

leaw $5 , %A
movw %D , (%A)

leaw $5, %A
movw (%A), %D

leaw $1, %A
andw %D, %A, %D

leaw $ELSE, %A
je
nop

leaw $0, %A
movw $1, (%A)
leaw $END, %A
jmp
nop

ELSE:
leaw $0, %A
movw $0, (%A)

END:


leaw $5 , %A
movw (%A) , %D
leaw $0 , %A
subw %D , (%A) , %A
movw %A , %D

leaw $21184, %A
movw %D, (%A)