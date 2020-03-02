from apiapp import app
from apiapp.views import user_api,source_api

app.register_blueprint(user_api.blue,url_prefix='/api/')
app.register_blueprint(source_api.blue,url_prefix='/api/')
if __name__ == '__main__':
    #注册蓝图

    app.run(host='0.0.0.0', port=5000)