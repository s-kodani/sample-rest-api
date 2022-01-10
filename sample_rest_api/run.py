import connexion
from flask_cors import CORS

DEBUG_MODE = True

def main():
    app = connexion.FlaskApp(
        __name__,
        host='0.0.0.0',
        port=10081,
        specification_dir='../apispec/',
        debug=DEBUG_MODE,
        options={
            'swagger_ui': True,
        },
    )
    app.add_api(
        'v1/openapi.yml',
        validate_responses=True,
    )
    if DEBUG_MODE:
        CORS(app.app, resources={r"/api/*": {"origins": "*"}})

    app.run()


if __name__ == '__main__':
    main()
