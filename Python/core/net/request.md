# Request

网络请求库的使用

网络请求通常分为四种类型: `GET`, `POST`, `PUT`, `DELETE`

- `GET`: 从服务器获取数据
- `POST`: 向服务器提交数据
- `PUT`: 修改服务器数据
- `DELETE`: 删除服务器数据

## requests

### 安装

```shell
pip install requests
```

### 使用

```python
import requests
```

### get()

`get()`方法用于发送get请求

```python
url = "https://www.baidu.com"
requests.get(url=url, params=None, **kwargs)
```

- param: url: 请求的url
- param: params: 请求的参数
- param: **kwargs: 其他参数
- return: Response

一个简单的例子，从api获取数据

```python
import requests

url = "https://api.ipify.org"

response = requests.get(url=url)

print(response.text)
```

result:

```shell
"***.***.***.***"   # ip地址
```

### post()

`post()`方法用于发送post请求

```python
url = "https://www.baidu.com"
requests.post(url=url, data=None, json=None, **kwargs)
```

- param: url: 请求的url
- param: data: 请求的数据
- param: json: 请求的json数据
- param: **kwargs: 其他参数

一个简单的例子，向api提交数据

```python
import requests
import json

url = "https://postman-echo.com/post"   # postman提供的测试api, 会返回提交的数据
data = {
    "name": "张三",
    "age": 18
}

response = requests.post(url=url, data=data)
json_data = json.loads(response.text)
print(json_data["json"])

```

result:

```json
{'name': '张三', 'age': '18'}
```
