# Pac Macro Demo

Python 3 scripts which automate player movement on a Pac Macro server for demonstration purposes.

## Components

No external libraries are required.

The `scripts/pacmacro/api.py` module contains everything you need to interact with the Pac Macro server.

## Setup

Navigate into the configuration directory:
```
cd scripts/cfg/
```

Create a new configuration file named `target-server.cfg` which will not be tracked by Git. You may create your own using the provided file `target-server.cfg.template` or reuse a provided config - for example:
```
cp target-server.cfg.heroku target-server.cfg
```

Exit the configuration directory:
```
cd ..
```

Once you have finished editing the configurations, choose any script in the `scripts/` to execute - for example:
```
./pacman_borders_nesw.py
```

### Default Behaviour

By default:
* `blinky.py` moves along Georgia Street, between Richards and Hornby,
* `clyde.py` moves along Granville Street, between Georgia and Pender,
* `inky.py` moves along Dunsmuir Street, between Howe and Seymour,
* `pinky.py` moves along Pender Street, between Hornby and Richards, and
* `pacman.py` encircles all 4 borders of the grid created by the above characters.