from main import engine,Team,Hero_T
from sqlmodel import Session,select

def create_hero():
    with Session(engine) as session:
        avengers_team = Team(name="Avengers",headquarters="NYC")
        spider_team = Team(name="Spider",headquarters="Chicago")
        session.add(avengers_team)
        session.add(spider_team)
        session.commit()


        doctor_st = Hero_T(name="Doctor Strange",secret_name="Dr_st",team_id=avengers_team.id)
        black_sp = Hero_T(name="Black Spider",secret_name="b_sp",team_id=spider_team.id)
        hulk = Hero_T(name="Green Hulk",secret_name="hk",team_id=avengers_team.id)
        batman = Hero_T(name="Batman",secret_name="bt",team_id=spider_team.id)

        session.add(doctor_st)
        session.add(black_sp)
        session.add(hulk)
        session.add(batman)
        session.commit()

        session.refresh(doctor_st)
        session.refresh(black_sp)
        session.refresh(hulk)
        session.refresh(batman)

        print("Doctor Strange Hero",doctor_st)
        print("Black Spider Hero",black_sp)
        print("Hulk Hero",hulk)
        print("Batman Hero",batman)


def read_hero_teams():
    with Session(engine) as session:
        statement = select(Hero_T,Team).where(Hero_T.team_id == Team.id)

        result = session.exec(statement).all()
        for res in result:
            print("Final Result",res)


def update_hero():
    with Session(engine) as session:
        statement = select(Hero_T).where(Hero_T.name == "Batman")
        result = session.exec(statement).one()

        result.team_id = 1 # updating spider_team with team_avengers
        session.add(result)
        session.commit()



def delete_team_connection():
    with Session(engine) as session:
        statement = select(Hero_T).where(Hero_T.name == "Green Hulk")
        hulk = session.exec(statement).one()

        hulk.team_id = None
        session.add(hulk)
        session.commit()

        session.refresh(hulk)
        print("No team assoscialted with hulk",hulk)




if __name__ == "__main__":
    # create_hero()
    # read_hero_teams()
    # update_hero()
    delete_team_connection()
