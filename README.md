# Transfer API for python

### 下载
```angular2
git clone https://github.com/zhxingy/transfer-py
```
### 安装
```angular2
python setup.py install
```

### 测试
```
from transfer import TEST

if __name__ == '__main__':
    test = TEST(service="http://127.0.0.1:8080", user="admin", password="admin")
    test.run()
```

### 简单使用
```angular2
from transfer import Transfer, TransferError

if __name__ == '__main__':
    ts = Transfer(service="http://127.0.0.1:8080", user="admin", password="admin")
    try:
        print ts.index()
    except TransferError as err:
        print err

```

### [文档](https://github.com/zhxingy/transfer-py/blob/master/API.md)
