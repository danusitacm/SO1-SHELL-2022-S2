# SO1-SHELL-2022-S2
## Integrantes 
- Daniela Cristaldo
- Yamil Padilla

## Manual de instalación.
Al iniciar el sistema LFS,ejecute el siguiente comando para poder ir a la raiz del sistema de archivos.
```sh
cd /
```
Si desea asegurarse de que se encuentra en la raiz,no dude en usar pwd para su verificacion.  
Clone el repositorio [SO1-SHELL-2022-S2](https://github.com/danusitacm/SO1-SHELL-2022-S2).
```sh
git clone https://github.com/danusitacm/SO1-SHELL-2022-S2.git
```
Conceda permiso al directorio /SO1-SHELL-2022-S2.
```sh
chmod -R 777 /SO1-SHELL-2022-S2
```
Luego prosiga a instalar las dependencias, para esto utilice el siguiente comando
```sh
pip install -r requirements.txt
```
<details><summary>Actualizacion de dependencias</summary>
<p>
Si desea actualizar las dependencias ejecute el comando
  
```sh
pip install --upgrade -r requirements.txt
```
</p>
</details>

Cree el script de ejecucion de la shell con el siguiente comando
```sh
cat > shell.sh << "EOF"
#!/bin/bash
cd /SO1-SHELL-2022-S2
python3 so1-sh.py
EOF
```
Ahora solo falta agregar la shell en /etc/profile
```sh
echo "bash /shell.sh" >> /etc/profile
```
Listo, reinicie el sistema.
```sh
shutdown -r 0
```
Cuando reinicie el sistema LFS vera algo como esto 
```sh
(Cmd) 
```
## Comandos
### Copiar
Copia un archivo o varios archivos en un directorio especificado por el usuario.
```
copiar [-h] Archivo [Archivo ...] Directorio_Destino
```
#### Argumentos
|Argumentos|Descripcion|Opcional|
|:---:|:---:|:---:|
|`Archivo`|El archivo que se desea copiar|No|
|`Directorio_destino`| Direccion donde se copiaran los archivos|No|
### Mover
Mueve un archivo o varios archivos en un directorio especificado por el usuario.
```
mover [-h] Archivo [Archivo ...] Directorio_Destino
```
#### Argumentos
|Argumentos|Descripcion|Opcional|
|:---:|:---:|:---:|
|`Archivo`|El archivo que se desea mover|No|
|`Directorio_Destino`| Direccion donde se moveran los archivos|No|
### Renombrar 
Cambia el nombre de un archivo.
```
renombrar [-h] Archivo Nuevo_Nombre
```
#### Argumentos
|Argumentos|Descripcion|Opcional|
|:---:|:---:|:---:|
|`Archivo`|El archivo que se desea renombrar o ruta del archivo|No|
|`Nuevo_Nombre`| El nuevo nombre del archivo|No|
