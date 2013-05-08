from . import db
from sqlalchemy import ForeignKey
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Application models
ROLE_STUDENT = 0
ROLE_ADMIN = 1
class User(db.Model):
    """ `User` is any entity which uses the application. User will
    have a valid facebook account to access the application.
    """
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
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
	
    def __init__(self, username, first_name, last_name, date_of_birth, college, year_of_study, branch, blood_group, email, news, phone, address, facebook, linkedin, twitter, google, pintrest, role, blood, organ, disaster):
        self.username = username
        self.first_name =first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.college = college
        self.year_of_study = year_of_study
        self.branch = branch
        self.blood_group = blood_group
        self.email = email
        self.news = news
        self.phone = phone
        self.address = address
        self.facebook = facebook
        self.linkedin = linkedin
        self.twitter = twitter
        self.google = google
        self.pintrest = pintrest
        self.role = role
        self.blood = blood
        self.organ = organ
        self.disaster = disaster

    def __repr__(self):
        return "<User:%r:%r>" % (self.id , self.name,self.email,self.role)


class Organisation(db.Model):
    """Organisation` is any entity which uses the application."""
    __tablename__ = "organisation"
    id = db.Column(db.Integer, primary_key=True)
    orgname = db.Column(db.String(255), nullable=False) 
    name = db.Column(db.String(255), nullable=False)
    yer_es=db.Column(db.Integer(255),nullable=False)
    focus=db.Column(db.String(255),nullable=False)
    about=db.Column(db.String(255),nullable=False)
    reg_adr=db.Column(db.String(255),nullable=False)
    cor_adr=db.Column(db.String(255),nullable=False)
    contact_name=db.Column(db.String(255),nullable=False)
    contact_des=db.Column(db.String(255),nullable=False)
    icare_phone=db.Column(db.Integer,nullable=False)
    icare_mobile=db.Column(db.Integer,nullable=False)
    icare_fax=db.Column(db.Integer,nullable=False)
    website = db.Column(db.String(255),nullable=False)
    icare_email = db.Column(db.String(255),nullable=False)
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

    def __init__(self, orgname, name, yer_es, focus, about, reg_adr, cor_adr, contact_name, contact_des, icare_phone, icare_mobile, icare_fax, website, icare_email, social, skills_based, micro, areaofwork, community, intl_camp, dis_hr, dis_stationary, dis_software, dis_hardware):
        self.orgname = orgname
        self.name = name
        self.yer_es =yer_es
        self.focus =focus
        self.about = about
        self.reg_adr = reg_adr
        self.cor_adr = cor_adr
        self.contact_name = contact_name
        self.contact_des = contact_des
        self.icare_phone = icare_phone
        self.icare_mobile = icare_mobile
        self.icare_fax = icare_fax
        self.website = website
        self.icare_email = icare_email
        self.social = social
        self.skills_based = skills_based
        self.micro = micro
        self.areaofwork = areaofwork
        self.community = community
        self.intl_camp = intl_camp
        self.dis_hr = dis_hr
        self.dis_stationary = dis_stationary
        self.dis_software = dis_software
        self.dis_hardware = dis_hardware        

    def __repr__(self):
        return "<Organisation:%r:%r>" % (self.id , self.name,self.website,self.email)


class FocusAreas(db.Model):
    """'Focus Areas' is an entity which has focus areas as fields"""
    __tablename__ = "focus"
    id = db.Column(db.Integer,primary_key=True)
    interest_name=db.Column(db.Integer,nullable=False)

    def __repr__(self):
          return "<FocusAreas:%r:%r>" % (self.id,self.interest_name)


class UserFocus(db.Model):
     """'UserFocus' relates users to their interests"""
     __tablename__ = "userfocus"
     id=db.Column(db.Integer,db.ForeignKey("user.id"),primary_key=True)
     focus_id=db.Column(db.Integer,db.ForeignKey("focus.id"),primary_key=True)
     
     def __repr__(self):
          return "<UserFocus:%r:%r>" % (self.id,self.focus_id)


class OrgFocus(db.Model):
     """'UserFocus' relates users to their interests"""
     __tablename__ = "orgfocus"
     id=db.Column(db.Integer,db.ForeignKey("organisation.id"),primary_key=True)
     focus_id=db.Column(db.Integer,db.ForeignKey("focus.id"),primary_key=True)

     def __repr__(self):
          return "<OrgFocus:%r:%r>" % (self.id,self.focus_id)

