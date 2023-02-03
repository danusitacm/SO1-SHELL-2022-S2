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

