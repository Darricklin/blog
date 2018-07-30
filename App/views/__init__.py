from .test import test
from .main import main
from .uesr_register import user
from .owncenter import center
from .posts import posts
blueprint_config=[(main,''),
                  (test,''),
                  (user,''),
                  (center,''),
                  (posts,'')]
def blueprint_register(app):
    for blue,prefix in blueprint_config:
        app.register_blueprint(blue,url_prefix=prefix)