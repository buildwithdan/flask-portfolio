import os

path = os.getcwd()
parent = os.path.dirname(path)

('python application.py')

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=9000)