from flask import Flask, render_template

app = Flask(
	__name__,
	template_folder='templates',
	static_folder='assets'
)

from routes import predict, login, register, dashboard

app.secret_key = b"B\x80&o\7"

@app.route('/')
def base_page():
  
	return render_template(
		'base.html'
	)

if __name__ == "__main__":
	app.run(
		host='0.0.0.0',
		port=8080
	)
