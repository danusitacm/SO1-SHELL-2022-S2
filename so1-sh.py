#!/usr/bin/env python
"""A simple cmd2 application."""
import cmd2
import argparse
import os
import os.path
from os import path
import shutil
from pathlib import Path

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

class FirstApp(cmd2.Cmd):
    """A simple cmd2 application."""
    # parser copiar
    cop_parser = argparse.ArgumentParser(description='Copia un archivo en un directorio determinado.')
    cop_parser.add_argument('Archivos', type=str ,nargs='+',help = "Los archivos a utilizar")
    cop_parser.add_argument('Directorio_Destino' , type=str,nargs=1, help = "Directorio destino")
    @cmd2.with_argparser(cop_parser)
    def do_copiar(self, args: argparse.Namespace) -> None:
        if verificar_direccion(args.Directorio_Destino[0]):
            destino = os.path.abspath(args.Directorio_Destino[0])
            self.poutput(destino)
            for i in range(len(args.Archivos)):
                if(verificar_archivo(args.Archivos[i])):
                    destino = os.path.join(destino,args.Archivos[i])
                    filedest = open(destino, 'w')
                    os.path.abspath(args.Archivos[i])
                    origen = open(args.Archivos[i],'r')
                    shutil.copy(args.Archivos[i],destino)
                    origen.close()
                    filedest.close()
                    self.poutput("archivo " + args.Archivos[i] + " copiado")
                else:
                    self.poutput("archivo no valido" + args.Archivos[i])   
            destino.close()         
        else:
            self.poutput("Directorio no valido")
    
    #Parse mover
    mov_parser = argparse.ArgumentParser(description='Mueve un archivo a un directorio determinado.')
    mov_parser.add_argument('Archivos', type=str ,nargs='+',help = "Los archivos a utilizar")
    mov_parser.add_argument('Directorio_Destino' , type=str,nargs=1, help = "Directorio destino")
    @cmd2.with_argparser(mov_parser)
    def do_mover(self, args: argparse.Namespace) -> None:
        if verificar_direccion(args.Directorio_Destino[0]):
            destino = os.path.abspath(args.Directorio_Destino[0])
            self.poutput(destino)
            for i in range(len(args.Archivos)):
                if(verificar_archivo(args.Archivos[i])):
                    destino = os.path.join(destino,args.Archivos[i])
                    filedest = open(destino, 'w')
                    os.path.abspath(args.Archivos[i])
                    origen = open(args.Archivos[i],'r')
                    shutil.copy(args.Archivos[i],destino)
                    os.remove(args.Archivos[i])
                    origen.close()
                    filedest.close()
                    self.poutput("archivo " + args.Archivos[i] + " movido")
                else:
                    self.poutput("archivo no valido" + args.Archivos[i])   
            destino.close()         
        else:
            self.poutput("Directorio no valido")
    
    #Parser renombrar
    renombrar_parser = argparse.ArgumentParser(description='Renombra un archivo.')
    renombrar_parser.add_argument('Archivo', type=str ,nargs='+',help = "Los archivos a renombrar")
    renombrar_parser.add_argument('Nuevo_nombre' , type=str,nargs=1, help = "Nuevo nombre del archivo")
    @cmd2.with_argparser(renombrar_parser)
    def do_renombrar(self, args: argparse.Namespace) -> None:
        if(verificar_archivo(args.Archivo[0])):
                    destino = os.path.join(os.getcwd(),args.Nuevo_nombre[0])
                    filedest = open(destino, 'w')
                    os.path.abspath(args.Archivo[0])
                    origen = open(args.Archivo[0],'r')
                    shutil.copy(args.Archivo[0],destino)
                    os.remove(args.Archivo[0])
                    origen.close()
                    filedest.close()
                    self.poutput("archivo renombrado")
        else:
            self.poutput("archivo no valido")         
    
    #Parse del pwd 
    pwd_parser = argparse.ArgumentParser(description='Imprime el directorio actual de trabajo.')
    @cmd2.with_argparser(pwd_parser)
    def do_pwd(self, args: argparse.Namespace) -> None:
       self.poutput(os.path.dirname(os.path.realpath(__file__)))
    
    #Parse de listar
    listar_parser = argparse.ArgumentParser(description='Lista los archivos y directorios de un directorio determinado.')
    listar_parser.add_argument('Directorio_Destino',nargs='?', default=os.getcwd(), type=str, help ="Directorio destino")
    @cmd2.with_argparser(listar_parser)
    def do_listar(self, args: argparse.Namespace) -> None:
        if verificar_direccion(args.Directorio_Destino):
            dirs = os.listdir(args.Directorio_Destino)
            for file in dirs:
               self.poutput(file)
        else:
            self.poutput("Directorio no valido")

if __name__ == '__main__':
    import sys
    c = FirstApp()
    sys.exit(c.cmdloop())