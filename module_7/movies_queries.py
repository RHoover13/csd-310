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

cursor = db.cursor()

cursor.execute("SELECT studio_id, studio_name FROM studio")

studios = cursor.fetchall()

print("\n  -- DISPLAYING Studio RECORDS --")

for studio in studios:
    print(" Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

cursor.execute("SELECT genre_id, genre_name FROM genre")

genres = cursor.fetchall()

print("\n  -- DISPLAYING Genre RECORDS --")

for genre in genres:
    print(" Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

input("\n\n Press any key to continue...")

query = "SELECT film_name, film_runtime FROM film WHERE film_runtime < 120"
cursor.execute(query)

short_films = cursor.fetchall()

print("\n  -- DISPLAYING Short Film RECORDS --")

for short_film in short_films:
    print(" Film Name: {}\nFilm Runtime: {}\n".format(short_film[0], short_film[1]))

input("\n\n Press any key to continue...")

query = "SELECT film_name, film_director FROM film ORDER BY film_director"
cursor.execute(query)

director = cursor.fetchall()

print("\n  -- DISPLAYING Director RECORDS In Order --")

for ordered in director:
    print(" Film Name: {}\nDirector: {}\n".format(ordered[0], ordered[1]))

input("\n\n Press any key to continue...")

db.close()
