## logging模块的使用

### 简单配置

```python
import logging

# 简单配置
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='test.log')

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
```

### 对象配置

```python
"""
对象配置
    可以解决中文乱码问题
    同时在文件和屏幕输出日志
    
步骤：
    创建一个log对象
    创建一个控制文件输出的文件操作符
    创建一个控制屏幕输出的屏幕操作符
    创建格式
    
    文件操作符绑定格式
    屏幕操作符绑定格式
    log对象绑定文件操作符和屏幕操作符
"""

# 创建一个log对象
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 创建一个控制文件输出的文件操作符
fh = logging.FileHandler('mylog.log', encoding='gbk')

# 创建一个控制屏幕输出的屏幕操作符
sh = logging.StreamHandler()

# 创建格式
fmt = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s')
fmt2 = logging.Formatter('%(asctime)s %(name)s[line:%(lineno)d] %(levelname)s: %(message)s')

# 文件操作符绑定格式
fh.setFormatter(fmt)

# 屏幕操作符绑定格式
sh.setFormatter(fmt2)
sh.setLevel(level=logging.WARNING)

# log对象绑定文件操作符和屏幕操作符
logger.addHandler(fh)
logger.addHandler(sh)


logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')
```

