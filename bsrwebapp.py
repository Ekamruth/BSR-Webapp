from flask import Flask,render_template

app=Flask(__name__, template_folder='htmlfiles')
@app.route("/")
def landing():
  return render_template('landing.html')

@app.route("/history")
def history():
  return render_template('history.html')

@app.route("/services")
def services():
  return render_template('services.html')

@app.route("/clients")
def clients():
  return render_template('clients.html')



if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)

