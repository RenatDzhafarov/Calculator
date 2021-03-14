from flask import Flask, render_template, request
app=Flask('__name__')

global n1,n2

@app.route('/')
def home():
    return render_template('web.html')


@app.route('/sum', methods=['GET', 'POST'])
def summa():
    n1=float(request.form['n1'])
    n2=float(request.form['n2'])
    res=n1+n2
    return render_template('web.html', n='The result is: {}'.format(res))

@app.route('/substract', methods=['GET', 'POST'])
def substract():
    n1=float(request.form['n1'])
    n2=float(request.form['n2'])
    res=n1-n2    
    return render_template('web.html', n='The result is: {}'.format(res))

@app.route('/multiply', methods=['GET', 'POST'])
def multiply():
    n1=float(request.form['n1'])
    n2=float(request.form['n2'])
    res=n1*n2    
    return render_template('web.html', n='The result is: {}'.format(res))

@app.route('/divide', methods=['GET', 'POST'])
def divide():
    n1=float(request.form['n1'])
    n2=float(request.form['n2'])
    res=n1/n2    
    return render_template('web.html', n='The result is: {:.2f}'.format(res))






if __name__ == '__main__':
    app.run(debug=True)