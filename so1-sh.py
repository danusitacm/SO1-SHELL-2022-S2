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
    # parser copiar y mover
    cop_mov_parser = argparse.ArgumentParser()
    cop_mov_parser.add_argument('Archivos', type=str ,nargs='+',help = "Los archivos a utilizar")
    cop_mov_parser.add_argument('Directorio_Destino' , type=str,nargs=1, help = "Directorio destino")

    @cmd2.with_argparser(cop_mov_parser)
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

    @cmd2.with_argparser(cop_mov_parser)
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
    
    # parser renombrar
    renombrar_parser = argparse.ArgumentParser()
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
         
    listar_parser = argparse.ArgumentParser()
    listar_parser.add_argument('Directorio_Destino' , default= os.getcwd(), type=str, help = "Directorio destino")
    @cmd2.with_argparser(listar_parser)
    def do_listar(self, args: argparse.Namespace) -> None:
        if verificar_direccion(args.Directorio_Destino[0]):
            os.path.abspath(args.Directorio_Destino[0])
            for path in Path(args.Directorio_Destino[0]).glob('/*'):
                self.poutput(path.name)
        else:
            self.poutput("Directorio no valido")

if __name__ == '__main__':
    import sys
    c = FirstApp()
    sys.exit(c.cmdloop())