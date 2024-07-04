from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Scientist',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 2,
    'title': 'Data Analyst',
    'location': 'Delhi, India',
    'salary': 'Rs. 12,00,000'
}, {
    'id': 3,
    'title': 'FrontEnd Developer',
    'location': 'Noida, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 4,
    'title': 'BackEnd Developer',
    'location': 'Gurugram, India',
    'salary': 'Rs. 14,00,000'
}]


@app.route("/")
def helloworld():
  return render_template('home.html', jobs=JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
