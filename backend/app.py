from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from upload_excel import uploadExcel




app = Flask(__name__)
CORS(app)
api = Api(app)



##
## Actually setup the Api resource routing here
##
@app.route('/')
def index():
    return "<h1>API Server is working...</h1>"


"""
    Routes
    ** '/api/register'
"""


api.add_resource(uploadExcel, '/api/upload')


# api.__init__(app)

if __name__ == '__main__':
    app.run()
