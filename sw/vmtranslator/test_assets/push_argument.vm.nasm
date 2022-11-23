;; push argument 0 - 1
leaw $ARG, %A
movw (%A), %A
movw (%A), %D
leaw $SP, %A
movw (%A), %A
movw %D, (%A)
incw %A
movw %A, %D
leaw $SP, %A
movw %D, (%A)
;; push argument 2 - 2
leaw $ARG, %A
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
