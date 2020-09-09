INSERT INTO estudiante (id_estudiante, nombre, apellido, usuario, fecha_nacimiento, nacionalidad, id_plan) 
VALUES(1, 'James', 'Smith', 'JaSi412', '1994-01-01', 'Colombia', 1),
		(2, 'Emma', 'Jhonson', 'EmJh657', '1995-02-02', 'Canadá', 1),
		(3, 'Alexander', 'Smirnov', 'Alex456', '1996-03-03', 'USA', 1),
		(4, 'Anastasia', 'Ivanova', 'Ana2482', '1997-04-04', 'México', 1),
		(5, 'Li', 'Wei', 'Li684', '1998-05-05', 'Inglaterra', 1);
		(6, 'Wang', 'Fang', 'Wf784', '1999-06-06', 'España', 2),
		(7, 'Ben', 'Muller', 'Ben10', '2000-07-07', 'Argentina', 2),
		(8, 'Emma', 'Schmidt', 'Ema1496', '2001-08-08', 'Francia', 2),		
		(9, 'Miguel', 'Silva', 'Miguel698', '2002-09-09', 'Brasil', 2),	
		(10, 'Alicia', 'Santos', 'Alicia958', '2003-10-10', 'Italia', 2),
		(11, 'Andrea', 'Martinez', 'Andre1426', '1992-06-10', 'Colombia', 2),
		(12, 'Santiago', 'Colón', 'Santi1423', '2001-10-09', 'Italia', 2),
		(13, 'Julio', 'Villota', 'Julio032', '1986-02-07', 'Italia', 2);




INSERT INTO institucion (id_institucion, nombre, pais, tipo, calificacion) 
VALUES (1, 'MICROSOFT', 'USA', 'Empresa', 4.7),
		 (2, 'UNIVERSIDAD INDUSTRIAL DE SANTANDER', 'Colombia', 'Institución Educativa', 5),
		 (3, 'MIT', 'USA', 'Institución Educativa', 4.9),
		 (4, 'HARVARD', 'USA', 'Institución Educativa', 4.9),
		 (5, 'OXFORD', 'Inglaterra', 'Institución Educativa', 4.8);
		 
		 
INSERT INTO curso (id_curso, id_institucion, nombre , clases_teoricas, clases_practicas, calificacion) 
VALUES (1, 2, 'Introducción a Machine Learning', 10, 20, 4.8),
		 (2, 2, 'Fundamentos matemáticos para inteligencia artificial', 20, 5, 4.7),
		 (3, 2, 'Matemáticas discretas', 30, 15, 4.6),
		 (4, 2, 'Cálculo multivariable', 25,10, 4.4),
		 (5, 2, 'Redes neuronales en Keras y Scikit-Learn', 10, 30, 4.3),
		 (14, 2, 'Ecuaciones Diferenciales', 15, 40, 4.3),
		 (6, 1, 'Curso de Redes de Internet', 50, 40, 4.4),
		 (7, 1, 'Curso de introducción a la seguridad informática', 60, 40, 4.0),
		 (8, 1, 'Curso de Hacking ético', 60, 35, 4.0),
		 (9, 3, 'Curso de Community Manager', 22, 11, 4.2),
		 (10, 3, 'Curso de Marca Personal', 24, 12, 4.1),
		 (11, 4, 'Curso de teletrabajo', 15, 18, 4.2),
		 (12, 4, 'Introducción a los Negocios Online', 24, 12, 4.1),
		 (13, 5, 'Técnicas de negociación', 24, 12, 4.1);
		 		 		 		 		 		 

INSERT INTO especializacion (id_especializacion,  nombre , calificacion, nivel, id_institucion) 
VALUES (1, 'Inteligencia Artificial', 4.8, 'Difícil', 2),
		 (2, 'Seguridad Informática', 4.9, 'Medio', 1),
		 (3, 'Marketing Digital', 4.9, 'Fácil', 3),
		 (4, 'Escuela de Negocios', 4.9, 'Medio', 4),
		 (5, 'Matemáticas avanzadas', 4.9, 'Medio', 2);
		 		 		 

INSERT INTO plan_curso (id_plan, id_curso) 
VALUES (1, 1),
		 (1, 2),	
		 (2, 3),	
		 (2, 4),	
		 (2, 5),	
		 (2, 6),	
		 (1, 7),	
		 (2, 8),	
		 (2, 9),	
		 (2, 10),
		 (2, 11),
		 (1, 12),
		 (2, 13),
		 (1, 14);
		 
			 
INSERT INTO plan_especializacion (id_plan, id_especializacion) 
VALUES (2, 1),
		 (2, 2),
		 (1, 3),
		 (2, 4),
		 (1,5);


INSERT INTO curso_categoria (id_curso, id_categoria) 
VALUES (1, 2),
		 (1, 4),
		 (1, 5),
		 (2, 4),
		 (2, 5),
		 (3, 5),
		 (3, 2),
		 (3, 4),
		 (4, 5),
		 (4, 4),
		 (4, 3),
		 (5, 4),
		 (5, 5),
		 (5, 1),	
		 (6, 3),
		 (6, 4),
		 (6, 5),		 	
		 (7, 2),
		 (7, 3),
		 (7, 4),	
		 (8, 1),
		 (8, 2),
		 (8, 3),	
		 (9, 2),	
		 (9, 3),
		 (9, 4),
		 (10, 3),
		 (10, 4),
		 (10, 5),	
		 (11, 4),	
		 (11, 5),
		 (11, 2),
		 (12, 5),
		 (12, 4),
		 (12, 3),	
		 (13, 4),
		 (13, 5),
		 (13, 1),	
		 (14, 3),				 
		 (14, 4),
		 (14, 5);
		 
		 
