import os
from os import path
import colorama
from termcolor import colored

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
    if not os.path.exists(path):
        os.system('touch '+ path)

def errorMessage(msg) -> None:
    self.poutput(colored(msg,'red'))
    logs.SystemError(msg)