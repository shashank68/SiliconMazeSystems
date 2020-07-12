import jwt
import base64
import os
import hashlib
from flask import Flask, render_template, make_response, request, redirect
from flask_wtf.csrf import CSRFProtect
import cryptography


app = Flask(__name__)
app.secret_key = '\xbb\xf9\r\xffeK(\xfaN\xb3\xbc\xa4\xc03\x19B\xb8B\xa4\xc3S*NH'
FLAG = os.getenv("FLAG")
PASSWORD = os.getenv("PASSWORD")
with open("priv", "r") as f:
	PRIVATE_KEY = f.read()
with open("pub", "r") as f:
	PUBLIC_KEY = f.read()
csrf = CSRFProtect(app)
csrf.init_app(app)

@app.route('/', methods=['GET'])
def index():
	auth = request.cookies.get("auth")
	if auth is None:
		logged_in = False
		admin = False
	else:
		logged_in = True
		admin = jwt.decode(auth, PUBLIC_KEY)["auth"] == "admin"
		
	resp = make_response(render_template("index.html", logged_in=logged_in, admin=admin, flag=FLAG))
	return resp

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == "POST":
		resp = make_response(redirect("/"))
		if request.form["action"] == "Login":
			if request.form["username"] == "admin" and request.form["password"] == PASSWORD:
				auth = jwt.encode({"auth": "admin"}, PRIVATE_KEY, algorithm="RS256")
			else:
				auth = jwt.encode({"auth": "guest"}, PRIVATE_KEY, algorithm="RS256")
			resp.set_cookie("auth", auth)
		else:
			resp.delete_cookie("auth")
		return resp
	else:
		resp = make_response(render_template("login.html"))
		return resp

@app.route('/logout', methods=['GET'])
def logout():
	resp = make_response(redirect("/"))
	resp.delete_cookie("auth")
	return resp

@app.route("/key")
def public_key():
	with open("./pub", "r") as f:
		resp = make_response(f.read())
		resp.mimetype = 'text/plain'
		return resp

@app.route("/supersecret")
def secret():
	with open("./secret", "r") as f:
		resp = make_response(f.read())
		resp.mimetype = 'text/plain'
		return resp

@app.route("/robots.txt")
def bot():
	with open("./robots.txt", "r") as f:
		resp = make_response(f.read())
		resp.mimetype = 'text/plain'
		return resp


if __name__ == "__main__":
	app.run(host='0.0.0.0')
