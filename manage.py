import os
from app import create_app,db
from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand
from app.models import User

app = create_app(os.getenv('FLASK_CONFIG')or 'default')
manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app = app,User=User)

if __name__ == '__main__':
    manager.run()