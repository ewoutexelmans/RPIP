from flask import Flask
app = Flask(__name__)

n = 0

@app.rout("/")
def hello():
    global n
    n += 1
    x = "Hello world, this is visit nr: "+str(n)
    return x

if __name__ == "__main__":
    app.run(host="0.0.0.0")
