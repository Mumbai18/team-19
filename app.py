from flasker import app
from flasker.models import  Applicant, Student, Donor, Committeemembers,  Donates, Volunteer, db

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Applicant': Applicant, 'Student': Student, 'Donor': Donor, 'Committeemembers': Committeemembers,
            'Donates': Donates, 'Volunteer': Volunteer}

if __name__ == '__main__':
    app.run()


