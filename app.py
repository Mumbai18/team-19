from flasker import app, db
from flasker.models import Donor, Applicant, Student, Committee, Educon


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Donor': Donor, 'Applicant': Applicant, 'Student': Student, 'Committee':Committee, 'Educon':Educon}

if __name__ == '__main__':
    app.run()
    db.session.add(Applicant(username='nimish', password='sule'))
    db.session.commit()


