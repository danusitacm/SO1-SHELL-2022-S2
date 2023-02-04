import os
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
def RegHorario(message):
    __path__= '/var/log/shell/usuario_horario_log.log'
    resources.crearArchivos(__path__)
    os.system('chmod -R 777  /var/log/usuario_horario_log.log')
    try:
        log=logging.getLogger(getpass.getuser())
        log.setLevel(logging.WARNING)
        file=logging.FileHandler(__path__)
        file.setLevel(logging.WARNING)
        formato=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file.setFormatter(formato)
        log.addHandler(file)
        log.warning(message)
        log.removeHandler(file)
        file.flush()
        file.close()
    except:
        log.fatal("Error, no se pudo acceder al archivo sistema_error.log")