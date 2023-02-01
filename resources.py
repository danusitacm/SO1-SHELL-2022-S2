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

def check_string(str,arch) -> bool:
    with open(arch,"r") as temp_f:
        datafile=temp_f.readlines()
    for line in datafile:
        if str in line:
            return True
    return False

def crearArchivos(path) -> None:
    for i in path:
        if not os.path.exists(i):
            os.system('touch '+ path)