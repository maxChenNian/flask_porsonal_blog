# flask_porsonal_blog
🍉 Learn flask and build a personal blog site.



## Flask 入门教程

### a001_000_example_flask_tutorial

- [第 1 章：准备工作](https://read.helloflask.com/c1-ready)
- [第 2 章：Hello，Flask！](https://read.helloflask.com/c2-hello)
- [第 3 章：模板](https://read.helloflask.com/c3-hello)

### a001_001_example_flask_tutorial

- [第 4 章：静态文件](https://read.helloflask.com/c4-static)
- [第 5 章：数据库](https://read.helloflask.com/c5-database)

### a001_002_example_flask_tutorial

- [第 6 章：模板优化](https://read.helloflask.com/c6-template2)
- [第 7 章：表单](https://read.helloflask.com/c7-form)
- [第 8 章：用户认证](https://read.helloflask.com/c8-login)


### a001_003_example_flask_tutorial

- [第 9 章：测试](https://read.helloflask.com/c9-test)

### a001_004_example_flask_tutorial

- [第 10 章：组织你的代码](https://read.helloflask.com/c10-organize)  
- [第 11 章：部署上线](https://read.helloflask.com/c11-deploy)
```shell
cd 001_004_example_flask_tutorial
flask initdb --drop 
flask admin
flask run
python test_watchlist.py
coverage run --source=watchlist test_watchlist.py
coverage report
coverage html
```

使用 [PythonAnywhere](https://www.pythonanywhere.com) 部署程序



## Flask Web开发实战
### a002_000_example_flask_development

第一章

在一个Web应用里，客户端和服务器上的Flask程序的交互可以简单
概括为以下几步： 

- 1）用户在浏览器输入URL访问某个资源。
- 2）Flask接收用户请求并分析请求的URL。
- 3）为这个URL找到对应的处理函数。 

- 4）执行函数并生成响应，返回给浏览器。

- 5）浏览器接收并解析响应，将信息显示在页面中。
