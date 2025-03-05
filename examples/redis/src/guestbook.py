from flask import Flask, request, redirect, url_for
import redis

# Point this to your Redis service name and port (as used in Kubernetes Service)
r = redis.Redis(host="redis-service", port=6379, db=0)

app = Flask(__name__)

@app.route('/')
def index():
    entries = r.lrange('guestbook', 0, -1)
    # Redis stores bytes, so decode to UTF-8
    formatted_entries = [e.decode('utf-8') for e in entries]

    return '''
    <html>
      <head>
        <title>Guestbook</title>
      </head>
      <body>
        <h1>Simple Guestbook</h1>
        <ul>
          {}
        </ul>
        <form action="/sign" method="POST">
          <input name="entry" type="text" />
          <button type="submit">Sign Guestbook</button>
        </form>
      </body>
    </html>
    '''.format('<br>'.join(formatted_entries))

@app.route('/sign', methods=['POST'])
def sign():
    entry = request.form.get('entry', '')
    if entry:
        r.lpush('guestbook', entry)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
