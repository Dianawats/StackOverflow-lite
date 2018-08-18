import os
from api import app

from config import app_config

config_name = os.getenv('APP_SETTINGS')  # config_name = "development"

if __name__ == '__main__':
    """creates application that runs"""

    app.config.from_object(app_config.get(config_name))
    app.run()


