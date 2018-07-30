from flask import Flask
from .settings import configDict #配置字典
from .extensions import config_extension#第三方扩展库
from .views import  blueprint_register#注册蓝本
def create_app(configName):
    app=Flask(__name__)
    app.config.from_object(configDict[configName])
    config_extension(app)
    blueprint_register(app)
    return app