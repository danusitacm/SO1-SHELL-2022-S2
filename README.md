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
|`Archivo`| Ruta de absoluta o relativa del archivo que se desea copiar|No|
|`Directorio_destino`| Ruta de absoluta o relativa del directorio|No|
### Mover
Mueve un archivo o varios archivos en un directorio especificado por el usuario.
```
mover [-h] Archivo [Archivo ...] Directorio_Destino
```
#### Argumentos
|Argumentos|Descripcion|Opcional|
|:---:|:---:|:---:|
|`Archivo`|Ruta de absoluta o relativa del archivo que se desea copiar|No|
|`Directorio_Destino`|Ruta de absoluta o relativa del directorio|No|
### Renombrar 
Cambia el nombre de un archivo.
```
renombrar [-h] Archivo Nuevo_Nombre
```
#### Argumentos
|Argumentos|Descripcion|Opcional|
|:---:|:---:|:---:|
|`Archivo`|Ruta de absoluta o relativa del archivo que se desea copiar|No|
|`Nuevo_Nombre`| El nuevo nombre del archivo|No|
### Listar
Lista los archivos o directorios de una ruta especifica. Si no recibe argumento, lista los archivos y directorios de la carpeta actual.
```
listar [-h] [Directorio_Destino]
```
#### Argumentos
|Argumentos|Descripcion|Opcional|
|:---:|:---:|:---:|
|`Directorio_Destino`|Ruta de absoluta o relativa que se desea ver los archivos y directorios|Si|
### Creardir
Crea un directorio, si se introduce mas de un nombre se crea por cada uno.
```
creardir [-h] Nombre_Directorio [Nombre_Directorio ...]
```
#### Argumentos
|Argumentos|Descripcion|Opcional|
|:---:|:---:|:---:|
|`Nombre_Directorio`|Nombre del nuevo directorio|No|
### Ir
Cambia el directorio. Si no recibe argumentos, nos traslada al primer directorio '/'
```
ir [-h] [Directorio_Destino]
```
#### Argumentos
|Argumentos|Descripcion|Opcional|
|:---:|:---:|:---:|
|`Directorio_Destino`|Ruta de absoluta o relativa para el traslado |Si|
### Permisos
Asigna o modifica permisos a un archivo o carpeta.
```
permisos [-h] Permisos Directorio_Destino
```
#### Argumentos
|Argumentos|Descripcion|Opcional|
|:---:|:---:|:---:|
|`Permisos`| Permisos que se le asignara al archivo o directorio |No|
|`Directorio_Destino`|Ruta de absoluta o relativa del archivo o directorio |No|
<details><summary>Permisos en numeros</summary>
<p>

- 0 = --- = sin acceso
- 1 = --x = ejecución
- 2 = -w- = escritura
- 3 = -wx = escritura y ejecución
- 4 = r-- = lectura
- 5 = r-x = lectura y ejecución
- 6 = rw- = lectura y escritura
- 7 = rwx = lectura, escritura y ejecución

</p>
</details>
