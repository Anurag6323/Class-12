from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SQLALCHEMY_DATABSE_URI']= 'sqlite:///test.db'
db=SQLAlchemy(app)


class Todo(db.Model):
    id=db.Column(db.integer, primary_key=True)
    content=db.Column(db.String(200), nullable=False)
    completed=db.Column(db.Integer,default=0)
    data_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id
#stuck after this because of some terminal thing

@app.route("/")

def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run()
