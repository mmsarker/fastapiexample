from models import User


def create_user(db, user):
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_users(db):
    return db.query(User).all()


def get_user(db, user_id):
    return db.query(User).filter(User.id == user_id).first()


def update_user(db, user_id, data):
    user = get_user(db, user_id)
    if not user:
        return None

    for key, value in data.dict(exclude_unset=True).items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user


def delete_user(db, user_id):
    user = get_user(db, user_id)
    if not user:
        return None

    db.delete(user)
    db.commit()
    return user
