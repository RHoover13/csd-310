import mysql.connector
from mysql.connector import errorcode
from pymysql import err

config = {
    "user": "root",
    "password": "Laura0413!",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"]))
    input("\n\n Press any key to continue...")

except mysql.connector as Error:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The supplied database does not exist")

    else:
        print(err)


def show_films(cursor, title):
    cursor.execute("select film_name as Name, film_director as Director, genre_name as Genre, "
                   "studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id = genre.genre_id "
                   "INNER JOIN studio ON film.studio_id = studio.studio_id")

    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2],
                                                                                         film[3]))


cursor = db.cursor()

show_films(cursor, "--DISPLAYING FILMS--")

add_film = ("INSERT INTO film(film_id, film_name, film_releaseDate, film_runtime, film_director, studio_id, "
            "genre_id)"
            "VALUES('4', 'Lone Survivor', '2013', '121', 'Peter Berg', '3', '3')")

cursor.execute(add_film)

db.commit()

show_films(cursor, "--DISPLAYING FILMS AFTER INSERT--")

update_film = "UPDATE film SET genre_id = 1 WHERE film_name = 'Alien'"

cursor.execute(update_film)

show_films(cursor, "--DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror--")

delete_film = "DELETE FROM film WHERE film_name = 'Gladiator'"

cursor.execute(delete_film)

show_films(cursor, "--DISPLAYING FILMS AFTER DELETE--")

db.close()
