from flask import Flask, request, render_template
import sqlite3
import json

GrouPayApp = Flask(__name__)


@GrouPayApp.route("/")
def GroupPayHome():
    return render_template("HomePage.html")


@GrouPayApp.route("/GrouPayEntry")
def GroupPayEntry():
    return render_template("form.html")


@GrouPayApp.route("/form.html")
def FormDataFetch():
    # fetching data from the JS page
    con = sqlite3.connect("Group.db")
    c = con.cursor()
    c.execute("SELECT * FROM Group")
    rows = c.fetchall()
    con.close()


if __name__ == "__main__":
    GrouPayApp.run(debug=True, port=5000)


# from flask import Flask, request, render_template
# import sqlite3
# import json

# app = Flask(__name__)


# @app.route("/About.html")
# def About():
#     return render_template("About.html")


# @app.route("/check_song/<songID>")
# def check_song(songID):
#     try:
#         conn = sqlite3.connect("playlist.db")
#         c = conn.cursor()

#         c.execute("SELECT EXISTS(SELECT 1 FROM playlist WHERE songID = ?)", (songID,))
#         result = c.fetchone()

#         conn.close()

#         return json.dumps({"exists": result[0]})
#     except Exception as e:
#         print(e)
#         return json.dumps({"exists": False})


# @app.route("/store_data", methods=["POST"])
# def store_data():
#     data = request.get_json()

#     # Store data in SQLite3 database
#     conn = sqlite3.connect("playlist.db")
#     c = conn.cursor()

#     c.execute(
#         """CREATE TABLE IF NOT EXISTS playlist
#                  (songName TEXT, songDuration TEXT, album TEXT, artistID TEXT, songID TEXT)"""
#     )

#     c.execute(
#         "INSERT INTO playlist VALUES (?, ?, ?, ?, ?)",
#         (
#             data["songName"],
#             data["songDuration"],
#             data["album"],
#             data["artistID"],
#             data["songID"],
#         ),
#     )
#     conn.commit()
#     conn.close()

#     return "", 204


# @app.route("/delete_song", methods=["POST"])
# def delete_song():
#     data = request.get_json()

#     # Delete song from SQLite3 database
#     conn = sqlite3.connect("playlist.db")
#     c = conn.cursor()

#     c.execute("DELETE FROM playlist WHERE songID=?", (data["songID"],))
#     conn.commit()
#     conn.close()

#     return "", 204


# @app.route("/PlayList.html")
# def playlist():
#     # Fetch data from SQLite3 database
#     conn = sqlite3.connect("playlist.db")
#     c = conn.cursor()
#     c.execute("SELECT * FROM playlist")
#     rows = c.fetchall()
#     conn.close()

#     # Generate HTML for table rows
#     rows_html = ""
#     for row in rows:
#         song_name = row[0]
#         song_duration = row[1]
#         album = row[2]
#         artist_id = row[3]
#         song_id = row[4]

#         row_html = f"""
#             <tr>
#                 <td>{song_name}</td>
#                 <td>{artist_id}</td>
#                 <td>{album}</td>
#                 <td>{song_duration}</td>
#                 <td><button class="delete_button" data-songid="{song_id}">-</button></td>
#             </tr>
#         """

#         rows_html += row_html

#     # Render PlayList.html template with dynamic rows
#     return render_template("PlayList.html", rows=rows_html)


# if __name__ == "__main__":
#     app.run(debug=True, port=5000)
