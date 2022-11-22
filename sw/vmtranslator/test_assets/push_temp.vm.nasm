;; push temp 5 - 1
leaw $5, %A
incw %A
incw %A
incw %A
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
;; push temp 7 - 2
leaw $5, %A
incw %A
incw %A
incw %A
incw %A
incw %A
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
