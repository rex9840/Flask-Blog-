from flask import Flask ,render_template,url_for,flash ,redirect
from forms import RegistrationForm,LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'cc45efa93621f7211f5dfffa1af0ab90'

#import secrets 
#secrets.token_hex(16)

#Dummy Data 

posts = [
    {
        'author' : 'Rock',
        'title' : 'wwe champions ',
        'content' : 'wwe is the best',
        'date_posted' : 'April 20, 2020'
    },
    {
        'author' : 'John Cena ',
        'title' : 'wwe world heavyweight champion',
        'content' : 'wwe is the best',
        'date_posted' : 'April 20, 2020'
    }
    
    
    
]




@app.route("/")
@app.route("/home")
def home():
    return render_template(template_name_or_list="home.html",posts=posts )




@app.route("/about")
def about():
    return render_template("about.html",title='About')


@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}','success')
        return redirect(url_for('home'))
    return render_template("register.html",title='Register',form = form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html",title='Login',form = form)




if __name__ == "__main__":
    app.run(debug=True,port=8000)