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

    # TODO
    def writeGoto(self, label):
        commands = []
        commands.append(self.writeHead("goto") + " " + label)

        # TODO ...
        self.commandsToFile(commands)

    # TODO
    def writeIf(self, label):
        commands = []
        commands.append(self.writeHead("if") + " " + label)
        

        # TODO ...
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

    def writePop(self, command, segment, index):
        self.updateUniqLabel()
        commands = []
        commands.append(self.writeHead(command) + " " + segment + " " + str(index))

        if segment == "" or segment == "constant":
            return False
        elif segment == "local":
            # dica: usar o argumento index (push local 1)
            pass # TODO
        elif segment == "argument":
            pass # TODO
        elif segment == "this":
            pass # TODO
        elif segment == "that":
            pass # TODO
        elif segment == "temp":
            # dica: usar o argumento index (push temp 0)
            pass # TODO
        elif segment == "static":
            pass # TODO
        elif segment == "pointer":
            pass # TODO

        self.commandsToFile(commands)

    def writePush(self, command, segment, index):
        commands = []
        commands.append(self.writeHead(command + " " + segment + " " + str(index)))

        if segment == "constant":
            # dica: usar index para saber o valor da consante
            # push constant index
            pass # TODO
        elif segment == "local":
            pass # TODO
        elif segment == "argument":
            pass # TODO
        elif segment == "this":
            pass # TODO
        elif segment == "that":
            pass # TODO
        elif segment == "argument":
            pass # TODO
        elif segment == "static":
            pass # TODO
        elif segment == "temp":
            pass # TODO
        elif segment == "pointer":
            pass # TODO

        self.commandsToFile(commands)

    # TODO
    def writeCall(self, funcName, numArgs):
        commands = []
        commands.append(self.writeHead("call") + " " + funcName + " " + str(numArgs))

        # TODO
        # ...

        self.commandsToFile(commands)

    # TODO
    def writeReturn(self):
        commands = []
        commands.append(self.writeHead("return"))

        # TODO
        # ...

        self.commandsToFile(commands)

    # TODO
    def writeFunction(self, funcName, numLocals):
        commands = []
        commands.append(self.writeHead("func") + " " + funcName + " " + str(numLocals))

        # TODO
        # ...

        self.commandsToFile(commands)
