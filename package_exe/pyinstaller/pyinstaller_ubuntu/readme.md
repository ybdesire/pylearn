# code structure


* main logic codes: main.py is main function, which has dependence myadd.py
* test.py: test output by run command


# steps


```
(envtf) root@user-OptiPlex-xxx:/home/xxx/tmp2019/pyinstaller_test_ubuntu# python main.py
final result is 13
(envtf) root@user-OptiPlex-xxx:/home/xxx/tmp2019/pyinstaller_test_ubuntu# pyinstaller --onefile main.py
72 INFO: PyInstaller: 3.4
****
6731 INFO: Building COLLECT COLLECT-00.toc
6928 INFO: Building COLLECT COLLECT-00.toc completed successfully.

(envtf) root@user-OptiPlex-xxx:/home/xxx/tmp2019/pyinstaller_test_ubuntu# ls
build  dist  main.py  main.spec  myadd.py  __pycache__  readme.md
(envtf) root@user-OptiPlex-xxx:/home/xxx/tmp2019/pyinstaller_test_ubuntu# cd dist/
(envtf) root@user-OptiPlex-xxx:/home/xxx/tmp2019/pyinstaller_test_ubuntu/dist# ls
main
(envtf) root@user-OptiPlex-xxx:/home/xxx/tmp2019/pyinstaller_test_ubuntu/dist# ./main
final result is 13

```


# multiple file to one elf

```
pyinstaller -F  -w main.py -p fea_ext.py -p model.jl
```
