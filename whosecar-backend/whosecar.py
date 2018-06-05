from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\Benjamin Dow\Desktop\whosecar\whosecar-backend\whosecar.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Templates
from CarpoolManagement.Carpools import CarPassengers, Cars, Carpool

# Routes
from CarpoolManagement.CarpoolManagement import NewCarpool, Car, PassengersByCar

#Add Api Routes
api.add_resource(NewCarpool, '/Carpool/<CarpoolID>')
api.add_resource(Car, '/Carpool/<CarpoolID>/Cars/')
api.add_resource(PassengersByCar,'/Car/<CarID>/Passengers')


#Set Up Database
#db.session.query(Carpool).delete()
#db.session.query(Cars).delete()
#db.session.commit()
db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
