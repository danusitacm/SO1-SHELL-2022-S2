#!/usr/bin/env python
"""A simple cmd2 application."""
import resources
import cmd2
import argparse
import os
import os.path
import getpass
import crypt
import hashlib
import logs
from os import path
import shutil
from pathlib import Path
import colorama
from termcolor import colored

class FirstApp(cmd2.Cmd):
    """A simple cmd2 application."""
    delattr(cmd2.Cmd,'do_set')
    def __init__(self):
        builtin_commands=['alias','edit','py','run_pyscript','run_script','shortcuts','macro','shell']
        super().__init__()
        self.hidden_commands.extend(builtin_commands) #Para esconder los Builtin Commands
    #COMANDOS BASICOS
    #Copiar
    cop_parser = argparse.ArgumentParser(description='Copiar un archivo en un directorio determinado.')
    cop_parser.add_argument('Archivos', type=str ,nargs='+',help = 'Los archivos a utilizar')
    cop_parser.add_argument('Directorio_Destino', type=str, help = 'Directorio destino')
    @cmd2.with_argparser(cop_parser)
    def do_copiar(self, args: argparse.Namespace) -> None:
        try:
            pathDestino = os.path.abspath(args.Directorio_Destino)
            for arch in args.Archivos:
                pathOrigen=os.path.abspath(arch)
                if(resources.verificar_archivo(arch)):
                    pathDestino = os.path.join(pathDestino,arch)
                    fileDest = open(pathDestino, 'w')
                    fileOrigen = open(pathOrigen,'r')
                    shutil.copy(pathOrigen,pathDestino)
                    fileOrigen.close()
                    fileDest.close()
                    self.poutput(f'Archivo {arch} copiado.')
                else:
                    self.poutput(f'No es un archivo: {arch}.') 
        except Exception as error:
            msg=f'copiar: {error}'
            self.poutput(colored(msg,'red'))
            logs.SystemError(msg)
    #Mover
    mov_parser = argparse.ArgumentParser(description='Mover un archivo a un directorio determinado.')
    mov_parser.add_argument('Archivos', type=str,nargs='+',help = 'Los archivos a utilizar')
    mov_parser.add_argument('Directorio_Destino',type=str, help = 'Directorio destino')
    @cmd2.with_argparser(mov_parser)
    def do_mover(self, args: argparse.Namespace) -> None:
        try:
            pathDestino = os.path.abspath(args.Directorio_Destino)
            for arch in args.Archivos:
                pathOrigen=os.path.abspath(arch)
                if(resources.verificar_archivo(arch)):
                    pathDestino = os.path.join(pathDestino,arch)
                    fileDest = open(pathDestino, 'w')
                    fileOrigen = open(pathOrigen,'r')
                    shutil.copy(pathOrigen,pathDestino)
                    os.remove(pathOrigen)
                    fileOrigen.close()
                    fileDest.close()
                    self.poutput(f'Archivo {arch} movido.')
                else:
                    self.poutput(f'No es un archivo: {arch}.') 
        except Exception as error:
            msg=f'mover: {error}'
            self.poutput(colored(msg,'red'))
            logs.SystemError(msg)        
    #Renombrar
    renombrar_parser = argparse.ArgumentParser(description='Renombrar un archivo.')
    renombrar_parser.add_argument('Archivoa', type=str,help = 'Archivo a renombrar.')
    renombrar_parser.add_argument('Nuevo_nombre' ,type=str, help = 'Nuevo nombre del archivo.')
    @cmd2.with_argparser(renombrar_parser)
    def do_renombrar(self, args: argparse.Namespace) -> None:
        try:
            if(resources.verificar_archivo(args.Archivo)):
                pathDestino = os.path.join(os.getcwd(),args.Nuevo_nombre)
                pathOrigen=os.path.abspath(args.Archivo)
                fileDest = open(pathDestino, 'w')
                fileOrigen = open(pathOrigen,'r')
                shutil.copy(pathOrigen,pathDestino)
                os.remove(pathOrigen)
                fileOrigen.close()
                fileDest.close()
                self.poutput(f'Archivo renombrado.')
            else:
                self.poutput(f'No es un archivo: {args.Archivo}.') 
        except Exception as error:
            msg=f'renombrar: {error}'
            self.poutput(colored(msg,'red'))
            logs.SystemError(msg)   
    
    #Pwd 
    pwd_parser = argparse.ArgumentParser(description='Mostar el directorio actual de trabajo.')
    @cmd2.with_argparser(pwd_parser)
    def do_pwd(self, args: argparse.Namespace) -> None:
        try:
            self.poutput(os.path.abspath(os.getcwd()))
        except Exception as error:
            msg=f'pwd: {error}'
            self.poutput(msg)
            logs.SystemError(msg)
    
    #listar
    listar_parser = argparse.ArgumentParser(description='Lista los archivos y directorios de un directorio determinado.')
    listar_parser.add_argument('Directorio_Destino',nargs='?',default='', type=str, help ='Directorio destino')
    @cmd2.with_argparser(listar_parser)
    def do_listar(self, args: argparse.Namespace) -> None:
        if(args.Directorio_Destino==''):
            args.Directorio_Destino=os.getcwd()
            self.poutput(args.Directorio_Destino)
        try:
            dirs = os.listdir(os.path.abspath(args.Directorio_Destino))
            for file in dirs:
               self.poutput(file)
        except Exception as error:
            msg=f'listar: {error}'
            self.poutput(colored(msg,'red'))
            logs.SystemError(msg)
    
    #creardir
    creardir_parser =argparse.ArgumentParser(description='Crear archivos.')
    creardir_parser.add_argument('Nombre_Archivo', type=str, nargs='*',help ='El nombre del archivo')
    @cmd2.with_argparser(creardir_parser)
    def do_creardir(self, args: argparse.Namespace) -> None:
        for arch in args.Nombre_Archivo:
            try:
                os.mkdir(arch)
            except Exception  as error:
                msg=f'creardir: {error}'
                self.poutput(colored(msg,'red'))
                logs.SystemError(msg)   

    #ir 
    ir_parser=argparse.ArgumentParser(description='Cambiar el directorio de trabajo actual de un usuario.')
    ir_parser.add_argument('Directorio_Destino',nargs='?', default='/', type=str, help ='Directorio destino')
    @cmd2.with_argparser(ir_parser)
    def do_ir(self, args: argparse.Namespace) -> None:
        try:
            os.chdir(os.path.abspath(args.Directorio_Destino))
        except Exception as error:
            msg=f'ir: {error}'
            self.poutput(colored(msg,'red'))
            logs.SystemError(msg)
    #permisos
    permiso_parser=argparse.ArgumentParser(description='Cambiar los permisos sobre un archivo o un directorio.')
    permiso_parser.add_argument('Permisos',type=str)
    permiso_parser.add_argument('Path',type=str)
    @cmd2.with_argparser(permiso_parser)
    def do_permiso(self, args: argparse.Namespace) -> None:
        try:
            os.path.abspath(args.Path)
            os.chmod(args.Path, int(args.Permisos,8))
        except Exception as error:
            msg=f'permiso: {error}'
            self.poutput(colored(msg,'red'))
            logs.SystemError(msg)
    #propietario
    propietario_parser=argparse.ArgumentParser(description='Cambiar los propietarios sobre un archivo o un conjunto de archivos.')
    propietario_parser.add_argument('UsuarioID',type=str,help='USUARIOID:[GRUPOID]')
    propietario_parser.add_argument('Archivos',nargs='*',type=str)
    @cmd2.with_argparser(propietario_parser)
    def do_propietario(self, args: argparse.Namespace) -> None:
        try:
            usuario=args.UsuarioID.split(':')
            for i in args.Archivos:
                os.chown(os.path.abspath(i),int(usuario[0]),int(usuario[1]))
        except Exception as error:
            msg=f'propietario: {error}'
            self.poutput(colored(msg,'red'))
            logs.SystemError(msg)
    #contraseña
    contrasena_parser=argparse.ArgumentParser(description='Cambiar la contraseña de un usuario.')
    contrasena_parser.add_argument('Usuario',nargs='?',default=getpass.getuser(),type=str,help='Usuario que desea cambiar la contraseña')
    @cmd2.with_argparser(contrasena_parser)
    def do_contrasena(self, args: argparse.Namespace) -> None:
        paths=["/etc/shadow","/etc/passwd"]
        if resources.check_string(args.Usuario,paths[1]):
            self.poutput(args.Usuario)   
            newPass=getpass.getpass("Introduzca una contraseña: ")
            tempNewPass=getpass.getpass("Vuelva a introducir la contraseña para confirmar: ")
            if newPass==tempNewPass:
                cryptpass=crypt.crypt(newPass,crypt.mksalt(crypt.METHOD_SHA512))

            else:
                self.poutput("Las contraseñas no coinciden.")   
        else:
            self.poutput("El usuario no existe.")
     
if __name__ == '__main__':
    import sys
    c = FirstApp()
    colorama.init(autoreset=True)
    if not os.path.exists('/var/log/shell'):
        #DANGER ZONE
        os.system('sudo mkdir /var/log/shell')
        os.system('sudo chmod -R 777  /var/log/shell')
    sys.exit(c.cmdloop())