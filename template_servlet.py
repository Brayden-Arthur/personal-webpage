from flask import Flask, render_template, g, request, send_file
app = Flask(__name__)

#default homepage, routed from home and the base url
@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template('index.html')

@app.route("/resume")
def resume():
    return render_template('resume.html')

@app.route("/Brayden_Arthur_Resume")
def resume_download():
    return send_file("Brayden_Arthur_Resume.pdf")

#runs servlet, debug=true if you want to test running code
if __name__ == "__main__":
    app.run(debug=True)
