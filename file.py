from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Front-End</title>

    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(to right, #1e3c72, #2a5298);
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            text-align: center;
            background: rgba(255,255,255,0.1);
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }

        h1 {
            font-size: 3rem;
            margin-bottom: 10px;
        }

        p {
            font-size: 1.2rem;
            margin-bottom: 20px;
        }

        button {
            background: white;
            color: #2a5298;
            border: none;
            padding: 12px 25px;
            font-size: 1rem;
            border-radius: 8px;
            cursor: pointer;
            transition: 0.3s;
        }

        button:hover {
            background: #dbeafe;
            transform: scale(1.05);
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Welcome Ahmed 🚀</h1>
        <p>This front-end webpage is powered by Python Flask.</p>

        <button onclick="showMessage()">Click Me</button>
    </div>

    <script>
        function showMessage() {
            alert('Your Python Front-End is Working!');
        }
    </script>

</body>
</html>
"""

@app.route('/')
def home():
    return "<h1>Flask Docker App Working 🚀</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
