INSERT INTO main_region (nombre, numero) VALUES ("Región de Tarapacá", "I"), ("Región de Antofagasta", "II"), ("Región de Atacama", "III"), ("Región de Coquimbo", "IV"), ("Región de Valparaíso", "V"), ("Región de Libertador General Bernardo O\'Higgins", "VI"), ("Región del Maule", "VII"), ("Región del Bio Bio", "VIII"), ("Región de la Araucanía", "IX"), ("Región de Los Lagos", "X"), ("Región de Aysén del General Carlos Ibáñez del Campo", "XI"), ("Región de Magallanes", "XII"), ("Región Metropolitana", "RM"), ("Región de Los Ríos", "XIV"), ("Región de Arica y Parinacota", "XV");

INSERT INTO main_ciudad (nombre, region_id) VALUES ("Valparaíso", 5), ("Viña del Mar", 5), ("Santiago", 13), ("Concepción", 8), ("Valdivia", 14), ("La Serena", 4), ("Tarapacá", 15), ("Temuco", 9);

INSERT INTO evaluaciones_motivoabuso(nombre) VALUES ('Contraparte no asistió'),('Pago/Cobro incorrecto'),('No cumple con acuerdo'),('Otros');


INSERT INTO ayudantias_categoria(nombre) VALUES ('Matemáticas'), ('Biología'), ('Química');

INSERT INTO ayudantias_subcategoria(nombre, categoria_id) VALUES ('Cálculo', 1),('Álgebra', 1), ('Ecuaciones diferenciales', 1);
