## 全站爬取1

### 基于管道的持久化存储

- 数据解析（爬虫类）

- 将解析的数据封装到item类型的对象中（爬虫类）

- 将item提交给管道， yield item（爬虫类）

- 在管道类的process_item中接手收item对象， 并进行任意形式的持久化存储操作（管道类）

- 在配置文件中开启管道

- 细节：

  - 将爬取到的数据进行备份：一个管道类对应一种平台的持久化存储

  - 有多个管道类是否意味着多个管道类都可以接收到爬虫文件提交的item？

    只有优先级最高的管道才会接收到item，其余的管道是从优先级最高的管道类中接收item
  

### 基于Spider父类进行全站数据的爬取

- 全站数据的爬取：将所有页码对应的页面数据进行爬取
- 手动发送请求 (get): `yield scrapy.Request(url, callback)`
- 对yield的总结:
  - 向管道提交item时, `yield item`
  - 手动发送请求: `yield scrapy.Request(url, callback)`
- 手动发送请求 (post): `yield scrapy.Request(url, formdata, callback)`

### scrapy请求传参

- 作用: 实现深度爬取

- 使用场景: 使用scrapy爬取的数据没有存在于同一个页面中, 
- 传递item: `yield Request(url, callback, meta={'item':item})`
- 接收item: `response.meta['item']`

### 提升scrapy爬取数据的效率

  在配置文件中进行相关配置即可.

- 增加并发: 默认scrapy开启的并发线程为32个, 可以适当进行增加. 在settings配置文件中修改CONCURRENT_REQUESTS=100
- 降低日志级别: 在运行scrapy时, 会有大量日志信息的输出, 为了减少CPU的使用率, 可以设置log输出信息为INFO或ERROR即可, 在配置文件中写入 LOG_LEVEL='INFO'
- 禁止cookie: 如果不是真的需要cookie, 则在scrapy爬取数据时可以禁止cookie, 从而减少CPU的使用率, 提升爬取效率. 在配置文件中设置COOKIES_ENABLED=False
- 禁止重试: 对失败的HTTP进行重新请求会减慢爬取速度, 因此可以禁止重试. 在配置文件中设置RETRY_ENABLED=False
- 减少下载超时: 如果对一个非常慢的链接进行爬取, 减少下载超时可以能让卡住的链接被快速放弃, 提升效率. 在配置文件中设置DOWNLOAD_TIMEOUT=10, 设置超时时间为10秒.

### scrapy的中间件

- 爬虫中间件
- 下载中间件(重点): 处于引擎和下载器之间
  - 作用: 批量拦截所有的请求和响应
  - 拦截请求, 可以篡改请求的头信息, 进行UA伪装; 或者篡改请求对应的IP代理
  - 拦截响应, 可以篡改响应数据, 或者篡改响应对象

- selenium在scrapy中的使用流程
  - 在爬虫类中定义一个browser属性, 其实就是实例化的浏览器对象
  - 在爬虫类重写父类的closed(self, spider)方法, 并在该方法中关闭browser
  - 在中间件中进行浏览器自动化操作

### 图片懒加载

- 应用到标签的伪属性, 数据捕获的时候要基于伪属性进行.
- 专门用于二进制数据下载和持久化存储的管道类: ImagePipeline

## 全站爬取2

### CrawlSpider

- 一种基于scrapy进行全站数据爬取的一种新的技术手段
- CrawlSpider是Spider的一个子类
  - 连接提取器: LinkExtractor
  - 规则解析器: Rule
- 使用流程:
  - 新建工程
  - cd 工程中, 新建一个爬虫文件 `scrapy genspider -t crawl spider_name www.xxx.com`





































































































