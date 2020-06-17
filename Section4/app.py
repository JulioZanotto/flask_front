from flask import Flask
from flask_restful import Resource, Api
import sqlalchemy
from sqlalchemy import create_engine, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    'mysql://python_user:Python2!@localhost:3306/escola_curso?unix_socket=/var/run/mysqld/mysqld.sock',
    echo=True)

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()

Base = declarative_base()


class Alchemy(Base):
    __tablename__ = 'alchemy'

    id_item = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    description = sqlalchemy.Column('description', sqlalchemy.VARCHAR(45))
    quantity = sqlalchemy.Column('quantity', sqlalchemy.INTEGER())
    price = sqlalchemy.Column('price', sqlalchemy.FLOAT())
    status = sqlalchemy.Column('status', sqlalchemy.VARCHAR(45))


app = Flask(__name__)
api = Api(app)


class Item(Resource):

    def get(self, name):
        items = session.query(Alchemy).all()
        for item in items:
            if item.description == name:
                return {'name': item.description}, 200
        return {'message': 'item not found'}, 404

    def post(self, name):
        new_item = Alchemy(description=name,
                           quantity=1,
                           price=12,
                           status='received')

        session.add(new_item)
        session.commit()
        return {'message': 'item {} added'.format(name)}, 201


api.add_resource(Item, '/item/<string:name>')

app.run(debug=True)
