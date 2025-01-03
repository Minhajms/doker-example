from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Welcome to Flask</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    color: #333;
                    text-align: center;
                    padding: 50px;
                }
                h1 {
                    color: #007BFF;
                }
                p {
                    font-size: 1.2em;
                }
            </style>
        </head>
        <body>
            <h1>Hello, Flask!</h1>
            <p>Welcome to my Flask app with some basic styling. Enjoy!</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
