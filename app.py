from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title': 'Python Developer',
    'location': 'New York',
    'salary': '$100,000'
  },
  {
    'id':2,
    'title': 'Cool Dude',
    'location': 'New York',
    'salary': '$100,000,000'
  },
{
  'id':3,
  'title': 'Music Developer',
  'location': 'Remote',  
}
]

@app.route("/")
def hello_world():
  return render_template('home.html', 
                         jobs=JOBS,
                        company_name='Tactical Treehouse')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)