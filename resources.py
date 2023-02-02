import os
from os import path

def verificar_direccion(dir) -> bool:
    os.path.abspath(dir)
    if path.isdir(dir):
        return True
    else:
        return False

def verificar_archivo(arch) -> bool:
    if path.isfile(arch):
        return True
    else:
        return False
def obtenerFilaUsuario (usuario,arch,separador,cantidad) :
    #Se puede usar con /etc/shadow /etc/passwd
    info=[] #list donde se guardara la columna donde estara el usuario y su info
    #abro archivo
    with open(arch,'r+') as tem_f:
        datafile=tem_f.readlines() #se almacena lo que esta el archivo en datafile como un list por cada linea 
    for line in datafile:
        if usuario in line:
            #encuentra la linea del usuario y separa por el separador
            info=line.split(separador,cantidad)
    return info
def guardarFilaUsuario (usuario,arch,newLine) :
    #abro archivo
    with open(arch,'r+') as tem_f:
        datafile=tem_f.readlines()
    for line in datafile:
        if usuario in line:
            index=datafile.index(line)
            datafile[index]=newLine
    with open(arch,'r+') as tem_f:
        tem_f.writelines(datafile)

def unirArray(array,separador):
    return separador.join(array)

def check_string(str,arch) -> bool:
    with open(arch,"r+") as temp_f:
        datafile=temp_f.readlines()
    for line in datafile:
        if str in line:
            return True
    return False

def crearArchivos(path) -> None:
    for i in path:
        if not os.path.exists(i):
            os.system('touch '+ path)