from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
  return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Мой Профиль</title>
        <style>
            body {
                background-color: #f0f2f5;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
            }
            .card {
                background: white;
                width: 320px;
                border-radius: 20px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.15);
                overflow: hidden;
                text-align: center;
            }
            .card img {
                width: 100%;
                height: 380px;
                object-fit: cover;
            }
            .info {
                padding: 15px;
            }
            .info h2 {
                margin: 5px 0;
                font-size: 22px;
            }
            .info p {
                color: #666;
                font-size: 14px;
                margin-bottom: 15px;
            }
            .buttons {
                display: flex;
                justify-content: space-around;
                padding-bottom: 20px;
            }
            .btn {
                width: 50px;
                height: 50px;
                border-radius: 50%;
                border: none;
                font-size: 22px;
                cursor: pointer;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }
            .dislike { background: #fff; color: #fd5068; border: 2px solid #fd5068; }
            .like { background: #2db9b0; color: white; }
        </style>
    </head>
    <body>
        <div class="card">
            <img src="https://picsum.photos/400/500" alt="Фото профиля">
            <div class="info">
                <h2>Barsbek </h2>
                <p>Создатель сайтов | Разработчик</p>
            </div>
            <div class="buttons">
                <button class="btn dislike">❌</button>
                <button class="btn like">💚</button>
            </div>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
  app.run()
