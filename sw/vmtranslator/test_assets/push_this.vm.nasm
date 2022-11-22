;; push this 0 - 1
leaw $THIS, %A
movw (%A), %A
movw (%A), %D
leaw $SP, %A
movw (%A), %A
movw %D, (%A)
incw %A
movw %A, %D
leaw $SP, %A
movw %D, (%A)
;; push this 2 - 2
leaw $THIS, %A
movw (%A), %A
incw %A
incw %A
movw (%A), %D
leaw $SP, %A
movw (%A), %A
movw %D, (%A)
incw %A
movw %A, %D
leaw $SP, %A
movw %D, (%A)
