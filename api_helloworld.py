from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    user_agent = request.headers.get('User-Agent')
    if 'Chrome' in user_agent:
        app.logger.info("Chrome browser detected")
        return 'Hello Google'
    elif 'Firefox' in user_agent:
        app.logger.info("Firefox browser detected")
        return 'Hello Firefox'
    else:
        app.logger.info("Other browser detected")
        return 'Hello World'

if __name__ == '__main__':
    # Bind to all interfaces
    app.run(host='0.0.0.0', port=5001, debug=True)



