from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
  return "Привет меня зовут Барсбек и это мой сайт!"


if __name__ == "__main__":
  app.run()
