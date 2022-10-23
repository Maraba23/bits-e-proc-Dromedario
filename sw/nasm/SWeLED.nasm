; Arquivo: SWeLED.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 28/3/2018
;
; Faça os LEDs exibirem 
; LED = OFF OFF OFF OFF OFF OFF OFF ON ON ON ON ON !SW3 !SW2 !SW1 0

leaw $496, %A ;
movw %A, %D ; vetor da base

leaw $21185 , %A ; vetor das switchs
andw (%A) , %D , %D
subw (%A) , %D , %D ;
notw %D ;
leaw $5 , %A
movw %D , (%A) ; até aki td certo

; fazer a operação é_par com D.
; subtrair not(é_par) do valor armazenado na R[5] e mover esse valor para %D

leaw $21184, %A ; localiza os leds
movw %D, (%A) ; liga os leds


; fluxo :
; sws = 010101011 - sw3 = 1 sw2 = 0 e sw1 = 1
; base = 111110000
; and entre sws e base = 010100000
; sub entre sws e (and result) = 000001011
; not do (sub result) = 111110100 - led3 = 0, led2 = 1 e led1 = 0

