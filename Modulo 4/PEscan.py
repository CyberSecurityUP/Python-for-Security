# importar o modulo de analise de arquivo PE
import pefile

def func5():
	#file = input("Select File: ")
	#pe = pefile.PE(file)
        # passando o paramento pe.file e definindo o exe que vai ser usado
        pe = pefile.PE("test.exe")
        # printar todos os cabeçalhos do arquivo 
        pe.print_info() # Prints all Headers in a human readable format
        # abaixo ele printa os hexadeciminal do cabeçalho DOS e_magic e lfanew
	#print("e_magic : " + hex(pe.DOS_HEADER.e_magic)) # Prints the e_magic field of the DOS_HEADER
	#print("e_lfnew : " + hex(pe.DOS_HEADER.e_lfanew)) # Prints the e_lfnew field of the DOS_HEADER
if __name__ == '__main__':
	func5()
