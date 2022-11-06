

class SymbolTable:
    # DONE
    def __init__(self):
        self.table = {}
        self.init()

    
    def init(self):
        """
        Inicializa a tabela de simbolos com os simbolos pre definidos
        exemplo: R0, R1, ...
        SP, LCL, ARG, THIS, THAT
        SCREEN, KBD, ..
        """

        self.table = {
            'SP': 0,
            'LCL': 1,
            'ARG': 2,
            'THIS': 3,
            'THAT': 4,
            'SCREEN': 16384,
            'LED': 21184,
            'SW': 21185,
            'x': 16,
            'y': 17,
            'LOOP': 2,
            'UPDATE': 12,
            'END': 14,
            'KBD': 24576
        }

        for i in range(16):
            self.table[f'R{i}'] = i
        

    def addEntry(self, symbol: str, address: int):
        """
        Insere uma entrada de um símbolo com seu endereço numérico na tabela de símbolos (self.table).
        @param symbol símbolo a ser armazenado na tabela de símbolos.
        @param address símbolo a ser armazenado na tabela de símbolos.
        """
        self.table[symbol] = address

    def contains(self, symbol):
        """
        Confere se o símbolo informado já foi inserido na tabela de símbolos.
        @param  symbol símbolo a ser procurado na tabela de símbolos.
        @return Verdadeiro se símbolo está na tabela de símbolos, Falso se não está na tabela de símbolos.
        """
        if symbol in self.table:
            return True
        return False

    
    def getAddress(self, symbol):
        """
        Retorna o valor númerico associado a um símbolo já inserido na tabela de símbolos.
        @param  symbol símbolo a ser procurado na tabela de símbolos.
        @return valor numérico associado ao símbolo procurado.
        """
        return self.table[symbol]
