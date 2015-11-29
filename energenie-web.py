#!/usr/bin/env python3
# vim:set ts=4 sw=4 sts=4 noet

import energenie

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
app.config.update(dict( DEBUG=True ))

@app.route("/")
def index():
	action = None
	return render_template('buttons.html')

@app.route("/switch/<socket>/<action>", methods=['GET'])
def switch(socket, action):
	if action == 'on':
		energenie.switch_on(int(socket))
	elif action == 'off':
		energenie.switch_off(int(socket))
	return redirect(url_for('index'))

if __name__ == "__main__":
	app.run(host='0.0.0.0')
