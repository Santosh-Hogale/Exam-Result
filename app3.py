# Integrate HTML with flask
# HTTP verb get and post
## Jinja Template
'''
{%..%} for loops,conditions, statements
{{  }} expressions to print output
{#..#} this is for comments
'''
from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index1.html")

@app.route('/success/<int:score>')
def success(score):
    res=" "
    if score>=50:
        res="Pass"
    else:
        res="Fail"
    exp={'score':score,'res':res}
    return render_template("result1.html",result=exp)

@app.route('/fail/<int:score>')
def fail(score):
    return 'the person has failed and mark is '+str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result=" "
    if marks<50:
        result="fail"
    else:
        result='success'
    return redirect(url_for(result,score=marks))

# Result checker  HTML Page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=="POST":
        Science=float(request.form['Science'])
        Maths=float(request.form['Maths'])
        C=float(request.form['C'])
        Datascience=float(request.form['Datascience'])
        total_score=(Science+Maths+C+Datascience)/4
    res=" "
    return redirect(url_for('success',score=total_score))

    
if __name__=='__main__':
    app.run(debug=True)