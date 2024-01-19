import os
from app.views import app

if __name__ == '__main__':
    app.run(os.getenv('APP_ADDRESS','localhost'), port=8888, debug=True)