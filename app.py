from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

ENV = 'dev'

if ENV =='dev':
    app.debug =True
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:vanadam11@localhost/flask_project'
else:
    app.debug=False
    app.config['SQLALCHEMY_DATABASE_URI']=''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class FeedBack(db.Model):
    __tablename__ ='feedback'
    id = db.Column(db.Integer,primary_key=True)
    customer = db.Column(db.String(200),unique=True,nullable=False)
    dealer = db.Column(db.String(100),nullable=False)
    rating = db.Column(db.Integer)
    comments = db.Column(db.String(200))
    
    def __init__(self, customer, dealer, rating, comments):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments 

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        comments = request.form['comments']
        rating = request.form['rating']
        if customer=='' or dealer=='':
            return render_template('index.html', message='fill customer and dealer it a must')
        
        if db.session.query(FeedBack).filter(FeedBack.customer==customer).count()==1:
            return render_template('index.html',message='data already exist')
        data = FeedBack(customer,dealer,rating,comments)
        db.session.add(data)
        db.session.commit()
        send_mail(customer,dealer,rating, comments)
        return render_template('success.html')


if __name__ == '__main__':
    app.run()