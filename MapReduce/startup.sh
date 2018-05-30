# Eduard Fores Ferrer, Denys Sydorenko
# 7/04/2018 v1.0
# sh startup.sh

#!/bin/bash

# Fichero que utilizamos para iniciar el server.py, registry.py, host-x.py y reducer.py.

gnome-terminal -e "python -m SimpleHTTPServer"
gnome-terminal -e "python registry.py"
gnome-terminal -e "python reducer.py"
gnome-terminal -e "python host1.py"
gnome-terminal -e "python host2.py"
gnome-terminal -e "python host3.py"
gnome-terminal -e "python host4.py"
gnome-terminal -e "python server.py"
