## Configuracion de entorno Ubuntu-Qtile
### Lista de aplicaciones
1. [Qtile](#qtile)
1. [Alacritty](#alacritty)
1. [Rofi](#rofi)
1. [Feh](#feh)
1. [Nerd fonts ubuntu mono](#nerd-fonts-ubuntu-mono)
1. E

### Qtile
Un administrador de ventanas de mosaico hackable y con todas las funciones escrito y configurado en Python [link](http://www.qtile.org/)
```
sudo apt update
sudo apt install python3
sudo apt install pip3

# dependencias para user qtile
sudo apt install python-gobject 
sudo apt install python-dbus
```

**Usar qtile en un entorno virual con venv.**
```
# install venv
sudo apt install python3-venv

# create a virtalenv
python3 -m venv venv

# active virtalenv
source ~/[path]/venv/bin/activate
```

**Instalar PyBObject**
```
Instrucciones en [aqui](https://pygobject.readthedocs.io/en/latest/getting_started.html#ubuntu-getting-started)
```

**Teniendo acivo el entorno virtual, instalamos qtile**
```
pip install xcffib
pip install --no-cache-dir cairocffi
pip install qtile
```

**Configurar accesos para inicar sesion con qtile**
```
# Configurar el path del venv en el archivo 'qtile-venv-entry'
# Cambiar a la ruta donde se encuentre el entorno virtual
source ~/local/qtile/venv/bin/activate

# Configurar path del archivos qtile-venv.desktop
Exec=/home/foo/local/qtile/qtile-venv-entry

# Copiar el archivo qtile-venv.desktop a la ruta '/usr/share/xsessions'
sudo cp qtile-venv.desktop /usr/share/xsessions
```

### Alacritty
Alacritty un emulador de terminal, acelerado con gpu. [link](https://github.com/alacritty/alacritty)

```
# Install
# agregar repositorio
sudo add-apt-repository ppa:mmstick76/alacritty
sudo apt update
sudo apt install alacritty
```
Alternativa para instalar alacritty desde el codigo fuente [link](https://github.com/alacritty/alacritty/blob/master/INSTALL.md#prerequisites).

## Rofi
Rofi es un selector de ventanas, diálogo de ejecución, lanzador ssh y reemplazo de dmenu [link](https://github.com/davatorium/rofi)
```
sudo apt install rofi
```

## Feh
feh es un visor de imágenes liviano y poderoso que también se puede usar para administrar el fondo de escritorio para administradores de ventanas independientes que carecen de tales características.
```dotnetcli
sudo apt install feh
feh --bg-scale ruta/al/fondo/de/pantalla
```

## Nerd fonts ubuntu mono
Fuente de iconos
Descargar fuente en [link](https://www.nerdfonts.com/font-downloads)
```dotnetcli
# install 
unzip UbuntuMono.zip -d ~/.fonts
fc-cache -fv
```

Para buscar los iconos y copiar [aqui](https://www.nerdfonts.com/cheat-sheet)

## Extras
Instalar dependencias
```
# icono de volumen
sudo apt install volumeicon-alsa

# velocidad de red
pip install psutil
```
