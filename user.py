from flask import render_template,request,session,flash,redirect,url_for
from flask.helpers import flash
from projectapp import app,db
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from sqlalchemy import func

from projectapp.mymodels import Member
from projectapp.myforms import LoginForm,SignupForm


@app.route('/login', methods=['POST','GET'])
def login():
    logform=LoginForm()
    if request.method=='GET':
        return render_template('user/login.html',logform=logform)
    else:
        if logform.validate_on_submit():
            username = request.form.get('email') 
            password = logform.password.data 
            urban = Member.query.filter(Member.member_email==username).first()
            if urban != None:
                stored_hash = urban.member_pwd
                check = check_password_hash(stored_hash,password)

                if check:                  
                    session['userid'] = urban.id 
                    return redirect(url_for('dashboard'))
                else:
                    flash('Invalid Details, try again')
                    return redirect(url_for('login'))
            else:
                flash('Invalid Details, try again')
                return redirect(url_for('login')) 

        else:
            return render_template('user/every.html',logform=logform)



    return render_template('user/login.html')

@app.route('/signup' ,methods=['POST','GET'])
def signup():
    if request.method=='GET':
        return render_template('user/signup.html')
    else:
        fname=request.form.get('fname')
        sname=request.form.get('sname')
        email=request.form.get('email')
        password=request.form.get('psw')
        password1=request.form.get('psw-repeat')
        if password != password1:
            flash('Passwords are not the same')
            return redirect('/signup')
        else:
            enc_pass = generate_password_hash(password)
            m=Member(member_fname=fname,member_lname=sname,member_email=email,member_phone='',member_pwd=enc_pass,member_pix='',member_dob='')
            db.session.add(m)
            db.session.commit()
            session['user_id']=m.id
            flash('Congrats! you are now registered')
            return redirect(url_for('login'))

@app.route('/')
@app.route('/home')
def home():
    loggedin=session.get('userid')
    if loggedin:
        data=Member.query.get(loggedin)
    return render_template('user/every.html',data=data)

@app.route('/testimonials')
def testimonial():
    return render_template('user/testimonial.html')

@app.route('/loginsin')
def test():
    return render_template('user/login2.html')
            
            


