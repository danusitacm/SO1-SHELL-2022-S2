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
    delattr(cmd2.Cmd,'do_shell')
    delattr(cmd2.Cmd,'do_set')
    def __init__(self):
        builtin_commands=['alias','edit','history','py','run_pyscript','run_script','shortcuts','macro']
        super().__init__()
        self.hidden_commands.extend(builtin_commands) #Para esconder los Builtin Commands
    # parser copiar
    cop_parser = argparse.ArgumentParser(description='Copiar un archivo en un directorio determinado.')
    cop_parser.add_argument('Archivos', type=str ,nargs='+',help = 'Los archivos a utilizar')
    cop_parser.add_argument('Directorio_Destino' , type=str,nargs=1, help = 'Directorio destino')
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
                    self.poutput('archivo '+ args.Archivos[i] +' copiado')
                else:
                    self.poutput('archivo no valido' + args.Archivos[i])   
            destino.close()         
        else:
            self.poutput('Directorio no valido')
    
    #Parse mover
    mov_parser = argparse.ArgumentParser(description='Mover un archivo a un directorio determinado.')
    mov_parser.add_argument('Archivos', type=str ,nargs='+',help = 'Los archivos a utilizar')
    mov_parser.add_argument('Directorio_Destino' , type=str,nargs=1, help = 'Directorio destino')
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
                    self.poutput('archivo ' + args.Archivos[i] + ' movido')
                else:
                    self.poutput('archivo no valido' + args.Archivos[i])   
            destino.close()         
        else:
            self.poutput('Directorio no valido')
    
    #Parser renombrar
    renombrar_parser = argparse.ArgumentParser(description='Renombrar un archivo.')
    renombrar_parser.add_argument('Archivo', type=str ,nargs='+',help = 'Los archivos a renombrar')
    renombrar_parser.add_argument('Nuevo_nombre' ,type=str,nargs=1, help = 'Nuevo nombre del archivo')
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
                    self.poutput('archivo renombrado')
        else:
            self.poutput('archivo no valido')         
    
    #Parse del pwd 
    pwd_parser = argparse.ArgumentParser(description='Mostar el directorio actual de trabajo.')
    @cmd2.with_argparser(pwd_parser)
    def do_pwd(self, args: argparse.Namespace) -> None:
       self.poutput(os.path.abspath(os.getcwd()))
    
    #Parse de listar
    listar_parser = argparse.ArgumentParser(description='Lista los archivos y directorios de un directorio determinado.')
    listar_parser.add_argument('Directorio_Destino',nargs='?', type=str, help ='Directorio destino')
    @cmd2.with_argparser(listar_parser)
    def do_listar(self, args: argparse.Namespace) -> None:
        args.Directorio_Destino=os.getcwd()
        if verificar_direccion(args.Directorio_Destino):
            os.path.abspath(args.Directorio_Destino)
            dirs = os.listdir(args.Directorio_Destino)
            for file in dirs:
               self.poutput(file)
        else:
            self.poutput('Directorio no valido')
    
    #Parse de creardir
    creardir_parser =argparse.ArgumentParser(description='Crea un archivo.')
    creardir_parser.add_argument('Nombre_Archivo', type=str, nargs='+',help ='El nombre del archivo')
    @cmd2.with_argparser(creardir_parser)
    def do_creardir(self, args: argparse.Namespace) -> None:
        for i in range(len(args.Nombre_Archivo)):
            if not os.path.exists(args.Nombre_Archivo[i]):
                os.mkdir(args.Nombre_Archivo[i])
            else:
                self.poutput('Ya existe un directorio o archivo con ese nombre.')
    #Parse de ir 
    ir_parser=argparse.ArgumentParser(description='Cambiar el directorio de trabajo actual de un usuario.')
    ir_parser.add_argument('Directorio_Destino',nargs='?', default='/', type=str, help ='Directorio destino')
    @cmd2.with_argparser(ir_parser)
    def do_ir(self, args: argparse.Namespace) -> None:
        self.poutput(args.Directorio_Destino)
        if verificar_direccion(args.Directorio_Destino):
            os.path.abspath(args.Directorio_Destino)
            os.chdir(args.Directorio_Destino)
        else:
            self.poutput('Directorio no valido')
    
    #Parse de permisos
    permiso_parser=argparse.ArgumentParser(description='Cambiar los permisos sobre un archivo o un directorio.')
    permiso_parser.add_argument('Permisos',type=str)
    permiso_parser.add_argument('Path',type=str)
    @cmd2.with_argparser(permiso_parser)
    def do_permiso(self, args: argparse.Namespace) -> None:
        if os.path.exists(args.Path):
            os.path.abspath(args.Path)
            os.chmod(args.Path, int(args.Permisos,8))
        else:
            self.poutput('Directorio no valido')
    
    #Parse de propietario
    propietario_parser=argparse.ArgumentParser(description='Cambiar los propietarios sobre un archivo o un conjunto de archivos.')
    propietario_parser.add_argument('UsuarioID',type=str,help='USUARIOID:[GRUPOID]')
    propietario_parser.add_argument('Archivos',nargs='*',type=str)
    @cmd2.with_argparser(propietario_parser)
    def do_propietario(self, args: argparse.Namespace) -> None:
        usuario=args.UsuarioID.split(':')
        self.poutput(usuario)
        for i in args.Archivos:
            if os.path.exists(i):
                os.path.abspath(i)
                self.poutput(i)
                os.chown(i,int(usuario[0]),int(usuario[1]))
            else:
                self.poutput('Directorio no valido')
            

if __name__ == '__main__':
    import sys
    c = FirstApp()
    sys.exit(c.cmdloop())