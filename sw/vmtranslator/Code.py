#!/usr/bin/env python3
import io
import os
import queue
import uuid


class Code:
    def __init__(self, outFile):
        self.outFile = outFile
        self.counter = 0
        self.vmFileName = None
        self.labelCounter = 0

    # DONE
    def close(self):
        self.outFile.close()

    # DONE
    def updateVmFileName(self, name):
        self.vmFileName = os.path.basename(name).split(".")[0]

    # DONE
    def commandsToFile(self, commands):
        for line in commands:
            self.outFile.write(f"{line}\n")

    # DONE
    def getUniqLabel(self):
        return self.vmFileName + str(self.labelCounter)

    # DONE
    def updateUniqLabel(self):
        self.labelCounter = self.labelCounter + 1

    # DONE
    def writeHead(self, command):
        self.counter = self.counter + 1
        return ";; " + command + " - " + str(self.counter)

    # DONE
    def writeInit(self, bootstrap, isDir):
        commands = []

        if bootstrap or isDir:
            commands.append(self.writeHead("init"))

        if bootstrap:
            commands.append("leaw $256,%A")
            commands.append("movw %A,%D")
            commands.append("leaw $SP,%A")
            commands.append("movw %D,(%A)")

        if isDir:
            commands.append("leaw $Main.main, %A")
            commands.append("jmp")
            commands.append("nop")

        if bootstrap or isDir:
            self.commandsToFile(commands)

    # DONE
    def writeLabel(self, label):
        commands = []
        commands.append(self.writeHead("label") + " " + label)

        commands.append(label + ":")

        self.commandsToFile(commands)

    # DONE
    def writeGoto(self, label):
        commands = []
        commands.append(self.writeHead("goto") + " " + label)

        commands.append(f"leaw ${label}, %A")
        commands.append(f"jmp")
        commands.append(f"nop")

        self.commandsToFile(commands)

    # DONE
    def writeIf(self, label):
        commands = []
        commands.append(self.writeHead("if") + " " + label)

        commands.append(f"leaw $SP, %A") # pegar um antes, SP tá no vazio em cima do stack.
        commands.append(f"subw (%A), $1, %D") # armazena a booleana em D, false == 000000000
        commands.append('movw %D, (%A)')
        commands.append('movw %D, %A')
        commands.append('movw (%A), %D')
        commands.append(f"notw %D") # id D == 0000000 , ent jmp

        commands.append(f"leaw ${label}, %A")
        commands.append(f"je")
        commands.append(f"nop")
        
        self.commandsToFile(commands)

    # DONE
    def writeArithmetic(self, command):
        self.updateUniqLabel()
        if len(command) < 2:
            print("instrucão invalida {}".format(command))
        commands = []
        commands.append(self.writeHead(command))

        if command == "add":
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw (%A), %D")
            commands.append("decw %A")
            commands.append("addw (%A), %D, %D")
            commands.append("movw %D, (%A)")
            commands.append("incw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
        elif command == "sub":
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw (%A), %D")
            commands.append("decw %A")
            commands.append("subw (%A), %D, %D")
            commands.append("movw %D, (%A)")
            commands.append("incw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
        elif command == "or":
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw (%A), %D")
            commands.append("decw %A")
            commands.append("orw (%A), %D, %D")
            commands.append("movw %D, (%A)")
            commands.append("incw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
        elif command == "and":
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw (%A), %D")
            commands.append("decw %A")
            commands.append("andw (%A), %D, %D")
            commands.append("movw %D, (%A)")
            commands.append("incw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
        elif command == "not":
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw (%A), %D")
            commands.append("notw %D")
            commands.append("movw %D, (%A)")
        elif command == "neg":
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw (%A), %D")
            commands.append("negw %D")
            commands.append("movw %D, (%A)")
        elif command == "eq":
            # dica, usar self.getUniqLabel() para obter um label único
            label1 = self.getUniqLabel()
            self.updateUniqLabel()
            label2 = self.getUniqLabel()

            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw (%A), %D")
            commands.append("decw %A")
            commands.append("subw (%A), %D, %D")
            commands.append(f"leaw ${label1}, %A")
            commands.append("je")
            commands.append("nop")

            commands.append("leaw $0, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("decw %A")
            commands.append("movw %D, (%A)")
            commands.append(f"leaw ${label2}, %A")
            commands.append("jmp")
            commands.append("nop")

            commands.append(f"{label1}:") # SÃO IGUAIS
            commands.append("leaw $0, %A")
            commands.append("notw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("decw %A")
            commands.append("movw %D, (%A)")
            
            commands.append(f"{label2}:")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
        elif command == "gt":
            # dica, usar self.getUniqLabel() para obter um label único
            label1 = self.getUniqLabel()
            self.updateUniqLabel()
            label2 = self.getUniqLabel()

            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw (%A), %D")
            commands.append("decw %A")
            commands.append("subw (%A), %D, %D")
            commands.append(f"leaw ${label1}, %A")
            commands.append("jg")
            commands.append("nop")

            commands.append("leaw $0, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("decw %A")
            commands.append("movw %D, (%A)")
            commands.append(f"leaw ${label2}, %A")
            commands.append("jmp")
            commands.append("nop")

            commands.append(f"{label1}:")
            commands.append("leaw $0, %A")
            commands.append("notw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("decw %A")
            commands.append("movw %D, (%A)")
            
            commands.append(f"{label2}:")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
        elif command == "lt":
            # dica, usar self.getUniqLabel() para obter um label único
            label1 = self.getUniqLabel()
            self.updateUniqLabel()
            label2 = self.getUniqLabel()

            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw (%A), %D")
            commands.append("decw %A")
            commands.append("subw (%A), %D, %D")
            commands.append(f"leaw ${label1}, %A")
            commands.append("jl")
            commands.append("nop")

            commands.append("leaw $0, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("decw %A")
            commands.append("movw %D, (%A)")
            commands.append(f"leaw ${label2}, %A")
            commands.append("jmp")
            commands.append("nop")

            commands.append(f"{label1}:")
            commands.append("leaw $0, %A")
            commands.append("notw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("decw %A")
            commands.append("movw %D, (%A)")
            
            commands.append(f"{label2}:")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("decw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")

        self.commandsToFile(commands)

    # DONE
    def writePop(self, command, segment, index):
        self.updateUniqLabel()
        commands = []
        commands.append(self.writeHead(command) + " " + segment + " " + str(index))

        if segment == "" or segment == "constant":
            return False
        elif segment == "local":

            commands.append('leaw $SP, %A')
            commands.append('subw (%A), $1, %A')
            commands.append('movw (%A), %D')
            commands.append('leaw $LCL, %A')
            commands.append('movw (%A), %A')
            if index != 0:
                for _ in range(index):
                    commands.append('incw %A')
            commands.append('movw %D, (%A)')
            commands.append('leaw $SP, %A')
            commands.append('subw (%A), $1, %D')
            commands.append('movw %D, (%A)')

        elif segment == "argument":

            commands.append('leaw $SP, %A')
            commands.append('subw (%A), $1, %A')
            commands.append('movw (%A), %D')
            commands.append('leaw $ARG, %A')
            commands.append('movw (%A), %A')
            if index != 0:
                for _ in range(index):
                    commands.append('incw %A')
            commands.append('movw %D, (%A)')
            commands.append('leaw $SP, %A')
            commands.append('subw (%A), $1, %D')
            commands.append('movw %D, (%A)')

        elif segment == "this":
            commands.append('leaw $SP, %A')
            commands.append('subw (%A), $1, %A')
            commands.append('movw (%A), %D')
            commands.append('leaw $THIS, %A')
            commands.append('movw (%A), %A')
            if index != 0:
                for _ in range(index):
                    commands.append('incw %A')
            commands.append('movw %D, (%A)')
            commands.append('leaw $SP, %A')
            commands.append('subw (%A), $1, %D')
            commands.append('movw %D, (%A)')
        elif segment == "that":
            commands.append('leaw $SP, %A')
            commands.append('subw (%A), $1, %A')
            commands.append('movw (%A), %D')
            commands.append('leaw $THAT, %A')
            commands.append('movw (%A), %A')
            if index != 0:
                for _ in range(index):
                    commands.append('incw %A')
            commands.append('movw %D, (%A)')
            commands.append('leaw $SP, %A')
            commands.append('subw (%A), $1, %D')
            commands.append('movw %D, (%A)')
        elif segment == "temp":

            commands.append('leaw $SP, %A')
            commands.append('subw (%A), $1, %A')
            commands.append('movw (%A), %D')
            commands.append('leaw $5, %A')
            if index != 0:
                for _ in range(index):
                    commands.append('incw %A')
            commands.append('movw %D, (%A)')
            commands.append('leaw $SP, %A')
            commands.append('subw (%A), $1, %D')
            commands.append('movw %D, (%A)')

        elif segment == "static":

            commands.append('leaw $SP, %A')
            commands.append('subw (%A), $1, %A')
            commands.append('movw (%A), %D')
            commands.append('leaw $16, %A')
            if index != 0:
                for _ in range(index):
                    commands.append('incw %A')
            commands.append('movw %D, (%A)')
            commands.append('leaw $SP, %A')
            commands.append('subw (%A), $1, %D')
            commands.append('movw %D, (%A)')

        elif segment == "pointer":
            commands.append('leaw $SP, %A')
            commands.append('subw (%A), $1, %A')
            commands.append('movw (%A), %D')
            if index == 0:
                commands.append('leaw $THIS, %A')
            else:
                commands.append('leaw $THAT, %A')
            commands.append('movw %D, (%A)')
            commands.append('leaw $SP, %A')
            commands.append('subw (%A), $1, %D')
            commands.append('movw %D, (%A)')

        self.commandsToFile(commands)

    # DONE
    def writePush(self, command, segment, index):
        commands = []
        commands.append(self.writeHead(command + " " + segment + " " + str(index)))

        if segment == "constant":
            # dica: usar index para saber o valor da consante
            # push constant index
            commands.append('leaw $' + str(index) + ', %A')
            commands.append('movw %A, %D')
            commands.append('leaw $SP, %A')
            commands.append('movw (%A), %A')
            commands.append('movw %D, (%A)')
            commands.append('incw %A')
            commands.append('movw %A, %D')
            commands.append('leaw $SP, %A')
            commands.append('movw %D, (%A)')
        elif segment == "local":
            commands.append('leaw $LCL, %A')
            commands.append('movw (%A), %A')
            if index != 0:
                for _ in range(index):
                    commands.append('incw %A')
            commands.append('movw (%A), %D')
            commands.append('leaw $SP, %A')
            commands.append('movw (%A), %A')
            commands.append('movw %D, (%A)')
            commands.append('incw %A')
            commands.append('movw %A, %D')
            commands.append('leaw $SP, %A')
            commands.append('movw %D, (%A)')
        elif segment == "argument":
            commands.append('leaw $ARG, %A')
            commands.append('movw (%A), %A')
            if index != 0:
                for _ in range(index):
                    commands.append('incw %A')
            commands.append('movw (%A), %D')
            commands.append('leaw $SP, %A')
            commands.append('movw (%A), %A')
            commands.append('movw %D, (%A)')
            commands.append('incw %A')
            commands.append('movw %A, %D')
            commands.append('leaw $SP, %A')
            commands.append('movw %D, (%A)')
        elif segment == "this":
            commands.append('leaw $THIS, %A')
            commands.append('movw (%A), %A')
            if index != 0:
                for _ in range(index):
                    commands.append('incw %A')
            commands.append('movw (%A), %D')
            commands.append('leaw $SP, %A')
            commands.append('movw (%A), %A')
            commands.append('movw %D, (%A)')
            commands.append('incw %A')
            commands.append('movw %A, %D')
            commands.append('leaw $SP, %A')
            commands.append('movw %D, (%A)')
        elif segment == "that":
            commands.append('leaw $THAT, %A')
            commands.append('movw (%A), %A')
            if index != 0:
                for _ in range(index):
                    commands.append('incw %A')
            commands.append('movw (%A), %D')
            commands.append('leaw $SP, %A')
            commands.append('movw (%A), %A')
            commands.append('movw %D, (%A)')
            commands.append('incw %A')
            commands.append('movw %A, %D')
            commands.append('leaw $SP, %A')
            commands.append('movw %D, (%A)')
        elif segment == "argument":
            commands.append('leaw $ARG, %A')
            commands.append('movw (%A), %A')
            if index != 0:
                for _ in range(index):
                    commands.append('incw %A')
            commands.append('movw (%A), %D')
            commands.append('leaw $SP, %A')
            commands.append('movw (%A), %A')
            commands.append('movw %D, (%A)')
            commands.append('incw %A')
            commands.append('movw %A, %D')
            commands.append('leaw $SP, %A')
            commands.append('movw %D, (%A)')
        elif segment == "static":
            commands.append('leaw $16, %A')
            if index != 0:
                for _ in range(index):
                    commands.append('incw %A')
            commands.append('movw (%A), %D')
            commands.append('leaw $SP, %A')
            commands.append('movw (%A), %A')
            commands.append('movw %D, (%A)')
            commands.append('incw %A')
            commands.append('movw %A, %D')
            commands.append('leaw $SP, %A')
            commands.append('movw %D, (%A)')
        elif segment == "temp":
            commands.append('leaw $5, %A')
            if index != 0:
                for _ in range(index):
                    commands.append('incw %A')
            commands.append('movw (%A), %D')
            commands.append('leaw $SP, %A')
            commands.append('movw (%A), %A')
            commands.append('movw %D, (%A)')
            commands.append('incw %A')
            commands.append('movw %A, %D')
            commands.append('leaw $SP, %A')
            commands.append('movw %D, (%A)')
        elif segment == "pointer":
            if index == 0:
                commands.append('leaw $THIS, %A')
            else:
                commands.append('leaw $THAT, %A')
            commands.append('movw (%A), %D')
            commands.append('leaw $SP, %A')
            commands.append('movw (%A), %A')
            commands.append('movw %D, (%A)')
            commands.append('incw %A')
            commands.append('movw %A, %D')
            commands.append('leaw $SP, %A')
            commands.append('movw %D, (%A)')

        self.commandsToFile(commands)

    # TODO
    def writeCall(self, funcName, numArgs):
        commands = []
        commands.append(self.writeHead("call") + " " + funcName + " " + str(numArgs))
        self.updateUniqLabel()
        labelReturn = self.getUniqLabel()
        self.updateUniqLabel()

        # coloca a label return no topo da pilha, começando a criar o frame
        commands.append(f'leaw ${labelReturn}, %A')
        commands.append('movw %A, %D')
        commands.append('leaw $SP, %A')
        commands.append('movw (%A), %A')
        commands.append('movw %D, (%A)')

        # coloca o local no frame
        commands.append('incw %A')
        commands.append('movw %A, %D')
        commands.append('leaw $SP, %A')
        commands.append('movw %D, (%A)') # salva como novo SP
        commands.append('leaw $LCL, %A')
        commands.append('movw (%A), %D')
        commands.append('leaw $SP, %A')
        commands.append('movw (%A), %A')
        commands.append('movw %D, (%A)')

        # coloca o argument no frame
        commands.append('incw %A')
        commands.append('movw %A, %D')
        commands.append('leaw $SP, %A')
        commands.append('movw %D, (%A)') # salva como novo SP
        commands.append('leaw $ARG, %A')
        commands.append('movw (%A), %D')
        commands.append('leaw $SP, %A')
        commands.append('movw (%A), %A')
        commands.append('movw %D, (%A)')

        # coloca o this no frame
        commands.append('incw %A')
        commands.append('movw %A, %D')
        commands.append('leaw $SP, %A')
        commands.append('movw %D, (%A)') # salva como novo SP
        commands.append('leaw $THIS, %A')
        commands.append('movw (%A), %D')
        commands.append('leaw $SP, %A')
        commands.append('movw (%A), %A')
        commands.append('movw %D, (%A)')

        # coloca o that no frame
        commands.append('incw %A')
        commands.append('movw %A, %D')
        commands.append('leaw $SP, %A')
        commands.append('movw %D, (%A)') # salva como novo SP
        commands.append('leaw $THAT, %A')
        commands.append('movw (%A), %D')
        commands.append('leaw $SP, %A')
        commands.append('movw (%A), %A')
        commands.append('movw %D, (%A)')

        # atualiza o novo local
        commands.append('incw %A')
        commands.append('movw %A, %D')
        commands.append('leaw $LCL, %A')
        commands.append('movw %D, (%A)')

        # atualiza o SP
        commands.append(f'leaw $SP, %A')
        commands.append('movw %D, (%A)')

        # atualiza o novo argument
        commands.append('leaw $5, %A')
        commands.append('subw %D, %A, %D')
        commands.append(f'leaw ${numArgs}, %A')
        commands.append('subw %D, %A, %D')
        commands.append('leaw $ARG, %A')
        commands.append('movw %D, (%A)')

        # salta para a função
        commands.append(f'leaw ${funcName}, %A')
        commands.append('jmp')
        commands.append('nop')


        commands.append(f'{labelReturn}:')

        self.commandsToFile(commands)

    # TODO
    def writeReturn(self):
        commands = []
        commands.append(self.writeHead("return"))

        # joga o resultado no lugar do primeiro arg
        commands.append('leaw $SP, %A')
        commands.append('subw (%A), $1, %A')
        commands.append('movw (%A), %D')
        commands.append('leaw $ARG, %A')
        commands.append('movw (%A), %A')
        commands.append('movw %D, (%A)')

        # atualiza o SP
        commands.append('incw %A')
        commands.append('movw %A, %D')
        commands.append('leaw $SP, %A')
        commands.append('movw %D, (%A)')

        # atualiza de volta o THAT
        commands.append('leaw $LCL, %A')
        commands.append('subw (%A), $1, %A')
        commands.append('movw (%A), %D')
        commands.append('leaw $THAT, %A')
        commands.append('movw %D, (%A)')

        # atualiza de volta o THIS
        commands.append('leaw $LCL, %A')
        commands.append('subw (%A), $1, %A')
        commands.append('decw %A')
        commands.append('movw (%A), %D')
        commands.append('leaw $THIS, %A')
        commands.append('movw %D, (%A)')

        # atualiza de volta o ARG
        commands.append('leaw $LCL, %A')
        commands.append('subw (%A), $1, %A')
        commands.append('decw %A')
        commands.append('decw %A')
        commands.append('movw (%A), %D')
        commands.append('leaw $ARG, %A')
        commands.append('movw %D, (%A)')

        # pega a label de return e coloca onde o SP aponta
        commands.append('leaw $LCL, %A')
        commands.append('subw (%A), $1, %A')
        commands.append('movw %A, %D')
        commands.append('leaw $4, %A')
        commands.append('subw %D, %A, %A')
        commands.append('movw (%A), %D')
        commands.append('leaw $SP, %A')
        commands.append('movw (%A), %A')
        commands.append('movw %D, (%A)')

        # atualiza de volta o LCL
        commands.append('leaw $LCL, %A')
        commands.append('subw (%A), $1, %A')
        commands.append('movw %A, %D')
        commands.append('leaw $3, %A')
        commands.append('subw %D, %A, %A')
        commands.append('movw (%A), %D')
        commands.append('leaw $LCL, %A')
        commands.append('movw %D, (%A)')

        # salta para o lugar de retorno
        commands.append('leaw $SP, %A')
        commands.append('movw (%A), %A')
        commands.append('movw (%A), %A')
        commands.append('jmp')
        commands.append('nop')


        self.commandsToFile(commands)

    # TODO
    def writeFunction(self, funcName, numLocals):
        commands = []
        commands.append(self.writeHead("func") + " " + funcName + " " + str(numLocals))

        commands.append(f'{funcName}:')

        #atualiza o novo SP, reservando espaço para as variáveis locais
        commands.append('leaw $SP, %A')
        commands.append('movw (%A), %D')
        commands.append(f'leaw ${numLocals}, %A')
        commands.append('addw %D, %A, %D')
        commands.append('leaw $SP, %A')
        commands.append('movw %D, (%A)')

        self.commandsToFile(commands)
