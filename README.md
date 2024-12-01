# xiaLotus-pyqt_aiohttp_selenium_embed
python3.11.3備份用


### 使用方式

```bash=
cd python-3.11.3

pip list
```

### download pip

##### 把 requirement.txt 挪到 python-3.11.1裡面


```bash=
cd Scripts

python.exe -m pip install -r requirement.txt
```

這樣就可以直接下載完畢

### 測試
輸入
```bash=
cd \python-3.11.3\Scripts

pip list
```


### requirement.txt
放在 `python-3-11.3` 裡面，可以直接下載


### 打包

```bash=
.\python-3.11.3\python.exe -m PyInstaller --onefile --windowed --hidden-import=selenium --hidden-import=PyQt5 pyqt_test.py
```

### 基本運行
使用方式：

```bash=
.\\python-3.11.3\python.exe ./{檔名}.py
```