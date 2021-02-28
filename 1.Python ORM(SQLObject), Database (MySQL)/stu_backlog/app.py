import os
import logging
from flask import Flask,jsonify,request

import sqlobject
from sqlobject.mysql import builder

conn = builder()(user='sarang', password='password',
                 host='localhost', db='sqlobject')

app = Flask(__name__)



class Student(sqlobject.SQLObject):
    _connection = conn
    name = sqlobject.StringCol(length=255)
    backlog=sqlobject.IntCol(name=None)
    subjects = sqlobject.MultipleJoin('Subjects')
stu=Student.createTable(ifNotExists=True)


class Subjects(sqlobject.SQLObject):
    _connection = conn
    maths=sqlobject.IntCol(name=None)
    hindi=sqlobject.IntCol(name=None)
    science=sqlobject.IntCol(name=None)
    english=sqlobject.IntCol(name=None)
    student = sqlobject.ForeignKey('Student')
sub=Subjects.createTable(ifNotExists=True)


@app.route('/create_stu',methods=['POST'])
def createstud():
    request_data = request.get_json()
    Student(name=request_data['name'],
            backlog=request_data['backlog'] )
    return 'student created', 201


@app.route('/create_sub',methods=['POST'])
def createsub():
    request_data = request.get_json()
    Subjects(maths=request_data['maths'],
             hindi=request_data['hindi'],
             science=request_data['science'],
             english=request_data['english'],
             studentID=request_data['studentID'])
    return 'subject created', 201


@app.route('/get_stu', methods=['GET'])
def fetch_user():
    stud = Student.get(all('*'))
    sub= Subjects.get(all('*'))
    dict1 = {"name":stud.name, "backlog":stud.backlog,
             }
    dict2= {"maths":sub.maths,
            "hindi":sub.hindi,
            "science":sub.science,
            "english":sub.english,
            }
    return jsonify(dict1,dict2), 200


@app.route('/get_stu/<user_id>', methods=['GET'])
def fetch_user_by_id(user_id):
    stud = Student.get(int(user_id))
    sub= Subjects.get(int(user_id))
    dict1 = {"name":stud.name, "backlog":stud.backlog,
            }
    dict2= {"maths":sub.maths,
            "hindi":sub.hindi,
            "science":sub.science,
            "english":sub.english,
            }
    return jsonify(dict1,dict2), 200


@app.route('/del_stu/<user_id>', methods=['DELETE'])
def del_user_by_id(user_id):
    stud = Student.get(int(user_id))
    sub= Subjects.get(int(user_id))
    return 'student deleted with subjects marks'


'''
@app.route('/get_stu', methods=['GET'])
def get_stud():
    stud = Student.select(Student.q.id==Student.q.id,
                          Subjects.q.maths<33,
                          Subjects.q.hindi<33,
                          Subjects.q.science<33,
                          Subjects.q.english<33)
    #dict1 = {"name":stud.name, "backlog":stud.backlog,
           #  }
    list(stud)
    return jsonify(stud)
'''


# Setup Logging
def init_log(log_name):
    ''' configures rotating log file for the Project '''
    from logging.handlers import RotatingFileHandler

    # Logging Globals
    LOG_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"

    log_dir = os.getcwd()+'/log'
    log_file = log_dir + '/' + log_name + '.log'

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    global log
    log = logging.getLogger(log_name)
    handler = RotatingFileHandler(log_file, maxBytes=5000000, backupCount=3)
    formatter = logging.Formatter(LOG_FORMAT)
    handler.setFormatter(formatter)
    log.addHandler(handler)
    log.setLevel(logging.DEBUG)
    return log
log = None
log = init_log('stu_log')

@app.errorhandler(404)
def page_not_found(error):
    log.error('Page not found: %s', (request.path))
    return log.error('Page not found: %s', (request.path))


@app.errorhandler(500)
def internal_server_error(error):
    log.error('Server Error: %s' % error)
    return log.error('Server Error: %s' % error)


@app.errorhandler(Exception)
def unhandled_exception(e):
    log.error('Unhandled Exception: %s' % str(e))
    return log.error('Unhandled Exception: %s' % str(e))


@app.route('/exception')
def exception():
    ''' test exception handling '''
    raise Exception('THIS IS AN EXCEPTION ')


if __name__=="__main__":
    app.run(debug=True)


