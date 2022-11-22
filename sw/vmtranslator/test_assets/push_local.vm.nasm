;; push local 0 - 1
leaw $LCL, %A
movw (%A), %A
movw (%A), %D
leaw $SP, %A
movw (%A), %A
movw %D, (%A)
incw %A
movw %A, %D
leaw $SP, %A
movw %D, (%A)
;; push local 2 - 2
leaw $LCL, %A
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
