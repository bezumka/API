from flask import Flask
from api.get_info import bp_info
from api.put_data import bp_put


app = Flask(__name__)
app.register_blueprint(bp_info)
app.register_blueprint(bp_put)


if __name__ == '__main__':
    app.run(debug=True)