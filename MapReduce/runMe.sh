#!/bin/bash

gnome-terminal -e "python registry.py"
gnome-terminal -e "python host1.py"
gnome-terminal -e "python host2.py"
gnome-terminal -e "python host3.py"
gnome-terminal -e "python reducer.py"
gnome-terminal -e "python server.py"
