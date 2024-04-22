from flask import Flask,request,jsonify
import json
from flask_cors import CORS
# ...
FeedBack = []
app = Flask(__name__)
cors = CORS(app,origins="*")
i = 0
@app.route('/api/feedback', methods=['POST',"GET"])
def back():
    if request.method == "POST":
        data = json.loads(request.get_data())["feed"]
        if len(data) >= 3:
            FeedBack.append(data)
        return FeedBack
    else:
        return FeedBack




if __name__ == "__main__":
    app.run(debug=True,port=8080)