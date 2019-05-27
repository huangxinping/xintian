from xintian.server import app
from views import *

app.blueprint(v1_bp)


@app.listener('before_server_start')
async def before_srver_start(app, loop):
    pass


@app.listener('before_server_stop')
async def before_server_stop(app, loop):
    pass


if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=True)
