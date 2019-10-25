#!/usr/bin/env python

from flask_script import Manager

from project_name import create_app


APP_NAME = 'project_name'

app = create_app(APP_NAME)
manager = Manager(app)
# setproctitle(APP_NAME)


@manager.option('-h', '--host', dest='host', default='0.0.0.0')
@manager.option('-p', '--port', dest='port')
def runserver(host='0.0.0.0', port=None):
    """Запуск легковесного web-сервера для раработки на локальной машине."""
    default_port = app.config['PORT']
    if host == 'localhost':
        host = '127.0.0.1'
    port = port if port else default_port
    app.run(debug=True, host=host, port=int(port))


if __name__ == '__main__':
    manager.run()
