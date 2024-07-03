# session is used to CRUD data inside table using orm by creating objects(instances), 
# whereas engine is used to create migrations, and perform only raw sql queries
from sqlmodel import Session,select
from main_engine import engine
from main_engine import Hero


# Creating data inside table
def create_data():
    hero1 = Hero(name="Jazib",secret_name="jz")
    hero2 = Hero(name="Hassan",secret_name="hs",age=21)
    hero3 = Hero(name="Qamber",secret_name="pl")

    with Session(engine) as session:
        session.add(hero1)
        session.add(hero2)
        session.add(hero3)
        session.commit()


def read_data():
    with Session(engine) as session:
        stmt = select(Hero)
        results = session.exec(stmt)
        # print("First result is: ",results.first())
        # print("All results are: ",results.all())
        for hero in results:
            print(hero)


def update_data():
    with Session(engine) as session:
        stmt = select(Hero).where(Hero.name == "Jazib")
        result = session.exec(stmt)

        # Single row update
        # hero = result.one()
        # hero.secret_name = "CR"
        # session.add(hero)
        # print("Before updated",hero)
        # session.refresh(hero)
        # print("after updated",hero)

        # Mulitple rows update
        for hero in result:
            hero.secret_name = "CR"
            session.add(hero)
        session.commit()



def delete_data():
    with Session(engine) as session:
        stmt = select(Hero).where(Hero.name == "Hassan")
        results = session.exec(stmt)
        single = results.first() # for one row
        session.delete(single)

        # for res in results: # for two rows
        #     single = session.delete(res)

        session.commit()



if __name__ == "__main__":
    # create_data()
    read_data()
    # update_data()
    # delete_data()