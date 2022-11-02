

class Code:
    def __init__(self):
        """
        Se precisar faca uso de variáveis.
        """
        pass

    # DONE
    def dest(self, mnemnonic):
        """
        Retorna o código binário do(s) registrador(es) que vão receber o valor da instrução.
        - in mnemnonic: vetor de mnemônicos "instrução" a ser analisada.
        - return bits: String de 4 bits com código em linguagem de máquina
          que define o endereco da operacao
        """

        dests = {
            "%A": "001",
            "%D": "010",
            "(%A)": "100",
            "%D%A": "011",
            "%A%D": "011",
            "(%A)%A": "101",
            "%A(%A)": "101",
            "(%A)%D": "110",
            "%D(%A)": "110",
            "(%A)%D%A": "111",
        }

        if mnemnonic[0] == 'movw':
            if len(mnemnonic) == 3:
                bits = dests[mnemnonic[-1]]
            elif len(mnemnonic) == 4:
                bits = dests[f'{mnemnonic[-2]}{mnemnonic[-1]}']
            elif len(mnemnonic) == 5:
                bits = dests["(%A)%D%A"]
        elif mnemnonic[0] in ['addw', 'subw', 'rsubw', 'andw', 'orw']:
            if len(mnemnonic) == 4:
                bits = dests[mnemnonic[-1]]
            elif len(mnemnonic) == 5:
                bits = dests[f'{mnemnonic[-2]}{mnemnonic[-1]}']
            elif len(mnemnonic) == 6:
                bits = dests["(%A)%D%A"]
        elif mnemnonic[0] in ['incw', 'decw', 'notw', 'negw']:
            bits = dests[mnemnonic[-1]]
        else:
            bits = "000"

        return bits

    # TODO
    def comp(self, mnemnonic):
        """
        Retorna o código binário do mnemônico para realizar uma operação de cálculo.
        - in mnemnonic: vetor de mnemônicos "instrução" a ser analisada.
        - return bits:  Opcode (String de 7 bits) com código em linguagem de máquina para a instrução.
        """

        bits = "000000"
        return bits

    # DONE
    def jump(self, mnemnonic):
        """
        Retorna o código binário do mnemônico para realizar uma operação de jump (salto).
        - in mnemnonic: vetor de mnemônicos "instrução" a ser analisada.
        - return bits: (String de 3 bits) com código em linguagem de máquina para a instrução.
        """
        jumps = {
            'jg': '001',
            'je': '010',
            'jge': '011',
            'jl': '100',
            'jne': '101',
            'jle': '110',
            'jmp': '111'
        }

        if mnemnonic[0] in jumps:
            bits = jumps[mnemnonic[0]]
        else:
            bits = "000"
        
        return bits

    # DONE
    def toBinary(self, value):
        """
        Converte um valor inteiro para binário 16 bits.
        """
        return f"{int(value):016b}"
