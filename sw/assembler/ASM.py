from .ASMsymbolTable import SymbolTable
from .ASMcode import Code
from .ASMparser import Parser


class ASM:

    # DONE
    def __init__(self, nasm, hack):
        self.hack = hack
        self.symbolTable = SymbolTable()
        self.parser = Parser(nasm)
        self.code = Code()

        self.lastIsJump = False

    # DONE
    def run(self):
        try:
            self.fillSymbolTable()
            self.generateMachineCode()
            return 0
        except Exception as e:
            print(e)
            print("--> ERRO AO TRADUZIR: {}".format(self.parser.currentLine))
            return -1

    # DONE
    def fillSymbolTable(self):
        """
        primeiro passo para a construção da tabela de símbolos de marcadores (labels)
        varre o código em busca de novos Labels e Endereços de memórias (variáveis)
        e atualiza a tabela de símbolos com os endereços (table).

        Dependencia : Parser, SymbolTable
        """
        while self.parser.advanced():
            if self.lastIsJump and self.parser.currentCommand[0] != 'nop':
                self.parser.no_additions += 1
                self.lastIsJump = False
            if self.parser.commandType() == "L_COMMAND":
                print(self.parser.no_additions)
                self.parser.no_labels += 1
                self.symbolTable.addEntry(self.parser.label(), self.parser.lineNumber - self.parser.no_labels + self.parser.no_additions + self.parser.no_leawD)
            if self.parser.commandType() == 'C_COMMAND':
                if self.parser.currentCommand[0][0] == 'j':
                    self.lastIsJump = True
                else:
                    self.lastIsJump = False
            if self.parser.commandType() == "A_COMMAND":
                if self.parser.currentCommand[2] == "%D":
                    self.parser.no_leawD += 1
            
        self.lastIsJump = False
            
        self.parser.reset()

    # DONE
    def generateMachineCode(self):
        """
        Segundo passo para a geração do código de máquina
        Varre o código em busca de instruções do tipo A, C
        gerando a linguagem de máquina a partir do parse das instruções.

        Dependencias : Parser, Code, fillSymbolTable
        """
        
        while self.parser.advanced():
            if self.parser.commandType() == "C_COMMAND":
                if self.parser.currentCommand[0][0] == 'j':
                    bin = "1000" + self.code.comp(self.parser.currentCommand) + "0" + self.code.dest(self.parser.currentCommand) + self.code.jump(self.parser.currentCommand) + "\n" + '100001010100000000'
                    self.lastIsJump = True
                    self.hack.write(bin + "\n")
                elif self.parser.currentCommand[0] == "nop" and not self.lastIsJump:
                    bin = '100001010100000000'
                    self.hack.write(bin + "\n")
                elif self.lastIsJump and self.parser.currentCommand[0] == "nop":
                    pass
                else:
                    bin = "1000" + self.code.comp(self.parser.currentCommand) + "0" + self.code.dest(self.parser.currentCommand) + self.code.jump(self.parser.currentCommand)
                    self.lastIsJump = False
                    self.hack.write(bin + "\n")

            elif self.parser.commandType() == "A_COMMAND":
                if self.symbolTable.contains(self.parser.symbol()):
                    bin = "00" + self.code.toBinary(self.symbolTable.getAddress(self.parser.symbol()))
                else:
                    bin = "00" + self.code.toBinary(self.parser.symbol())
                
                if self.parser.currentCommand[2] == "%D":
                    bin += "\n"
                    bin += '100001100000010000'
                
                self.hack.write(bin + "\n")