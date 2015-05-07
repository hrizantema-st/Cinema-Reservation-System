DROP TABLE IF EXISTS movies;
CREATE TABLE movies(id INTEGER PRIMARY KEY, name TEXT, rating REAL);
INSERT INTO movies(name, rating) VALUES('The Hunger Games: Catching Fire', 7.9),('Wreck-It Ralph', 7.8), ('Her', 8.3);

DROP TABLE IF EXISTS projections;
CREATE TABLE projections(id INTEGER PRIMARY KEY, movie_id INTEGER, type TEXT, data DATE, time TIME, FOREIGN KEY(movie_id) REFERENCES movies(id));
INSERT INTO projections (movie_id, type, data, time)
VALUES  (1, '3D', '2014-04-01', '19:10'),
        (1, '2D', '2014-04-01', '19:00'),
        (1, '4DX', '2014-04-02', '21:00'),
        (3, '2D', '2014-04-05', '20:20'),
        (2, '3D', '2014-04-02', '22:00'),
        (2, '2D', '2014-04-02', '19:30');

DROP TABLE IF EXISTS reservations;
CREATE TABLE reservations(id INTEGER PRIMARY KEY, username TEXT, projection_id INTEGER, row INTEGER, column INTEGER,
                         FOREIGN KEY (projection_id) REFERENCES projections(id));
INSERT INTO reservations (username, projection_id, row, column)
VALUES  ('RadoRado', 1, 2, 1),
        ('RadoRado', 1, 3, 5),
        ('RadoRado', 1, 7, 8),
        ('Ivo', 3, 1, 1),
        ('Ivo', 3, 1, 2),
        ('Mysterious', 5, 2, 3),
        ('Mysterious', 5, 2, 4);
