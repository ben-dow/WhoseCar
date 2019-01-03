from WhoseCar import db


def CommitToSession(ModelObjects):
    for m in ModelObjects:
        db.session.add(m)

    db.session.commit()
