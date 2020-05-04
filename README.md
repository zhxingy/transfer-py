# 原力流媒体直播流传输工具transferAPI的python封装

### 下载
```angular2
git clone https://github.com/zhxingy/transfer-py
```
### 安装
```angular2
python setup.py install
```
### 使用
```angular2
from transfer import Transfer, TransferError

ts = Transfer(service="http://127.0.0.1:8080", user="admin", password="admin")
try:
    print ts.index()
except TransferError as err:
    print err

```



