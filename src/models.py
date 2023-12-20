import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


# Creamos una class que será el Modelo instanciando de Base. Naming convention: PascalCase en plural
    # 1. Creamos el alias de la tabla __tablename__ . Naming convention: snake_case
    # 2. Columnas, 
    # 2.1. Clave primaria. Tipo de dato, primary_key=True
    # 2.2. Atributos del modelo. Tipo de dato(longitud), acepta datos vacíos?, es un dato único?
    # 2.3. Clave foránea. Tipo de dato, ForeignKey('alias.id')
    # 3. Relaciones. relationship(Models)
    # 4. Métodos


Base = declarative_base()

# Creamos una class que será el Modelo instanciando de Base. Naming convention: PascalCase en plural
class Users(Base):
    # 1. Creamos el alias de la tabla __tablename__ . Naming convention: snake_case
    __tablename__ = 'users'
    # 2. Columnas, 
    # 2.1. Clave primaria. Tipo de dato, primary_key=True
    id = Column(Integer, primary_key=True)
    # 2.2. Atributos del modelo. Tipo de dato(longitud), acepta datos vacíos?, es un dato único?
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    subscrition_date  = Column(Date)



class Profiles(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    # 2.2. Atributos del modelo. Tipo de dato(longitud), acepta datos vacíos?, es un dato único?
    firstname = Column(String(20), nullable=False)
    lastname = Column(String(20), nullable=False)
    nickname =  Column(String(20), nullable=False)
    image_url =  Column(String(120), nullable=False)
    # 2.3. Clave foránea. Tipo de dato, ForeignKey('alias.id')
    # 3.3 One to One
    users_id = Column(Integer, ForeignKey('users.id'), unique=True)
    # 3. Relaciones. relationship(Models)
    users = relationship(Users)


class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    # 3.3 One to Many
    users_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users)

    def to_dict(self):
        return {}


# Creamos una class que será el Modelo instanciando de Base. Naming convention: PascalCase en plural
class Characters(Base):
    # 1. Creamos el alias de la tabla __tablename__ . Naming convention: snake_case
    __tablename__ = 'characters'
    # 2. Columnas, 
    # 2.1. Clave primaria. Tipo de dato, primary_key=True
    id = Column(Integer, primary_key=True)
    # 2.2. Atributos del modelo. Tipo de dato(longitud), acepta datos vacíos?, es un dato único?
    name = Column(String(100), nullable=False)
    description = Column(String(250), nullable=False)
    height = Column(Integer)
    mass = Column(String)
    hair_color = Column(String)
    skin_color = Column(String)
    eye_color = Column(String)
    birth_year = Column(String)
    gender = Column(String)
    homeworld = Column(String)
    url = Column(String)


# Creamos una class que será el Modelo instanciando de Base. Naming convention: PascalCase en plural
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(Integer)
    population = Column(Integer)
    climate = Column(Integer)
    terrain = Column(Integer)
    surface_water = Column(Integer)
    url = Column(Integer)

# Creamos una class que será el Modelo instanciando de Base. Naming convention: PascalCase en plural
class FavoriteCharacters(Base):
    # 1. Creamos el alias de la tabla __tablename__ . Naming convention: snake_case
    __tablename__ = 'favorite_characters'
    # 2. Columnas, 
    # 2.1. Clave primaria. Tipo de dato, primary_key=True
    id = Column(Integer, primary_key=True)
    # 2.3. Clave foránea. Tipo de dato, ForeignKey('alias.id')
    users_id = Column(Integer, ForeignKey('users.id')) # int fk >-< users.id
    characters_id  = Column(Integer, ForeignKey('characters.id'))
    # 3. Relaciones. relationship(Models)
    users = relationship(Users)
    characters = relationship(Characters)


class FavoritePlanets(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True)
    # 3.3 Many to Many
    users_id = Column(Integer, ForeignKey('users.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    users = relationship(Users)
    planets = relationship(Planets)


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
