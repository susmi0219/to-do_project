from flask import Flask, render_template,request, redirect, url_for, abort

app = Flask(__name__)

todos =[
    {'id' : 1, 'task': 'Learn flask'},
    {'id' : 2, 'task': 'Build a project'},
    {'id' : 3, 'task': 'Deploy the app'}
]
next_id = 4
@app.route('/')
def get_todos():
    return render_template('todos.html', todos=todos)
if __name__=='__main__':
    app.run(debug=True)