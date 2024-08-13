import os
from flask import Flask, request

app = Flask(__name__)

# Get the suffix from an environment variable, default to '42' if not set
suffix = os.getenv('SUFFIX', '22')

@app.route('/')
def hello_world():
    user_agent = request.headers.get('User-Agent')
    if 'Chrome' in user_agent:
        app.logger.info("Chrome browser detected")
        return f'Hello Google{suffix}'
    elif 'Firefox' in user_agent:
        app.logger.info("Firefox browser detected")
        return f'Hello Firefox{suffix}'
    else:
        app.logger.info("Other browser detected")
        return f'Hello World{suffix}'

if __name__ == '__main__':
    # Bind to all interfaces
    app.run(host='0.0.0.0', port=5001, debug=True)




