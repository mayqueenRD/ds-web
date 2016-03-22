#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import sys
import subprocess

reload(sys) # Reload does the trick!
sys.setdefaultencoding('UTF8')

app = Flask(__name__)

@app.route("/")
def main():
    proc = subprocess.Popen(["cat ./marquee.txt ", ""], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    marquee=out

    proc = subprocess.Popen(["cat ./marquee-speed.txt ", ""], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    marquee_speed=out


    templateData = {
        'marquee': marquee
        'marquee_speed': marquee_speed
    }

    return render_template('index2.html', **templateData)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
