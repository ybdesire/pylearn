# package the main.py to exe

* py2 environment is better
* windows environment
* there is 3rd lib at main.py, such as sklearn


# Steps

* install pyinstaller by pip
* run `pyinstaller main.py --hidden-import sklearn.neighbors.typedefs`
* the get `main.exe` at dist/main, ~500M contents for dist/main
* copy `train.csv` and `test.csv` to `main.exe` path, then run exe directly at cmd



