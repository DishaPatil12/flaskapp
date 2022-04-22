from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def home():
    # return 'Hello World'
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/task')
def register1():
    return render_template('task.html')

# @app.route('/task')
# def task():
#     return render_template('task.hmtl')
    

if __name__ == '__main__':  
    app.run(debug = True)  