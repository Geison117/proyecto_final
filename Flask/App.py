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
    return render_template('institucion/addInstitucion.html')

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
    return render_template('institucion/institucion.html',instituciones = ins)

@app.route('/edit_ins/<id>')
def editins(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM institucion WHERE id_institucion = %s',(id))
    ins = cur.fetchall()
    return render_template('institucion/editinstitucion.html', institucion = ins[0])

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
    DELETE FROM estudiante_curso WHERE
	id_curso IN (SELECT id_curso FROM curso
    WHERE id_institucion = %s)''',(id))
    				
    cur.execute('''
    DELETE FROM estudiante_especializacion WHERE
	id_especializacion IN (SELECT id_especializacion FROM especializacion
    WHERE id_institucion = %s)''',(id))

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
    cur.execute('SELECT i.nombre,c.* FROM curso c join institucion i on i.id_institucion=c.id_institucion')
    data = cur.fetchall()
    return render_template('cursos/cursos.html',cursos = data)
    
@app.route('/add_curso')
def add_cur():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM institucion')
    ins = cur.fetchall()
    cur.execute('SELECT * FROM plan')
    pl = cur.fetchall()
    cur.execute('SELECT * FROM categoria')
    cat = cur.fetchall()
    return render_template('cursos/addCurso.html',instituciones = ins, planes = pl, categorias = cat )

@app.route('/add_cur', methods=['POST'])
def addedcur():
    if request.method == 'POST':
        institucion= request.form['ins']
        nombre= request.form['nom']
        clasest= request.form['ct']
        clasesp= request.form['cp']
        calificacion= request.form['cal']
        plan = request.form['plan']
        cat1 = request.form['cat1']
        cat2 = request.form['cat2']
        cat3 = request.form['cat3']
        cur = mysql.connection.cursor()
        cur.execute(''' 
        INSERT INTO curso (id_institucion,nombre,clases_teoricas,clases_practicas,calificacion) VALUES (%s, %s, %s,%s,%s)
        ''', (institucion,nombre,clasest,clasesp,calificacion))
        mysql.connection.commit()
        cur.execute('SELECT MAX(id_curso) FROM curso')
        id = cur.fetchall()
        print(id[0])
        print(plan)
        print(cat1)
        print(cat2)
        print(cat3)
        if int(plan) == 2:
            cur.execute('INSERT INTO plan_curso VALUES (%s,%s),(%s,%s)',(1,id[0],2,id[0]))
        else:
            cur.execute('INSERT INTO plan_curso VALUES (%s,%s)',(1,id[0]))
        mysql.connection.commit()
        if int(cat2) > 0 and int(cat3) > 0:
            if int(cat1) != int(cat2) and int(cat1) != int(cat2):
                cur.execute('INSERT INTO curso_categoria(id_curso,id_categoria) VALUES (%s,%s),(%s,%s),(%s,%s)',(id[0],cat1,id[0],cat2,id[0],cat3)) 
        else:
            if int(cat2) > 0:
                if cat1 != cat2: 
                    cur.execute('INSERT INTO curso_categoria (id_curso,id_categoria) VALUES (%s,%s),(%s,%s)',(id[0],cat1,id[0],cat2)) 
            else:
                if int(cat3) > 0:
                    if cat1 != cat3:
                        cur.execute('INSERT INTO curso_categoria (id_curso,id_categoria) VALUES (%s,%s),(%s,%s)',(id[0],cat1,id[0],cat3))
                else:
                    cur.execute('INSERT INTO curso_categoria (id_curso,id_categoria) VALUES (%s,%s)',(id[0],cat1))
        mysql.connection.commit()
        return redirect(url_for('cursos/curhtml'))

#RUTAS PARA ESTUDIANTE


@app.route('/estudiante')
def esthtml():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM estudiante')
    data = cur.fetchall()
    cur.execute('SELECT nombre FROM plan')
    nombrePlan=cur.fetchall()
    return render_template('estudiante/estudiante.html',estudiantes = data, plan = nombrePlan)

@app.route('/add_estudiante')
def add_est():
    return render_template('estudiante/addEstudiante.html')

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

@app.route('/elim_est/<id>')
def elimest(id):
    cur = mysql.connection.cursor()
    cur.execute(
    '''DELETE FROM estudiante_curso 
     WHERE id_estudiante=%s''',(id))


    cur.execute('''DELETE FROM estudiante_especializacion 
    WHERE id_estudiante=%s''',(id))

    cur.execute('''DELETE FROM estudiante 
     WHERE id_estudiante=%s''',(id))
    
    mysql.connection.commit()

    return redirect(url_for('esthtml'))

@app.route('/update_estudiante/<id>')
def upest(id):
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM estudiante
    WHERE id_estudiante =%s''',(id))
    datosEstudiante = cur.fetchall()
    
    return render_template('estudiante/editEstudiante.html', estudiante = datosEstudiante)

@app.route('/update_estud/<id>', methods=['POST'])
def updatees(id):
    if request.method == 'POST':
        nombre= request.form['nom']
        apellido= request.form['ape']
        usuario= request.form['usu']
        fecha_nac= request.form['fec']
        nacionalidad= request.form['nac']
        plan= request.form['pla']
        cur = mysql.connection.cursor()
        cur.execute(''' 
        UPDATE estudiante SET nombre=%s,apellido=%s,usuario=%s,fecha_nacimiento=%s,nacionalidad=%s,id_plan=%s
        WHERE id_estudiante = %s''', (nombre,apellido,usuario,fecha_nac,nacionalidad,plan,id))
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
    cur.execute('''SELECT id_estudiante FROM estudiante WHERE id_estudiante=%s''',(id))
    estudiante = cur.fetchall()
    return render_template('estudiante/ver_cursos.html', cursos = cursosEstudiante, estudiante=estudiante)


@app.route('/ver_especializaciones/<id>')
def ver_especializaciones(id):
    cur = mysql.connection.cursor()
    cur.execute('	SELECT es.* FROM estudiante_especializacion ee, especializacion es, estudiante e'\
	' WHERE ee.id_estudiante=e.id_estudiante'\
	' AND ee.id_especializacion=es.id_especializacion'\
	' AND e.id_estudiante =%s;',(id))
    especializacionEstudiante = cur.fetchall()
    cur.execute('''SELECT id_estudiante FROM estudiante WHERE id_estudiante=%s''',(id))
    estudiante = cur.fetchall()
    return render_template('/estudiante/ver_especializaciones.html', especializaciones = especializacionEstudiante, estudiante=estudiante)

@app.route('/inscribir_curso/<id>')
def inscur(id):
    cur = mysql.connection.cursor()
    cur.execute('''SELECT id_plan FROM estudiante WHERE 
    id_estudiante = %s''',(id))
    idplan = cur.fetchall()
    idplan =idplan[0][0]
    idplan = str(idplan)
    
    cur.execute('SELECT id_estudiante FROM estudiante WHERE id_estudiante = %s',(id))
    estudiante = cur.fetchall()
    cur.execute('''SELECT c.* FROM plan_curso pc,curso c
	WHERE pc.id_curso=c.id_curso
	AND pc.id_plan = %s
	AND c.id_curso NOT IN 
	(SELECT id_curso FROM estudiante_curso
	WHERE id_estudiante = %s)''',(idplan,id))
    cursos = cur.fetchall()
    return render_template('estudiante/inscripcionCurso.html', cursos = cursos, estudiante=estudiante)

@app.route('/ins_cur/<ide>/<idc>')
def ins_cur(ide,idc):
    cur = mysql.connection.cursor()
    cur.execute('''INSERT INTO estudiante_curso (id_estudiante,id_curso,fec_fin,fec_inicio,Aprobado)
     VALUES (%s,%s,'2030-08-25',DATE(NOW()),0)  ''',(ide,idc))
    mysql.connection.commit()
    
    return redirect(url_for('ver_cursos',id=ide))


@app.route('/inscribir_especializacion/<id>')
def insesp(id):
    cur = mysql.connection.cursor()
    cur.execute('''SELECT id_plan FROM estudiante WHERE 
    id_estudiante = %s''',(id))
    idplan = cur.fetchall()
    idplan =idplan[0][0]
    idplan = str(idplan)
    
    cur.execute('SELECT id_estudiante FROM estudiante WHERE id_estudiante = %s',(id))
    estudiante = cur.fetchall()
    cur.execute('''	SELECT es.* FROM plan_especializacion pc,especializacion es
	WHERE pc.id_especializacion=es.id_especializacion
	AND pc.id_plan = %s
	AND es.id_especializacion NOT IN 
	(SELECT id_especializacion FROM estudiante_especializacion
	WHERE id_estudiante = %s)''',(idplan,id))
    especializaciones = cur.fetchall()
    return render_template('/estudiante/inscripcionEspecializacion.html', especializaciones = especializaciones, estudiante=estudiante)

@app.route('/ins_esp/<ide>/<ides>')
def ins_esp(ide,ides):
    cur = mysql.connection.cursor()
    cur.execute('''INSERT INTO estudiante_especializacion (id_estudiante,id_especializacion,estado)
     VALUES (%s,%s,'En curso')  ''',(ide,ides))
    mysql.connection.commit()
    
    return redirect(url_for('ver_especializaciones',id=ide))


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
    app.run(port=4200, debug=True)