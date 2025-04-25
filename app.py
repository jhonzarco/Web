from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return "<h1><strong>Esta es la página de About.</strong></h1><p>Esta es una página de ejemplo para mostrar cómo funciona Flask.</p>"

@app.route('/tasks')
def list_tasks():
    return "Lista de tareas"

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)