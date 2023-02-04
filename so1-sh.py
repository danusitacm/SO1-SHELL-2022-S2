#!/usr/bin/env python
"""A simple cmd2 application."""
import resources
import cmd2
import argparse
import os
import shutil
import os.path
import getpass
import crypt
import hashlib
import logs
from ftplib import FTP
from os import path
import shutil
from pathlib import Path

class FirstApp(cmd2.Cmd):
    """A simple cmd2 application."""
    delattr(cmd2.Cmd,'do_set')
    def __init__(self):
        super().__init__()
        builtin_commands=['alias','edit','py','run_pyscript','run_script','shortcuts','macro','shell']
        self.hidden_commands.extend(builtin_commands) #Para esconder los Builtin Commands  
    def onecmd(self, s,**kwargs):
        comando=s.raw
        logs.RegComandos(comando)
        return cmd2.Cmd.onecmd(self,s,**kwargs)    
    #COMANDOS BASICOS
    #Copiar
    cop_parser = argparse.ArgumentParser(description='Copiar un archivo en un directorio determinado.')
    cop_parser.add_argument('Archivo', type=str ,nargs='+',help = 'Los archivos a utilizar')
    cop_parser.add_argument('Directorio_Destino', type=str, help = 'Directorio destino')
    @cmd2.with_argparser(cop_parser)
    def do_copiar(self, args: argparse.Namespace) -> None:
        try:
            pathDestino = os.path.abspath(args.Directorio_Destino)
            for arch in args.Archivo:
                pathOrigen=os.path.abspath(arch)
                pathDestino = os.path.join(pathDestino,arch)
                fileDest = open(pathDestino, 'w')
                fileOrigen = open(pathOrigen,'r')
                shutil.copy(pathOrigen,pathDestino)
                fileOrigen.close()
                fileDest.close()
                self.poutput(f'Archivo {arch} copiado.')   
        except Exception as error:
            msg=f'copiar: {error}'
            self.perror(msg)
            logs.SystemError(msg)
    #Mover
    mov_parser = argparse.ArgumentParser(description='Mover un archivo a un directorio determinado.')
    mov_parser.add_argument('Archivo', type=str,nargs='+',help = 'Los archivos a utilizar')
    mov_parser.add_argument('Directorio_Destino',type=str, help = 'Directorio destino')
    @cmd2.with_argparser(mov_parser)
    def do_mover(self, args: argparse.Namespace) -> None:
        try:
            pathDestino = os.path.abspath(args.Directorio_Destino)
            for arch in args.Archivo:
                pathOrigen=os.path.abspath(arch)
                pathDestino = os.path.join(pathDestino,arch)
                fileDest = open(pathDestino, 'w')
                fileOrigen = open(pathOrigen,'r')
                shutil.copy(pathOrigen,pathDestino)
                os.remove(pathOrigen)
                fileOrigen.close()
                fileDest.close()
                self.poutput(f'Archivo {arch} movido.')
        except Exception as error:
            msg=f'mover: {error}'
            self.perror(msg)
            logs.SystemError(msg)        
    #Renombrar
    renombrar_parser = argparse.ArgumentParser(description='Renombrar un archivo.')
    renombrar_parser.add_argument('Archivo', type=str,help = 'Archivo a renombrar.')
    renombrar_parser.add_argument('Nuevo_Nombre' ,type=str, help = 'Nuevo nombre del archivo.')
    @cmd2.with_argparser(renombrar_parser)
    def do_renombrar(self, args: argparse.Namespace) -> None:
        try:
            pathDestino = os.path.join(os.getcwd(),args.Nuevo_Nombre)
            pathOrigen=os.path.abspath(args.Archivo)
            fileDest = open(pathDestino, 'w')
            fileOrigen = open(pathOrigen,'r')
            shutil.copy(pathOrigen,pathDestino)
            os.remove(pathOrigen)
            fileOrigen.close()
            fileDest.close()
            self.poutput(f'Archivo renombrado.')
        except Exception as error:
            msg=f'renombrar: {error}'
            self.perror(msg)
            logs.SystemError(msg)   
    #Pwd 
    pwd_parser = argparse.ArgumentParser(description='Mostar el directorio actual de trabajo.')
    @cmd2.with_argparser(pwd_parser)
    def do_pwd(self, args: argparse.Namespace) -> None:
        try:
            self.poutput(os.path.abspath(os.getcwd()))
        except Exception as error:
            msg=f'pwd: {error}'
            self.perror(msg)
            logs.SystemError(msg)
    history_parser = argparse.ArgumentParser(description='Mostar el directorio actual de trabajo.')
    @cmd2.with_argparser(history_parser)
    def do_history(self, args: argparse.Namespace) -> None:
        try:
            temp_f=open('/var/log/shell/comando.log','r')
            for line in temp_f:
                temp_line=line.split(' ',5)
                self.poutput(temp_line[5].rstrip('\n'))
        except Exception as error:
            msg=f'history: {error}'
            self.perror(msg)
            logs.SystemError(msg)
    #listar
    listar_parser = argparse.ArgumentParser(description='Lista los archivos y directorios de un directorio determinado.')
    listar_parser.add_argument('Directorio_Destino',nargs='?',default='', type=str, help ='Directorio destino')
    @cmd2.with_argparser(listar_parser)
    def do_listar(self, args: argparse.Namespace) -> None:
        if(args.Directorio_Destino==''):
            args.Directorio_Destino=os.getcwd()
        try:
            dirs = os.listdir(os.path.abspath(args.Directorio_Destino))
            for file in dirs:
               self.poutput(file)
        except Exception as error:
            msg=f'listar: {error}'
            self.perror(msg)
            logs.SystemError(msg)
    
    #creardir
    creardir_parser =argparse.ArgumentParser(description='Crear directorios.')
    creardir_parser.add_argument('Nombre_Directorio',type=str,nargs='+',help ='El nombre del directorio')
    @cmd2.with_argparser(creardir_parser)
    def do_creardir(self, args: argparse.Namespace) -> None:
        for arch in args.Nombre_Directorio:
            try:
                os.mkdir(arch)
            except Exception  as error:
                msg=f'creardir: {error}'
                self.perror(msg)
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
            self.perror(msg)
            logs.SystemError(msg)
    #kill
    kill_parser=argparse.ArgumentParser(description='Terminar procesos.')
    kill_parser.add_argument('Sigkill',default='9', type=int,help ='Señales para enviar a los procesos.')
    kill_parser.add_argument('PID',type=int,help='ID del proceso')
    @cmd2.with_argparser(kill_parser)
    def do_kill(self, args: argparse.Namespace) -> None:
        try:
            os.kill(args.PID,args.Sigkill)
            msg=f'kill: Se mato al proceso de PID:  {args.PID}'
            self.poutput(msg)
        except Exception as error:
            msg=f'kill: {error}'
            self.perror(msg)
            logs.SystemError(msg)
    #permisos
    permiso_parser=argparse.ArgumentParser(description='Cambiar los permisos sobre un archivo o un directorio.')
    permiso_parser.add_argument('Permisos',type=str)
    permiso_parser.add_argument('Directorio_Destino',type=str)
    @cmd2.with_argparser(permiso_parser)
    def do_permisos(self, args: argparse.Namespace) -> None:
        try:
            os.path.abspath(args.Directorio_Destino)
            os.chmod(args.Directorio_Destino, int(args.Permisos,8))
        except Exception as error:
            msg=f'permiso: {error}'
            self.perror(msg)
            logs.SystemError(msg)
    #propietario
    propietario_parser=argparse.ArgumentParser(description='Cambiar los propietarios sobre un archivo o un conjunto de archivos.')
    propietario_parser.add_argument('UsuarioID',type=str,help='USUARIOID:[GRUPOID]')
    propietario_parser.add_argument('Archivo',nargs='+',type=str)
    @cmd2.with_argparser(propietario_parser)
    def do_propietario(self, args: argparse.Namespace) -> None:
        try:
            usuario=args.UsuarioID.split(':')
            for i in args.Archivo:
                shutil.chown(os.path.abspath(i),int(usuario[0]),int(usuario[1]))
        except Exception as error:
            msg=f'propietario: {error}'
            self.perror(msg)
            logs.SystemError(msg)
     #contraseña
    contrasena_parser=argparse.ArgumentParser(description='Cambiar la contraseña de un usuario.')
    contrasena_parser.add_argument('Usuario',nargs='?',default=getpass.getuser(),type=str,help='Usuario que desea cambiar la contraseña')
    @cmd2.with_argparser(contrasena_parser)
    def do_contrasena(self, args: argparse.Namespace) -> None:
        try:
            newPass=getpass.getpass("Introduzca una contraseña: ")
            tempNewPass=getpass.getpass("Vuelva a introducir la contraseña para confirmar: ")
            if newPass==tempNewPass:
                cryptpass=crypt.crypt(newPass,crypt.mksalt(crypt.METHOD_SHA512)) 
                usuShadow=resources.obtenerFilaUsuario(args.Usuario,"/etc/shadow",':',3)
                usuShadow.pop(1)
                usuShadow.insert(1,cryptpass)
                resources.guardarFilaUsuario(args.Usuario,"/etc/shadow",resources.unirArray(usuShadow,':'))
                self.poutput("Se cambio la contraseña, exitosamente!!")
            else:
                msg=f'contrasena: Las contraseñas no coinciden.'
        except Exception as error:
            msg=f'contrasena: {error}'
        finally:
            self.perror(msg)
            logs.SystemError(msg)
    #grep
    grep_parser = argparse.ArgumentParser(description='Buscar un string en un archivo.')
    grep_parser.add_argument('String', type=str,nargs=1,help = 'String a buscar')
    grep_parser.add_argument('Archivo', type=str,nargs=1,help = 'Archivo en donde se busca')
    @cmd2.with_argparser(grep_parser)
    def do_grep(self, args: argparse.Namespace) -> None:
        try:
             for arch in args.Archivo:
                Lineas_encontradas = []
                path=os.path.abspath(arch)
                file = open(path,'r')
                numero_linea = 0
                for linea in file:
                    numero_linea += 1
                    linea = linea.rstrip()
                    Lista_palabras = linea.split(" ")
                    for Palabra in args.String:
                        if Palabra in Lista_palabras:
                            Lineas_encontradas.append(str(numero_linea) + " - " + linea)
                    file.close
                for linea in Lineas_encontradas:
                    self.poutput(linea)
        except Exception as error:
            msg=f'grep: {error}'
            self.perror(msg)
            logs.SystemError(msg)
    #ftp
    ftp_parser = argparse.ArgumentParser(description='Transferencia por FTP.')
    ftp_parser.add_argument('Accion',type=str,choices=['subir','descargar','listar','eliminar'],help='La accion que se desea realizar en el servidor.')
    ftp_parser.add_argument('Archivo',type=str,default=' ',nargs='?',help='Archivo que se desea subir')
    @cmd2.with_argparser(ftp_parser)
    def do_ftp(self, args: argparse.Namespace) -> None:
        try:
            # ftpHostname=input("Ingrese el host: ")
            # ftpUser=input("Ingrese el nombre de usuario: ")
            # ftpPasswd=getpass.getpass()
            ftpHostname='ftp.dlptest.com'
            ftpUser='dlpuser'
            ftpPasswd='rNrKYTX9g7z3RgJRmxWuGHbeu'
            with FTP(ftpHostname) as ftp:            
                ftpMsg=ftp.login(ftpUser,ftpPasswd)
                self.poutput(ftpMsg)
                logs.Transferencias(ftpMsg,'INFO')
                if args.Accion=='subir':
                    with open(args.Archivo,'rb') as file:
                        ftpMsg=ftp.storbinary(f'STOR {args.Archivo}',file)
                    self.poutput(f'ftp: {ftpMsg}')
                    logs.Transferencias(f'{ftpMsg} File: {args.Archivo}','INFO')
                    self.poutput(ftp.dir())
                elif args.Accion=='descargar':
                    with open(args.Archivo,'wb') as file:
                        ftpMsg=ftp.retrbinary(f'RETR {args.Archivo}',file.write)
                    logs.Transferencias(f'{ftpMsg} File: {args.Archivo}','INFO')
                    self.poutput(f'ftp: {ftpMsg}')
                    self.poutput('Archivo descargado:')
                    resources.leerArch(args.Archivo)
                elif args.Accion=='listar':
                    self.poutput(ftp.dir())
                    ftpMsg='Se listo correctamente los archivos.'
                    self.poutput(f'ftp: {ftpMsg}')
                    logs.Transferencias(f'{ftpMsg}','INFO')
                elif args.Accion=='eliminar':
                    ftpMsg=ftp.delete(args.Archivo)
                    self.poutput(f'ftp: {ftpMsg}')
                    logs.Transferencias(f'{ftpMsg} File: {args.Archivo}','INFO')
        except Exception as error:
            msg=f'ftp: {error}'
            self.perror(msg)
            logs.SystemError(msg)
            logs.Transferencias(msg,'ERROR')
    #Demonio
    demonio_parser =argparse.ArgumentParser(description='Manipulacion de demonios del sistema.')
    demonio_parser.add_argument('Accion',type=str,choices=['levantar','apagar','listar'],help='La accion que se desea realizar con los demonios.')
    demonio_parser.add_argument('Nombre',type=str,default=' ',nargs='?',help='Nombre del demonio')
    @cmd2.with_argparser(propietario_parser)
    def do_propietario(self, args: argparse.Namespace) -> None:
        try:
            if(os.getuid==0):
                if args.Accion=='levantar':
                    print('l')   
                elif args.Accion=='apagar':
                    print('a')
                elif args.Accion=='listar':
                    print('l2')
            else:
                    msg=f'demonio: El usuario no tiene los permisos suficientes.'
        except Exception as error:
            msg=f'propietario: {error}'
            self.perror(msg)
            logs.SystemError(msg)
    #usuario
    usuario_parser = argparse.ArgumentParser(description='Agrega un usuario.')
    usuario_parser.add_argument('Usuario', type=str,nargs=1,help = 'Nombre de usuario')
    usuario_parser.add_argument('-i','--ip',default=' ',type=str,nargs=1,help = 'Ips permitidas (separadas por comas)')
    usuario_parser.add_argument('-ho','--horario',default=' ',type=str,nargs=1,help = 'Horario permitido (horainicio,horasalida)')
    @cmd2.with_argparser(usuario_parser)
    def do_usuario(self, args: argparse.Namespace) -> None:
        try:
            if not resources.check_string(args.Usuario[0],"/etc/passwd"):
                UID = resources.NewUID()
                GID = resources.NewGID()
                os.system('chmod -R 777  /etc/passwd')
                os.system('chmod -R 777  /etc/group')
                homedir = f"/home/{args.Usuario[0]}"
                lineausu =f"\n{args.Usuario[0]}:x:{UID}:{GID}:{args.ip} {args.horario}:{homedir}:/bin/bash"
                lineagro =f"\n{args.Usuario[0]}:x:{GID}:"
                with open("/etc/group",'a') as tem_f:
                    tem_f.write(lineagro)
                with open("/etc/passwd",'a') as tem_f:
                    tem_f.write(lineausu)
                os.system('chmod 777 /home')
                os.mkdir(homedir)
                os.system('chmod 755 /home')
                os.system(f'chmod -R 777 {homedir}')
                self.poutput(f'Usuario creado correctamente')
                os.system('chmod -R 644  /etc/passwd')
                os.system('chmod -R 644  /etc/group')
            else:
                msg=f'usuario: El usuario {args.Usuario} ya existe.'      
        except Exception as error:
            msg=f'usuario: {error}'
            self.perror(msg)
            logs.SystemError(msg)
if __name__ == '__main__':
    import sys
    c = FirstApp()
    if not os.path.exists('/var/log/shell'):
        #DANGER ZONE
        os.system('mkdir /var/log/shell')
        os.system('chmod -R 777  /var/log/shell')
    sys.exit(c.cmdloop())
