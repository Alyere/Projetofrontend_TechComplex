from flask import Flask, render_template, request 
app = Flask(__name__)

@app.route('/')
def home():
   
    return render_template('sobre.html', path=request.path)

@app.route('/complexidade')
def complexidade():
    
    return render_template('complexidade.html', path=request.path)

@app.route('/dicas')
def dicas():

    return render_template('dicas.html', path=request.path)

if __name__ == '__main__':
 
    app.run(debug=True)