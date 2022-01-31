import datetime

from app.database import Base, engine, session

from app.models import Status, User, Event

import random

from faker import Faker


def create_status_data():
    list_statuses = ['ativo', 'em andamento', 'concluido', 'exluido', 'pausado', ]

    for status in list_statuses:
        new_status = Status(name=status, active=True)

        session.add(new_status)

    session.commit()


def create_users_data(qtd_users):
    faker = Faker()

    for _ in range(qtd_users):
        name = faker.name()

        new_user = User(name=name, active=True)

        session.add(new_user)

    session.commit()


def create_events_data(qtd_events, description_instance, title_intance='event'):
    count_users = session.query(User).count()

    count_status = session.query(Status).count()

    for num_event in range(qtd_events):
        instance_autor = session.query(User).get(random.randint(1, count_users))

        instance_status = session.query(Status).get(random.randint(1, count_status))

        new_event = Event(
            title=f'{title_intance} {num_event}',
            description=f'{description_instance}',
            author_id=instance_autor.id,
            status_id=instance_status.id,
            active=True,
            date_created=datetime.datetime.now(),
            date_event=datetime.datetime.now())

        session.add(new_event)

        session.commit()

        for i in range(1, 5):
            user = session.query(User).filter(User.id == i).one()
            new_event.participants.append(user)

        print(new_event.participants)

        session.commit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    create_status_data()
    create_users_data(5)
    create_events_data(10, 'new description')
    for instance in session.query(Event):
        print(instance.title)
