from flask import Flask
import subprocess
import os
import datetime
import getpass



app = Flask(__name__)

def get_top_output():
    result = subprocess.run(["top", "-b", "-n", "1"], capture_output=True, text=True)
    return result.stdout

@app.route("/htop")
def htop():
    name = "Garima Jain"
    username = getpass.getuser() 
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    top_output = get_top_output()

    response = f"""
    <h1>Name: {name}</h1>
    <h2>Username: {username}</h2>
    <h3>Server Time (IST): {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</h3>
    <pre>{top_output}</pre>
    """
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

