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
|`-h`| Muestra la descripcion, uso, argumentos del comando |Si|
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
|`-h`| Muestra la descripcion, uso, argumentos del comando |Si|
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
|`-h`| Muestra la descripcion, uso, argumentos del comando |Si|
### Listar
Lista los archivos o directorios de una ruta especifica. Si no recibe argumento, lista los archivos y directorios de la carpeta actual.
```
listar [-h] [Directorio_Destino]
```
#### Argumentos
|Argumentos|Descripcion|Opcional|
|:---:|:---:|:---:|
|`Directorio_Destino`|Ruta de absoluta o relativa que se desea ver los archivos y directorios|Si|
|`-h`| Muestra la descripcion, uso, argumentos del comando |Si|
### Creardir
Crea un directorio, si se introduce mas de un nombre se crea por cada uno.
```
creardir [-h] Nombre_Directorio [Nombre_Directorio ...]
```
#### Argumentos
|Argumentos|Descripcion|Opcional|
|:---:|:---:|:---:|
|`Nombre_Directorio`|Nombre del nuevo directorio|No|
|`-h`| Muestra la descripcion, uso, argumentos del comando |Si|
### Ir
Cambia el directorio. Si no recibe argumentos, nos traslada al primer directorio '/'
```
ir [-h] [Directorio_Destino]
```
#### Argumentos
|Argumentos|Descripcion|Opcional|
|:---:|:---:|:---:|
|`Directorio_Destino`|Ruta de absoluta o relativa para el traslado |Si|
|`-h`| Muestra la descripcion, uso, argumentos del comando |Si|
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
|`-h`| Muestra la descripcion, uso, argumentos del comando |Si|
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

### Propietario
Cambia el propietario de uno o varios archivos, si se introduce mas de un archivo, se modificara el propietario de ese conjunto de archivos.
```
propietario [-h] UsuarioID:GrupoID Archivo [Archivo ...]
```
#### Argumentos
|Argumentos|Descripcion|Opcional|
|:---:|:---:|:---:|
|`UsuarioID:GrupoID`| id nuevo del usuario y del grupo que modificaremos |No|
|`Archivo`|Ruta de absoluta o relativa del archivo|No|
|`-h`| Muestra la descripcion, uso, argumentos del comando |Si|
### Contraseña
Cambia la contraseña de un usuario. Si no se recibe argumentos se modificara la contraseña del usuario actual. Solo el usuario root puede cambiar contraseña de otros usuarios.
```
contrasena [-h] [Usuario]
```
#### Argumentos
|Argumentos|Descripcion|Opcional|
|:---:|:---:|:---:|
|`Usuario`| Nombre del usuario que se modificara la contraseña |Si|
|`-h`| Muestra la descripcion, uso, argumentos del comando |Si|
### Pwd
Muestra la ruta del directorio actual en el se esta ubicado actualmente.
```
pwd [-h]
```
#### Argumentos
|Argumentos|Descripcion|Opcional|
|:---:|:---:|:---:|
|`-h`| Muestra la descripcion, uso, argumentos del comando |Si|

### kill
Terminar procesos con señales determinadas.
```
kill [-h] Sigkill PID
```
#### Argumentos
|Argumentos|Descripcion|Opcional|
|:---:|:---:|:---:|
|`Sigkill`|La señal que tenemos que enviar al comando kill |No|
|`PID`| Identificador del proceso |No|
|`-h`| Muestra la descripcion, uso, argumentos del comando |Si|
