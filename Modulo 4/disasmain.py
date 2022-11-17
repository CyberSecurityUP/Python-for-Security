#pip install pyelftools
# import os modulos ELFFile para analisar arquivos ELF
from elftools.elf.elffile import ELFFile
# E o modulo capstone que ajuda no disassembler
from capstone import *

print("JOAS ANTONIO")
# Abaixo seleciono o arquivo que ele vai abrir e ler
with open('.\test.elf', 'rb') as f:   #change the file name to what you are performing reverse engineering
    # aqui ele vai abrir o arquivo elffile 
    elf = ELFFile(f)
    # coleta seção .text que retorna os trechos relacionados a código
    code = elf.get_section_by_name('.text')
    # é a referência à instrução que um determinado processador possui para conseguir realizar determinadas tarefas.
    ops = code.data()                 # returns a bytestring with the opcodes
    # Se esta seção aparecer na imagem de memória de um processo, este membro contém o endereço no qual o primeiro byte da seção deve residir.
    addr = code['sh_addr']            # starting address of `.text`
    # Definição da arquitetura da aplicação, seja ela compilada em x86 ou x64
    md = Cs(CS_ARCH_X86, CS_MODE_64)
    for i in md.disasm(ops, 0x7aa):    # looping through each opcode
        # Aqui ele vai trazer opcodes, seja endereços de memória
# mnemônicos são usados ​​para especificar um opcode que representa uma instrução de linguagem de máquina completa e operacional
# Por fim a representação do objeto
        print(f"0x{i.address:x}:\t{i.mnemonic}\t{i.op_str}")
