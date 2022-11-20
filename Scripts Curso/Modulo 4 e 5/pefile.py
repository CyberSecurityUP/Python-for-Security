import pefile

def func1():
    file = input("Nome do arquivo: ")
    pe = pefile.PE(file)
    pe.print_info()
    print("e_magic: " + hex(pe.DOS_HEADER.e_magic))

if __name__ == '__main__':
    func1()
