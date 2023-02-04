import os
import time
import logging
import getpass
import resources
def SystemError(message):
    __path__= '/var/log/shell/sistema_error.log'
    resources.crearArchivos(__path__)
    os.system('chmod -R 777  /var/log/shell/sistema_error.log')
    try:
        log=logging.getLogger(getpass.getuser())
        log.setLevel(logging.ERROR)
        file=logging.FileHandler(__path__)
        file.setLevel(logging.ERROR)
        formato=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file.setFormatter(formato)
        log.addHandler(file)
        log.error(message)
        log.removeHandler(file)
        file.flush()
        file.close()
    except:
        log.fatal("Error, no se pudo acceder al archivo sistema_error.log")
def RegComandos(message):
    __path__= '/var/log/shell/comando.log'
    resources.crearArchivos(__path__)
    os.system('chmod -R 777  /var/log/shell/comando.log')
    try:
        log=logging.getLogger(getpass.getuser())
        log.setLevel(logging.DEBUG)
        file=logging.FileHandler(__path__)
        file.setLevel(logging.DEBUG)
        formato=logging.Formatter('%(asctime)s - %(name)s - %(message)s')
        file.setFormatter(formato)
        log.addHandler(file)
        log.debug(message)
        log.removeHandler(file)
        file.flush()
        file.close()
    except:
        log.fatal("Error, no se pudo acceder al archivo comando.log")
def Transferencias(message,status):
    __path__= '/var/log/shell/Shell_transferencias.log'
    resources.crearArchivos(__path__)
    os.system('chmod -R 777  /var/log/shell/Shell_transferencias.log')
    try:
        if status=='INFO':
            log=logging.getLogger(getpass.getuser())
            log.setLevel(logging.INFO)
            file=logging.FileHandler(__path__)
            file.setLevel(logging.INFO)
            formato=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file.setFormatter(formato)
            log.addHandler(file)
            log.info(message)
            log.removeHandler(file)
            file.flush()
            file.close()
        elif status=='ERROR':
            log=logging.getLogger(getpass.getuser())
            log.setLevel(logging.ERROR)
            file=logging.FileHandler(__path__)
            file.setLevel(logging.ERROR)
            formato=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file.setFormatter(formato)
            log.addHandler(file)
            log.error(message)
            log.removeHandler(file)
            file.flush()
            file.close()
    except:
        log.fatal("Error, no se pudo acceder al archivo Shell_transferencias.log")
def RegHorarios(status):
    info = resources.obtenerFilaUsuario(getpass.getuser(),'/etc/passwd',':',5)
    info_user = info[4].split(' ')
    if info_user:
        horario = info_user[0].split(',')
    __path__= '/var/log/shell/usuario_horarios_log.log'
    resources.crearArchivos(__path__)
    try:
        message =''
        if status == 'inicio':
            message = f"inicio sesion"
        else:
            message = f"cerro sesion"
        if horario:    
            if horario[0] <= time.struct_time.tm_hour <= horario[1] :
                message = f"{message} - fuera de horario"
        log=logging.getLogger(getpass.getuser())
        log.setLevel(logging.WARNING)
        file=logging.FileHandler(__path__)
        file.setLevel(logging.WARNING)
        formato=logging.Formatter('%(asctime)s - %(name)s - %(message)s')
        file.setFormatter(formato)
        log.addHandler(file)
        log.debug(message)
        log.removeHandler(file)
        file.flush()
        file.close()
    except:
        log.fatal("Error, no se pudo acceder al archivo usuario_horarios_log.log")