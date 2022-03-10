from flask import Flask

app = Flask(__name__)


# 所谓的“注册”，就是给这个函数戴上一个装饰器帽子。
# 我们使用 app.route() 装饰器来为这个函数绑定对应的 URL，
# 当用户在浏览器访问这个 URL 的时候，就会触发这个函数，获取返回值，并把返回值显示到浏览器窗口：
@app.route('/hello_start')
def hello():
    # 注册一个处理函数，这个函数是处理某个请求的处理函数，
    # Flask 官方把它叫做视图函数（view funciton），你可以理解为“请求处理函数”。
    return 'Welcome to My Watchlist!'


@app.route('/helle_flask')
def hello_flask():
    return '<h1>Hello Flask!</h1><img src="http://helloflask.com/totoro.gif">'


# 一个视图函数也可以绑定多个 URL，这通过附加多个装饰器实现
# @app.route('/')
@app.route('/index')
@app.route('/home')
def hello_page():
    return 'Welcome to My Watchlist!'


#  用户输入的数据会包含恶意代码，所以不能直接作为响应返回，
#  需要使用 Flask 提供的 escape() 函数对 name 变量进行转义处理，
#  比如把 < 转换成 &lt;。这样在返回响应时浏览器就不会把它们当做代码执行。
from flask import escape


# 通过下面的方式，我们也可以在视图函数里获取到这个变量值：
@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % escape(name)


# 为了避免手写，Flask 提供了一个 url_for 函数来生成 URL，
# 它接受的第一个参数就是端点值，默认为视图函数的名称
from flask import url_for


@app.route('/test')
def test_url_for():
    # 下面是一些调用示例（请在命令行窗口查看输出的 URL）：
    print(url_for('hello'))  # 输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='greyli'))  # 输出：/user/greyli
    print(url_for('user_page', name='peter'))  # 输出：/user/peter
    print(url_for('test_url_for'))  # 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))  # 输出：/test?num=2
    return 'Test page'


# 使用 render_template() 函数可以把模板渲染出来，
# 必须传入的参数为模板文件名（相对于 templates 根目录的文件路径），这里即 'index.html'。
from flask import render_template

name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]


@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)
