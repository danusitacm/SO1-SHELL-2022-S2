# SO1-SHELL-2022-S2
## Integrantes 
- Daniela Cristaldo
- Yamil 

## Manual de instalación.
Al iniciar el sistema LFS,ejecute el siguiente comando para poder ir a la raiz del sistema de archivos.
```sh
-bash-5.2# cd /
```
Si desea asegurarse de que se encuentra en la raiz,no dude en usar pwd para su verificacion.
Clone el repositorio [SO1-SHELL-2022-S2](https://github.com/danusitacm/SO1-SHELL-2022-S2).
```sh
-bash-5.2# git clone https://github.com/danusitacm/SO1-SHELL-2022-S2.git
```
Conceda permiso al directorio /SO1-SHELL-2022-S2.
```sh
-bash-5.2# chmod -R 777 /SO1-SHELL-2022-S2
```
Luego prosiga a instalar las dependencias, para esto utilice el siguiente comando
```sh
-bash-5.2# pip install -r requirements.txt
```
<details>
<p>
Si desea actualizar las dependencias ejecute el comando
  
```sh
-bash-5.2# pip install --upgrade -r requirements.txt
```
</p>
</details>

Cree el script de ejecucion de la shell con el siguiente comando
```sh
-bash-5.2# cat > shell.sh << "EOF"
#!/bin/bash
cd /SO1-SHELL-2022-S2
python3 so1-sh.py
EOF
```
Ahora solo falta agregar la shell en /etc/profile
```sh
-bash-5.2# echo "bash /shell.sh" >> /etc/profile
```
Listo todos los pasos reiniciamos el sistema.
```sh
-bash-5.2# shutdown -r 0
```
