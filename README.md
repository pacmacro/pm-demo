# Pac Macro Demo

Python 3 scripts which automate player movement on a Pac Macro server for demonstration purposes.

## Components

No external libraries are required.

The `pacmacro.py` module contains everything you need to interact with the Pac Macro server. The `template.py` script is an example for how to use the `pacmacro` module to move a player around, and is a great start if you'd like to make your own player demonstration scripts

## Setup

To start using the scripts provided, choose any script other than `pacmacro.py` or `template.py`. Edit the script to set the configurations for the server which the demo will be performed on, which player will be moved, and where the player will move from/to. By default, the scripts are configured for a server running on `localhost:8080`.

Once you have finished editing the configurations, simply execute the script:
```
./pacman_borders_nesw.py
```
