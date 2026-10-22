from Models.model import *
from flask import Flask

app=Flask(__name__)

app.config['SECRET_KEY']="East"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///gs_store.sqlite3'

db.init_app(app)


with app.app_context():
    db.create_all()
    
    
    
if __name__=="__main__":
    app.run(port=5000,debug=True)
    
    




