from flask_restful import reqparse, Resource
import werkzeug
import pandas as pd
from db_connection import get_connection
import uuid
import os

__all__ = ('uploadExcel')
class uploadExcel(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('file',
                    type=werkzeug.datastructures.FileStorage,
                    location='files',
                    required=True,
                    help='provide a file')
        args = parser.parse_args()
        try:
            file = args['file']
            file.save(file.filename)
            data = pd.read_excel(file.filename, engine='openpyxl')
            data = data.to_json()
            con = get_connection()
            cur = con.cursor()
            cur.execute("insert into exceltojson values (?, ?)", (str(uuid.uuid4()), str(data)))
            con.close()
            self.remove_file(file.filename)
            return {"Result": True, "Message":data}
        except BaseException as excep:
            self.remove_file(file.filename)
            return {"Result": False,"Message": str(excep)}
    

    def remove_file(self, file_name):
        if os.path.exists(file_name):
            os.remove(file_name)
            return True
        else:
            return False 