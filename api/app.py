from flask import Flask, jsonify
from controller.user import user_blueprint
from controller.reservation import reservation_blueprint
from controller.apartment import apartment_blueprint

import exception.controller as ExCon

app = Flask(__name__)

app.register_blueprint(user_blueprint, url_prefix="/api/user")
app.register_blueprint(reservation_blueprint, url_prefix="/api/reservation")
app.register_blueprint(apartment_blueprint, url_prefix="/api/apartment")


@app.errorhandler(ExCon.ControllerException)
def handle_custom_exceptions(error):
    error_dict = error.to_dict()
    response = jsonify(error_dict)
    response.status_code = error.to_code()  # Internal Server Error
    return response


if __name__ == "__main__":
    app.run(debug=True)
