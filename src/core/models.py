from . import db
from sqlalchemy import ForeignKey
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Application models
ROLE_STUDENT = 0
ROLE_ADMIN = 1

user_focus = db.Table('user_focus',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('focus_id', db.Integer, db.ForeignKey('focus.id'))
)

org_focus = db.Table('org_focus',
    db.Column('org_id', db.Integer, db.ForeignKey('organisation.id')),
    db.Column('focus_id', db.Integer, db.ForeignKey('focus.id'))
)

user_org = db.Table('user_org',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('org_id', db.Integer, db.ForeignKey('organisation.id'))
)        

class User(db.Model):
    """ `User` is any entity which uses the application. User will
    have a valid facebook account to access the application.
    """
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255),nullable=False)
    date_of_birth = db.Column(db.Integer)
    college=db.Column(db.String(255),nullable=False)
    year_of_study = db.Column(db.Integer,nullable=False)
    branch = db.Column(db.String(60),nullable=False)
    blood_group=db.Column(db.String(5),nullable=False)
    email = db.Column(db.String(255),index = True,unique = True)
    news=db.Column(db.Boolean)
    phone = db.Column(db.Integer,nullable=False,unique=True)
    address=db.Column(db.String(255),nullable=False)
    facebook=db.Column(db.String(255),unique=True)
    linkedin=db.Column(db.String(255),unique=True)
    twitter=db.Column(db.Integer(255),unique=True)
    google=db.Column(db.Integer(255),unique=True)
    pintrest=db.Column(db.String(255),unique=True)
    role = db.Column(db.String(255),default = ROLE_STUDENT)
    blood = db.Column(db.Boolean)
    organ = db.Column(db.Boolean)
    disaster = db.Column(db.Boolean)
    focus = db.relationship('FocusAreas', secondary=user_focus)
    orgs = db.relationship('Organisation', secondary=user_org)
    def __repr__(self):
        return "<User:%d:%s:%s:%s>" % (self.id , self.first_name,self.email,self.last_name)

class Organisation(db.Model):
    """Organisation` is any entity which uses the application."""
    __tablename__ = "organisation"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    yer_es=db.Column(db.Integer(255),nullable=True)
    about=db.Column(db.String(255),nullable=True)
    reg_adr=db.Column(db.String(255),nullable=True)
    cor_adr=db.Column(db.String(255),nullable=True)
    contact_name=db.Column(db.String(255),nullable=True)
    contact_des=db.Column(db.String(255),nullable=True)
    icare_phone=db.Column(db.Integer,nullable=True)
    icare_mobile=db.Column(db.Integer,nullable=True)
    icare_fax=db.Column(db.Integer,nullable=True)
    website = db.Column(db.String(255),nullable=True)
    icare_email = db.Column(db.String(255),nullable=True)
    social = db.Column(db.Boolean)
    skills_based = db.Column(db.Boolean)
    micro = db.Column(db.Boolean)
    areaofwork = db.Column(db.String(255))
    community=db.Column(db.Boolean)
    intl_camp=db.Column(db.Boolean)
    dis_hr=db.Column(db.Boolean)
    dis_stationary=db.Column(db.Boolean)
    dis_software=db.Column(db.Boolean)
    dis_hardware=db.Column(db.Boolean)
    focus = db.relationship('FocusAreas', secondary=org_focus)

    def __repr__(self):
        return "<Organisation:%d:%s:%s:%s>" % (self.id , self.name,self.website,self.email)


class FocusAreas(db.Model):
    """'Focus Areas' is an entity which has focus areas as fields"""
    __tablename__ = "focus"
    id = db.Column(db.Integer,primary_key=True)
    interest_name=db.Column(db.String(255),nullable=False)

    def __repr__(self):
          return "<FocusAreas:%r:%r>" % (self.id,self.interest_name)



