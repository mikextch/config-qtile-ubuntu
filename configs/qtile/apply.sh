#!/bin/bash

PATH_QTILE=~/.config/qtile
FILE_CONFIG_DEFAULT_COPY=~/.config/qtile/config-default.py
FILE_CONFIG_DEFAULT=~/.config/qtile/config.py


if [ -f "$FILE_CONFIG_DEFAULT_COPY" ]; then
    echo "$FILE_CONFIG_DEFAULT_COPY exists"
else
    echo "no existe creando..."
    cp $FILE_CONFIG_DEFAULT $FILE_CONFIG_DEFAULT_COPY
fi

cp config.py $PATH_QTILE
cp autostart.sh $PATH_QTILE
cp -r settings $PATH_QTILE
cp -r themes $PATH_QTILE

cd $PATH_QTILE
chmod +x autostart.sh
