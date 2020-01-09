from flask import Flask, redirect, url_for, request, render_template

from .auth import requires_auth
from .zxllogging import logger

app = Flask(__name__)

#logging.basicConfig(filename='', level=logging.DEBUG, filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# https://www.jianshu.com/p/8752d9000cff 参考认证信息
@app.route('/api')
@requires_auth
def api_hello():
    logger.info('登录成功！')
    logger.warning('登录警告!')
    logger.error('登录失败!')

    return '嘘，这是绝密间谍的东西'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/admin')
def hello_admin():
    return 'Hello Admin'


@app.route('/login/<name>')
def login1(name):
    return 'Hello %s' % name


@app.route('/guest/')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest


@app.route('/user/')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)
