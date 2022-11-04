

class Code:
    def __init__(self):

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
        if mnemnonic[0] == 'movw':
            if '$0' == mnemnonic[1]:
                bits = '0101010'
            elif '$1' == mnemnonic[1]:
                bits = '0111111'
            elif '$-1' == mnemnonic[1]:
                bits = '0111010'
            elif mnemnonic[1] == '%D':
                bits = '0001100'
            elif mnemnonic[1] == '%A':
                bits = '0110000'
            elif mnemnonic[1] == '(%A)':
                bits = '1110000'
        elif mnemnonic[0] == 'notw':
            if mnemnonic[1] == '%D':
                bits = '0001101'
            elif mnemnonic[1] == '%A':
                bits = '0110001'
            elif mnemnonic[1] == '(%A)':
                bits = '1110001'
        elif mnemnonic[0] == 'negw':
            if mnemnonic[1] == '%D':
                bits = '0001111'
            elif mnemnonic[1] == '%A':
                bits = '0110011'
            elif mnemnonic[1] == '(%A)':
                bits = '1110011'
        elif mnemnonic[0] == 'incw':
            if mnemnonic[1] == '%D':
                bits = '0011111'
            elif mnemnonic[1] == '%A':
                bits = '0110111'
            elif mnemnonic[1] == '(%A)':
                bits = '1110111'
        elif mnemnonic[0] == 'decw':
            if mnemnonic[1] == '%D':
                bits = '0001110'
            elif mnemnonic[1] == '%A':
                bits = '0110010'
            elif mnemnonic[1] == '(%A)':
                bits = '1110010'
        elif mnemnonic[0] == 'addw':
            if '$1' in mnemnonic:
                if mnemnonic[1] == '%D' or mnemnonic[2] == '%D':
                    bits = '0011111'
                elif mnemnonic[1] == '%A' or mnemnonic[2] == '%A':
                    bits = '0110111'
                elif mnemnonic[1] == '(%A)' or mnemnonic[2] == '(%A)':
                    bits = '1110111'
            elif '$-1' in mnemnonic:
                if mnemnonic[1] == '%D' or mnemnonic[2] == '%D':
                    bits = '0001110'
                elif mnemnonic[1] == '%A' or mnemnonic[2] == '%A':
                    bits = '0110010'
                elif mnemnonic[1] == '(%A)' or mnemnonic[2] == '(%A)':
                    bits = '1110010'
            elif mnemnonic[1] == '(%A)' or mnemnonic[2] == '(%A)':
                bits = '1000010'
            else:
                bits = '0000010'
        elif mnemnonic[0] == 'subw':
            if '$1' in mnemnonic:
                if mnemnonic[1] == '%D' or mnemnonic[2] == '%D':
                    bits = '0001110'
                elif mnemnonic[1] == '%A' or mnemnonic[2] == '%A':
                    bits = '0110010'
                elif mnemnonic[1] == '(%A)' or mnemnonic[2] == '(%A)':
                    bits = '1110010'
            elif mnemnonic[1] == '%D':
                if mnemnonic[2] == '%A':
                    bits = '0010011'
                else:
                    bits = '1010011'
            elif mnemnonic[1] == '%A':
                bits = '0000111'
            else:
                bits = '1000111'
        elif mnemnonic[0] == 'andw':
            if mnemnonic[1] == '(%A)' or mnemnonic[2] == '(%A)':
                bits = '1000000'
            else:
                bits = '0000000'
        elif mnemnonic[0] == 'orw':
            if mnemnonic[1] == '(%A)' or mnemnonic[2] == '(%A)':
                bits = '1010101'
            else:
                bits = '0010101'
        elif mnemnonic[0] == 'rsubw':
            if mnemnonic[1] == '%A':
                bits = '0010011'
            elif mnemnonic[1] == '(%A)':
                bits = '1010011'
            else:
                if mnemnonic[2] == '%A':
                    bits = '0000111'
                else:
                    bits = '1000111'
        elif mnemnonic[0] in ['jmp', 'jle', 'je', 'jl', 'jne', 'jge', 'jg']:
            bits = '0001100'
        else:
            raise ValueError(f'Erro: mnemônico {mnemnonic} não reconhecido.')

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
        
