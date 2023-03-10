from flask import Flask
from data import db_session

from data.users import User


db_session.global_init("db/blogs.db")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    add_user()
    #app.run()

def add_user():
    user = User()
    user.name = "Пользователь 2"
    user.about = "биография пользователя 2"
    user.email = "email2@email.ru"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = db_sess.query(User).first()
    print(user.name)

if __name__ == '__main__':
    main()


