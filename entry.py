from bakery import create_app

app = create_app(app_name='bakery')
app.config['DEBUG'] = True
app.config.from_object('config')
app.config.from_pyfile('local.cfg', silent=True)

import logging
LOG_FILENAME = 'data/run.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)

logging.info('Project start')

if __name__ == '__main__':
    app.run(port=5000)
