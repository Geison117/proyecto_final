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


#RUTAS PARA INSTITUCION
@app.route('/add_institucion')
def add_insti():
    return render_template('addInstitucion.html')

@app.route('/add_insti', methods=['POST'])
def addedins():
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
        return redirect(url_for('insti'))

@app.route('/institucion')
def insti():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM institucion')
    ins = cur.fetchall()
    return render_template('institucion.html',instituciones = ins)

@app.route('/edit_ins/<id>')
def editins(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM institucion WHERE id_institucion = %s',(id))
    ins = cur.fetchall()
    return render_template('editinstitucion.html', institucion = ins[0])

@app.route('/update_ins/<id>', methods = ['POST'])
def updateins(id):
    if request.method == 'POST':
        nom = request.form['nom']
        pais = request.form['pais']
        tipo = request.form['tipo']
        cal = request.form['cal']
        cur = mysql.connection.cursor()
        cur.execute('''
        UPDATE institucion
        SET nombre = %s, pais = %s, tipo = %s, calificacion = %s
        WHERE id_institucion = %s
        ''',((nom,pais,tipo,cal,id)))
        mysql.connection.commit()
    return redirect(url_for('insti'))

@app.route('/elim_ins/<id>')
def elimins(id):
    cur = mysql.connection.cursor()
    cur.execute('''
    DELETE FROM curso
    WHERE id_institucion = %s''',(id))
    cur.execute('''
    DELETE FROM especializacion
    WHERE id_institucion = %s''',(id))
    cur.execute('''
    DELETE FROM institucion
    WHERE id_institucion = %s''',(id))
    mysql.connection.commit()
    return redirect(url_for('insti'))
    
 #RUTAS PARA CURSOS

@app.route('/cursos')
def curhtml():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM curso')
    data = cur.fetchall()
    return render_template('cursos.html',cursos = data)
    
@app.route('/add_curso')
def add_cur():
    return render_template('addCurso.html')

@app.route('/add_cur', methods=['POST'])
def addedcur():
    if request.method == 'POST':
        institucion= request.form['ins']
        nombre= request.form['nom']
        clasest= request.form['ct']
        clasesp= request.form['cp']
        calificacion= request.form['cal']
        cur = mysql.connection.cursor()
        cur.execute(''' 
        INSERT INTO curso (id_institucion,nombre,clases_teoricas,clases_practicas,calificacion) VALUES (%s, %s, %s,%s,%s)
        ''', (institucion,nombre,clasest,clasesp,calificacion))
        mysql.connection.commit()
        return redirect(url_for('curhtml'))

#RUTAS PARA ESTUDIANTE


@app.route('/estudiante')
def esthtml():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM estudiante')
    data = cur.fetchall()
    cur.execute('SELECT nombre FROM plan')
    nombrePlan=cur.fetchall()
    return render_template('estudiante.html',estudiantes = data, plan = nombrePlan)

@app.route('/add_estudiante')
def add_est():
    return render_template('addEstudiante.html')

@app.route('/add_estud', methods=['POST'])
def addedes():
    if request.method == 'POST':
        nombre= request.form['nom']
        apellido= request.form['ape']
        usuario= request.form['usu']
        fecha_nac= request.form['fec']
        nacionalidad= request.form['nac']
        plan= request.form['pla']
        cur = mysql.connection.cursor()
        cur.execute(''' 
        INSERT INTO estudiante (nombre,apellido,usuario,fecha_nacimiento,nacionalidad,id_plan) VALUES (%s, %s, %s,%s,%s,%s)
        ''', (nombre,apellido,usuario,fecha_nac,nacionalidad,plan))
        mysql.connection.commit()
        return redirect(url_for('esthtml'))



@app.route('/ver_cursos/<id>')
def ver_cursos(id):
    cur = mysql.connection.cursor()
    cur.execute('	SELECT c.* FROM estudiante_curso ec, curso c, estudiante e'\
	' WHERE ec.id_estudiante=e.id_estudiante'\
	' AND ec.id_curso=c.id_curso'\
	' AND e.id_estudiante =%s;',(id))
    cursosEstudiante = cur.fetchall()
    return render_template('ver_cursos.html', cursos = cursosEstudiante)

#RUTAS PARA ESPECIALIZACION

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
    app.run(port=3800, debug=True)