import mysql
from flask import Flask, render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/billingsystem'
db = SQLAlchemy(app)


class Customer(db.Model):
    invoice_no = db.Column(db.Integer, primary_key=True)
    ssn = db.Column(db.Integer, nullable=false)
    custname = db.Column(db.String(80), nullable=false)
    contactnum = db.Column(db.String(12), nullable=false)


class Items(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(80), nullable=false)
    quantity = db.Column(db.Integer, nullable=false)
    price = db.Column(db.Integer, nullable=false)


class Inventform(db.Model):
    productId = db.Column(db.Integer, primary_key=True)
    productname = db.Column(db.String(80), nullable=false)
    quantity = db.Column(db.Integer, nullable=false)
    price = db.Column(db.Integer, nullable=false)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    if request.method == 'POST':
        '''add entry to database'''
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        age = request.form.get('age')
        entry = Items(item_id=fname, item_name=lname, quantity=email, price=age)
        db.session.add(entry)
        db.session.commit()
    return render_template('inventory.html')


@app.route('/customer', methods=['GET', 'POST'])
def customer():
    if request.method == 'POST':
        '''Add entry to database'''
        no = request.form.get('no')
        SSN = request.form.get('SSN')
        custname = request.form.get('custname')
        contactnum = request.form.get('contactnum')
        entry = Customer(ssn=SSN, custname=custname, contactnum=contactnum, invoice_no=no)
        db.session.add(entry)
        db.session.commit()
    return render_template('customer.html')


@app.route('/bill2')
def bill2():
    return render_template('bill2.html')


# @app.route('/try_invent')
# def try_invent():
#     form = Inventform()
#     return render_template('try_invent.html', form=form)




# @app.route('/new_give', methods=['GET', 'POST'])
# def new_give():
#     return render_template('new_give.html')


# @app.route('/')
# def Index():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT  * FROM students")
#     data = cur.fetchall()
#     cur.close()
#
#     return render_template('new_give.html', students=data)


# @app.route('/insert', methods=['POST'])
# def insert():
#
#     if request.method == "POST":
#         flash("Data Inserted Successfully")
#         name = request.form['name']
#         email = request.form['email']
#         phone = request.form['phone']
#         entry = Customer(name=name, email=email, phone=phone)
#         db.session.add(entry)
#         db.session.commit()
#         return redirect(url_for('new_give'))
#
#
# @app.route('/delete/<string:id_data>', methods=['GET'])
# def delete(id_data):
#     flash("Record Has Been Deleted Successfully")
#     cur = mysql.connection.cursor()
#     cur.execute("DELETE FROM students WHERE id=%s", (id_data,))
#     mysql.connection.commit()
#     return redirect(url_for('new_give'))
#
#
# @app.route('/update', methods=['POST', 'GET'])
# def update():
#
#     if request.method == 'POST':
#         id_data = request.form['id']
#         name = request.form['name']
#         email = request.form['email']
#         phone = request.form['phone']
#         cur = mysql.connection.cursor()
#         cur.execute("""
#                UPDATE students
#                SET name=%s, email=%s, phone=%s
#                WHERE id=%s
#             """, (name, email, phone, id_data))
#         flash("Data Updated Successfully")
#         mysql.connection.commit()
#         return redirect(url_for('new_give'))
#


if __name__ == "__main__":
    app.run(debug=True)
