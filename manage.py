from flask_script import Manager
from App import create_app #导入app
from flask_migrate import MigrateCommand
app = create_app('default') #加载配置
manager = Manager(app)
manager.add_command('db',MigrateCommand) #将迁移的命令添加到终端运行解析器 通过命令进行迁移
if __name__ == '__main__':
    manager.run()
