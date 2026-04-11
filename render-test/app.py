from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "WhatsApp Bot Running 🚀"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return "Webhook verified ✅"
    if request.method == 'POST':
        data = request.json
        print(data)
        return "Message received"

if __name__ == '__main__':
    app.run()