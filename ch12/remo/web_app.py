#!/usr/bin/env python

from lirc import Lirc
from flask import Flask
from flask import render_template
from flask import request, jsonify

BASE_URL = ''

# Flask 객체 하나 생성
# css, js, img들을 담을 폴더를 지정한다.(web/static)
# jinja 템플릿으로 사용할 폴더 위치 (web/web-doc)
app = Flask(__name__
            , static_folder='web/static'
            , template_folder='web/web-doc')


# Initialise the Lirc config parser
with open('/etc/lirc/lircd.conf') as f:
    lirc = Lirc(f.read())

#------------------------------
# Pages
#------------------------------

@app.route("/")
def index():
    remos = lirc.get_remotes()
    return render_template('main.html', remos=remos)


@app.route("/remo/<remo_id>")
def controls(remo_id=None):
    buttons = sorted(lirc.get_buttons(remo_id))
    return render_template('control.html'
                           , remo_id = remo_id
                           , buttons = buttons )


#------------------------------
# AJAX
#------------------------------

@app.route("/remo/<remo_id>/<button_key>/execute", methods=["GET"])
def button_execute(remo_id, button_key):
    lirc.send_key(remo_id, button_key)
    ret = { 'code': 0, 'msg': 'ok' }
    return jsonify(**ret)


if __name__ == "__main__":
    app.run( host='0.0.0.0', port=5000, debug=True)


