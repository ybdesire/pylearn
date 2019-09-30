# environment setup

0. windows10 + python3
1. download android simulator (http://mumu.163.com/)
2. pip install uiautomator
3. add adb path to environment variable (I installed AndroidStudio here)

```
C:\Users\xxx\AppData\Local\Android\Sdk\platform-tools
```

4. start android simulator, then connect by adb

```
adb connect 127.0.0.1:7555
```

# usage

* https://github.com/xiaocong/uiautomator

e.g. open QQ at android simulator

```
from uiautomator import device as d

d.screen.on()
d(text="QQ").click()
```

