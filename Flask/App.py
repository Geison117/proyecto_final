from flask import Flask, render_template, request,redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#Mysql Connection
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='usuario'
app.config['MYSQL_PASSWORD']='1234'
app.config['MYSQL_DB']='proyecto'
mysql = MySQL(app)

#settings
app.secret_key='mysecretkey'

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/add_institucion')
def add_insti():
    return render_template('addInstitucion.html')

@app.route('/add_insti', methods=['POST'])
def added():
    if request.method == 'POST':
        nom = request.form['nom']
        pais = request.form['pais']
        tipo = request.form['tipo']
        cal = request.form['cal']
        cur = mysql.connection.cursor()
        cur.execute(''' 
        INSERT INTO institucion (nombre,pais,tipo,calificacion) VALUES (%s, %s, %s,%s)
        ''', (nom,pais,tipo,cal))
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur=mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', (fullname,phone,email))
        mysql.connection.commit()
        flash('Contacto agregado con exito')


        return redirect(url_for('Index'))


@app.route('/edit/<id>')
def get_contact(id):
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id=%s',(id))
    data = cur.fetchall()
    return render_template('edit-contact.html', contact=data[0])

@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur=mysql.connection.cursor()
        cur.execute("""
            UPDATE contacts 
            SET fullname = %s,
                email = %s,
                phone = %s
            WHERE id = %s    
        """, (fullname,email,phone,id))
        mysql.connection.commit()
        flash('Contacto actualizado')
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur=mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contacto removido')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port=3000, debug=True)