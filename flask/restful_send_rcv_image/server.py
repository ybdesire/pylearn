import base64
import os
from flask import Flask, request, Response
import jsonpickle
# refered from 
# https://blog.csdn.net/t8116189520/article/details/90904452
# https://gist.github.com/kylehounslow/767fb72fde2ebdd010a0bf4242371594

app=Flask(__name__)
 

@app.route("/api/img", methods=['POST'])
def get_frame():
    upload_file = request.files['file']
    file_name_orig = upload_file.filename
    file_name_dst = 'rcv_'+file_name_orig
    file_path=r'.'
    if upload_file:
        file_paths = os.path.join(file_path, file_name_dst)
        upload_file.save(file_paths)
    response = { 'message': 'received' }
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")



# start flask app
app.run(host="0.0.0.0", port=5000, threaded=True)
