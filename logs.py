import os
import logging
import getpass
import resources
def SystemError(message):
    __path__= '/var/log/shell/sistema_error.log'
    resources.crearArchivos(__path__)
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
#No pude implementar todavia
def RegComandos(message):
    __path__= '/var/log/shell/comando.log'
    resources.crearArchivos(__path__)
    try:
        log=logging.getLogger(getpass.getuser())
        log.setLevel(logging.DEBUG)
        file=logging.FileHandler(__path__)
        file.setLevel(logging.DEBUG)
        formato=logging.Formatter('%(asctime)s - %(message)s')
        file.setFormatter(formato)
        log.addHandler(file)
        log.error(message)
        log.removeHandler(file)
        file.flush()
        file.close()
    except:
        log.fatal("Error, no se pudo acceder al archivo comando.log")