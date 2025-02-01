from flask import Flask
from app.imei.routes import main as routes


def main():
    app = Flask(__name__)
    app.register_blueprint(routes)
    return app


if __name__ == '__main__':
    app = main()
    app.run(host='0.0.0.0', port=8000, debug=False)
