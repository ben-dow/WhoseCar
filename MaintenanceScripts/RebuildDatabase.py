print("Are You Sure? This erases everything!\n")

answer = input()

if answer == "y":
    import os

    try:
        os.remove("test.db")
    except:
        pass

    from WhoseCar import db

    db.create_all()

