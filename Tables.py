import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , Integer , String , ForeignKey
from sqlalchemy.orm import sessionmaker , relationship , backref

engine = sqlalchemy.create_engine('postgresql://webadmin:VCNtps41396@node37019-thanet.proen.app.ruk-com.cloud:5432/homework') 
Base = declarative_base()

class STUDENT(Base):
        __tablename__ = 'students'
        student_id = Column(String(13), primary_key = True ,nullable=True)
        f_name = Column(String(30),nullable=True)
        l_name = Column(String(30),nullable=True)
        e_mail = Column(String(50),nullable=True)

        def __repr__(self) :
                return '<User(student_id = {} , f_name = {} , l_name = {} , e_mail = {})>'.format(self.student_id,self.f_name,self.l_name,self.e_mail)

class REGISTRATION(Base):
        __tablename__ = "registrations"
        id = Column(Integer, primary_key=True, nullable=True)
        student_id = Column(String(13), nullable=True)
        subject_id = Column(String(15), nullable=True)
        year = Column(String(4), nullable=True)
        semester = Column(String(1), nullable=True)
        grade = Column(String(2), nullable=True)
        
        def __repr__(self):
                return '<User(student_id = {} , subject_id = {} , year = {} , semester = {} , grade = {})>'.format(self.student_id,\
                        self.subject_id, self.year , self.semester , self.grade)

class SUBJECT(Base):
        __tablename__ = 'subjects'
        subject_id = Column(String(15),primary_key=True, nullable=True)
        subject_name = Column(String(50), nullable=True)
        creadit = Column(Integer, nullable=True)
        teacher_id = Column(String(3), nullable=True)


        def __repr__(self):
                return '<User(subject_id = {} , subject_name= {} , creadit = {} , teacher_id = {})>'.format(self.subject_id,\
                        self.subject_name, self.creadit , self.teacher_id)

class TEACHER(Base):
        __tablename__ = 'teachers'
        teacher_id = Column(String(3),primary_key=True, nullable=True)
        teacher_f_name = Column(String(50), nullable=True)
        teacher_l_name = Column(String(30), nullable=True)
        teacher_e_mail = Column(String(50), nullable=True)

        def __repr__(self):
                return '<User(teacher_id = {} , teacher_f_name= {} , teacher_l_name = {} , teacher_e_mail = {})>'.format(self.teacher_id,\
                        self.teacher_f_name, self.teacher_l_name , self.teacher_e_mail)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

Student_1 = STUDENT(student_id='6406022620029',f_name='Thanet',l_name='Suwannapirom',e_mail='s6406022620029@gmail.com')
Student_2 = STUDENT(student_id='6406022610015',f_name='Kongphop',l_name='Sri-On',e_mail='s6406022610015@gmail.com')
Student_3 = STUDENT(student_id='6406022020053',f_name='Watcharakorn',l_name='Yentaweesub',e_mail='s64060262620053@gmail.com')

Registration_1 = REGISTRATION(student_id='6406022620029',subject_id='060233113',year='2565',semester='1',grade='A')
Registration_2 = REGISTRATION(student_id='6406022620029',subject_id='060233201',year='2565',semester='1',grade='A')
Registration_3 = REGISTRATION(student_id='6406022610015',subject_id='060233113',year='2565',semester='1',grade='A')
Registration_4 = REGISTRATION(student_id='6406022610015',subject_id='060233205',year='2565',semester='1',grade='B+')
Registration_5 = REGISTRATION(student_id='6406022020053',subject_id='060233201',year='2565',semester='1',grade='A')
Registration_6 = REGISTRATION(student_id='6406022020053',subject_id='060233205',year='2565',semester='1',grade='B')

Subject_1 = SUBJECT(subject_id='060233113',subject_name='ADVANCED COMPUTER PROGRAMMING',creadit=3,teacher_id='AMK')
Subject_2 = SUBJECT(subject_id='060233205',subject_name='ADVANCED NETWORK AND PROTOCOL',creadit=3,teacher_id='KNM')
Subject_3 = SUBJECT(subject_id='060233201',subject_name='NETWORK ENGINEERING LABORATORY',creadit=1,teacher_id='WKN')

Teacher_1 = TEACHER(teacher_id='AMK',teacher_f_name='Anirach',teacher_l_name='Mingkhwan',teacher_e_mail='Anirach@gmail.com')
Teacher_2 = TEACHER(teacher_id='KNM',teacher_f_name='Khanista',teacher_l_name='Namee',teacher_e_mail='Khanista@gmail.com')
Teacher_3 = TEACHER(teacher_id='WKN',teacher_f_name='Watcharachai',teacher_l_name='Kongsiriwattana',teacher_e_mail='Watcharachai@gmail.com')

session.add_all([Student_1,Student_2,Student_3,Registration_1,Registration_2,Registration_3,Registration_4,Registration_5,Registration_6,\
        Subject_1,Subject_2,Subject_3,Teacher_1,Teacher_2,Teacher_3])
print(session.query(STUDENT).all())
session.commit()
