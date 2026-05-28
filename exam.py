from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Celebration</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(135deg, #ff6ec4, #7873f5, #42e695);
                font-family: Arial, sans-serif;
                overflow: hidden;
            }

            h1 {
                color: white;
                font-size: 4rem;
                text-align: center;
                text-shadow: 3px 3px 10px rgba(0,0,0,0.3);
                animation: pulse 1.5s infinite;
            }

            @keyframes pulse {
                0% { transform: scale(1); }
                50% { transform: scale(1.08); }
                100% { transform: scale(1); }
            }
        </style>
    </head>
    <body>
        <h1>Hooray! We Can Finally Take the Exams!</h1>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)