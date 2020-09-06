CREATE DATABASE proyecto ;

USE proyecto;

CREATE TABLE plan(

id_plan INT AUTO_INCREMENT,
nombre VARCHAR(30),
precio FLOAT,
PRIMARY KEY(id_plan)
);


CREATE TABLE categoria
(	
	id_categoria int AUTO_INCREMENT,
	nombre VARCHAR(50),
	PRIMARY KEY(id_categoria)		
);

CREATE TABLE institucion
(	
	id_institucion int AUTO_INCREMENT,
	nombre VARCHAR(50),
	pais VARCHAR(50),
	tipo VARCHAR(50),
	calificacion FLOAT,
	PRIMARY KEY(id_institucion)		
);

CREATE TABLE estudiante(

id_estudiante INT AUTO_INCREMENT,
nombre VARCHAR(30),
apellido VARCHAR(30),
usuario VARCHAR(30),
fecha_nacimiento DATE,
nacionalidad VARCHAR(20),
id_plan INT,
PRIMARY KEY(id_estudiante),
FOREIGN KEY(id_plan) REFERENCES plan(id_plan)


);


CREATE TABLE curso(

id_curso INT AUTO_INCREMENT,
id_institucion INT,
nombre VARCHAR(100),
clases_teoricas INT,
clases_practicas INT,
calificacion FLOAT,
PRIMARY KEY(id_curso),
FOREIGN KEY(id_institucion) REFERENCES institucion(id_institucion)
);



CREATE table especializacion(
id_especializacion INT AUTO_INCREMENT,
nombre VARCHAR(100),
calificacion FLOAT,
nivel VARCHAR(20),
id_institucion INT,
PRIMARY KEY(id_especializacion),
FOREIGN KEY(id_institucion) REFERENCES institucion(id_institucion)
);


CREATE TABLE plan_especializacion
(	
	
	id_plan INT,
	id_especializacion INT,
	PRIMARY KEY(id_plan,id_especializacion ),
	FOREIGN KEY(id_especializacion) REFERENCES especializacion(id_especializacion),
	FOREIGN KEY(id_plan) REFERENCES plan(id_plan)		
);


CREATE TABLE curso_categoria
(	

	id_curso INT,
	id_categoria INT,
	PRIMARY KEY(id_categoria, id_curso),
	FOREIGN KEY(id_categoria) REFERENCES categoria(id_categoria),
	FOREIGN KEY(id_curso) REFERENCES curso(id_curso)		
);







CREATE TABLE estudiante_especializacion(
id_estudiante INT NOT NULL,
id_especializacion INT NOT NULL,
PRIMARY KEY(id_estudiante,id_especializacion),
FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante),
FOREIGN KEY (id_especializacion) REFERENCES especializacion(id_especializacion)
);

CREATE TABLE estudiante_curso(
id_estudiante INT NOT NULL,
id_curso INT NOT NULL,
PRIMARY KEY (id_estudiante,id_curso),
FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante),
FOREIGN KEY (id_curso) REFERENCES curso(id_curso)
);

CREATE TABLE especializacion_curso(
id_especializacion INT NOT NULL,
id_curso INT NOT NULL,
PRIMARY KEY(id_especializacion,id_curso),
FOREIGN KEY (id_especializacion) REFERENCES especializacion(id_especializacion),
FOREIGN KEY (id_curso) REFERENCES curso(id_curso)
);


CREATE TABLE plan_curso(
id_plan INT NOT NULL,
id_curso INT NOT NULL,
PRIMARY KEY(id_plan,id_curso),
FOREIGN KEY (id_plan) REFERENCES plan(id_plan),
FOREIGN KEY (id_curso) REFERENCES curso(id_curso)
);

INSERT INTO plan (nombre,precio) VALUES('Gratis',0),('Premium',10000);

INSERT INTO categoria (nombre) VALUES ('Artes y Humanidades'),('Ciencia'),('Deportes'),('Tecnología'),('Matematicas'); 

