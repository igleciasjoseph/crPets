from flask import Flask, request, redirect, render_template
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route('/')
def index():
    mysql = connectToMySQL('crPets')
    pets = mysql.query_db('SELECT * FROM pets;')
    print(pets)
    return render_template('index.html', all_pets = pets)

@app.route('/add', methods = ['POST'])
def add():
    mysql = connectToMySQL('crPets')
    query = "INSERT INTO pets(name, type, created_at, updated_at) VALUES (%(n)s, %(t)s, NOW(), NOW())"
    data = {
        "n": request.form['fnameadd'],
        "t": request.form['typeadd']
    }
    new_pet_id = mysql.query_db(query, data)
    return redirect('/')

@app.route('/delete')
def delete():
    mysql = connectToMySQL('crPets')
    query = "DELETE FROM pets;"
    mysql.query_db(query)
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)
