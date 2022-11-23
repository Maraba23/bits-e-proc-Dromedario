;; push pointer 0 - 1
leaw $THIS, %A
movw (%A), %D
leaw $SP, %A
movw (%A), %A
movw %D, (%A)
incw %A
movw %A, %D
leaw $SP, %A
movw %D, (%A)
;; push pointer 1 - 2
leaw $THAT, %A
movw (%A), %D
leaw $SP, %A
movw (%A), %A
movw %D, (%A)
incw %A
movw %A, %D
leaw $SP, %A
movw %D, (%A)
