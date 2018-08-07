#!/usr/bin/env python
# __coding:utf-8__
from flask import  Flask  , make_response  ,jsonify,redirect


app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}),404)

@app.route('/api/v1.0/wangfeitest')
def wangfeitest():
    return 'The test is succuss!!!'



if __name__ == '__main__':
    app.run(host='0.0.0.0')

