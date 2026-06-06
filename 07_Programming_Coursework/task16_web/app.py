from flask import Flask, render_template, request, redirect, url_for
import sql_connection

app = Flask(__name__)

# …instead of @app.before_first_request…
# make sure the table exists as soon as your app is imported:
sql_connection.create_db_table()


# Alias “/” to your index.html route
@app.route('/', methods=["GET", "POST"])
@app.route('/index.html', methods=["GET", "POST"])
def home():
    return render_template('index.html', title='Home Page')


@app.route('/input_page.html', methods=["GET", "POST"])
def input_page_fuction():
    if request.method == "POST":
        mood     = request.form.get('mood', '')
        genre    = request.form.get('genre', '')
        username = request.form.get('username', '').strip()

        return redirect(url_for(
            'output_page_fuction',
            mood=mood,
            genre=genre,
            username=username
        ))

    return render_template('input_page.html', title='Find My Song')


@app.route('/output_page.html', methods=["GET"])
def output_page_fuction():
    mood     = request.args.get('mood')
    genre    = request.args.get('genre')
    username = request.args.get('username')

    if not (mood and genre and username):
        return redirect(url_for('input_page_fuction'))

    # 1) pick recommendation
    recommendations = {
      'happy': {
        'rock':    ("Don't Stop Me Now",     'https://open.spotify.com/track/43DHLzDkncpby82Po5jlOZ'),
        'pop':     ('Happy',                 'https://open.spotify.com/track/6NPVjNh8Jhru9xOmyQigds'),
        'jazz':    ('Summertime',            'https://open.spotify.com/track/20XdEFyaUR9C7aDIdq2OAd')
      },
      'sad': {
        'rock':    ('Nutshell',              'https://open.spotify.com/track/2JuasWPUodaUxf5nwNpciQ'),
        'pop':     ('Someone Like You',      'https://open.spotify.com/track/4kflIGfjdZJW4ot2ioixTB'),
        'jazz':    ('Someone to Watch Over Me','https://open.spotify.com/track/65AdKtpL8F3alW7QLD5UNj')
      },
      'relaxed': {
        'rock':    ('Wish You Were Here',    'https://open.spotify.com/track/7pKfPomDEeI4TPT6EOYjn9'),
        'pop':     ('Butterflies',           'https://open.spotify.com/track/1dWUBCoztAMZcqec1CAE6z'),
        'jazz':    ('So What',               'https://open.spotify.com/track/2RlgNHKcydI9sayD2Df2xp')
      }
    }
    rec = recommendations.get(mood, {}).get(genre)

    # 2) persist it
    if rec:
        sql_connection.insert_data(
            0, 0, 0, 0, 0,      # dummy ints
            username,           # str_field1
            mood,               # str_field2
            genre,              # str_field3
            rec[0],             # str_field4 = title
            rec[1]              # str_field5 = URL
        )

    # 3) render
    return render_template(
        'output_page.html',
        title='Your Recommendation',
        mood=mood,
        genre=genre,
        username=username
    )


if __name__ == '__main__':
    # (you already created the table at import time)
    app.run(debug=True)
