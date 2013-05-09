pabel
=====

Automation of PaDEL and OpenBabel/iBabel

Dependencies
- Python 2.7.3 
- PaDel Version
- OpenBabel 2.3.1 with Python-Bindings (py27-openbabel)

For Mac OS X Users:
It's recommended that you download OpenBabel through MacPorts.
There are several dependencies that OpenBabel requires, and it will be much faster this way.

sudo port install py27-openbabel

If you want to port an exisiting Python binary, simply add it to your PYTONPATH. This can be done by doing the following:
(1) Load the 'python2.7' binary (default for MacPorts)
(2) Type in 'import openbabel' and hit 'Enter'
(3) Type in 'openbabel.__file__' and hit 'Enter'. This should display the working directory for the library. .../site-packages
(4) Copy this directory and then use your favorite editor to ~/.profile
(5) Add: export PYTHONPATH=COPIED-SITE-PACKAGES-PATH:$PYTHONPATH
(6) Save and Exit.

