## requests简介

​	requests模块是在urllib的基础上编写的, 采用的是Apache2 Licensed开源协议的HTTP库. 与urllib相比较, requests模块使用起来更加方便, 但安装好python之后没有该模块, 故使用requests模块需要单独安装.

## requests详解

一个使用requests模块的简单示例:

```python
import requests

url = 'http://www.baidu.com'

# 响应对象
response = requests.get(url)

# 响应状态码
print(response.status_code)
# 响应字符串
print(response.text)
# 响应字节串
print(response.content)
print(response.content.decode('utf-8'))
# 响应头
print(response.headers)
# cookies
print(response.cookies)
```

​	这里有一个需要注意的地方, 有些网站直接用`response.text`返回数据时会出现乱码问题, 解决方法有两种. 一种是使用`response.content`返回数据, 这里返回的是二进制格式, 通过decode可以转换为utf-8; 另一种是找出requests使用的编码方式, 并改变`response.encoding`属性, `response.encoding = 'utf-8'`. 这是因为当请求发出以后, requests会根据http头部对响应的编码做推测, 当访问`response.text`时, requests会使用推测的文本编码.

### 各种请求方式

```python
requests.get('http://httpbin.org/get')
requests.post('http://httpbin.org/post')
requests.put('http://httpbin.org/put')
requests.delete('http://httpbin.org/delete')
requests.head('http://httpbin.org/get')
requests.options('http://httpbin.org/get')
```

### GET请求

```python
# 基本get请求
response = requests.get('http://httpbin.org/get')
print(response.text)


# 带参数的get请求1
response = requests.get('http://httpbin.org/get?name=lau&age=24')
print(response.text)

# 带参数的get请求2
data = {'name': None, 'age': 24}
response = requests.get('http://httpbin.org/get', params=data)
print(response.url)         # http://httpbin.org/get?age=24
print(response.text)        # args中会传入data

# 两种方式的区别是, 当通过params参数传递一个字典内容时, 如果字典中的参数为None, 不会添加到url上
```

### 解析json

```python
response = requests.get('http://httpbin.org/get')
print(type(response.text))          # str

# 解析json1
print(response.json())
print(type(response.json()))        # dict

# 解析json2
print(json.loads(response.text))    # dict
```

### 获取二进制数据

​	使用`response.content`,  下载图片, 视频时最为常用.

### 添加headers

​	直接通过requests请求访问一些网站时, 默认是无法访问的, 会出现`400 Bad Request`错误. 这是因为这些网站需要头部信息, 我们需要将requests请求模仿成浏览器在访问, 即在头部信息中添加用户代理, 可以在谷歌浏览器中输入`Chrome://version`查看对应的用户代理, 并将用户代理添加到请求的头部信息中.

```python
headers = {
    'User-agent':
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

response = requests.get('http://www.zhihu.com', headers=headers)
print(response.text)
```

### POST请求

```python
# post请求
headers = {
    'User-agent':
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

data = {
    'name': 'lau',
    'age': 24
}
response = requests.post('http://httpbin.org/post', headers=headers, data=data)
print(response.text)        # form中会传入data
```

响应的更多属性

```python
# 响应的更多属性
response = requests.get('http://httpbin.org/get', headers=headers, )
print(type(response.status_code), response.status_code)     # int
print(type(response.headers), response.headers)             # requests.structures.CaseInsensitiveDict
print(type(response.cookies), response.cookies)             # requests.cookies.RequestsCookieJar
print(type(response.url), response.url)                     # str
print(type(response.history), response.history)             # list
```

### 文件上传

```python
files = {'files': open('./app.py', 'r')}
response = requests.post('http://httpbin.org/post', files=files)
print(response.text)        # files中会写入文件内容, "Content-Type": "multipart/form-data; 
```

### 获取cookie

```python
response = requests.get('http://www.baidu.com')
print(response.cookies)			# <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>

for k, v in response.cookies.items():
    print(k, v)					# BDORZ 27315 
```

### 会话维持

​	cookie的一个作用就是用于模拟登陆, 做会话维持

```python
# 会话维持
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456')
response = s.get('http://httpbin.org/cookies')
print(response.text)

# {
#   "cookies": {
#     "number": "123456"
#   }
# }
```

### 代理设置

```python
proxies = {
    'http': 'http://115.223.7.110:80',
}
response = requests.get('http://www.baidu.com', proxies=proxies)
print(response.content.decode('utf-8'))
```

### 超时设置
​	通过timeout参数设置超时时间




