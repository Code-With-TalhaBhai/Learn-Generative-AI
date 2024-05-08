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

        session.add(doctor_st)
        session.add(black_sp)
        session.add(hulk)
        session.commit()

        session.refresh(doctor_st)
        session.refresh(black_sp)
        session.refresh(hulk)

        print("Doctor Strange Hero",doctor_st)
        print("Black Spider Hero",black_sp)
        print("Hulk Hero",hulk)


def read_hero_teams():
    with Session(engine) as session:
        # team = session.exec(select(Team).where(Team.id == 2))
        # hero = session.exec(select(Hero_T).where(Hero_T.id == 2))

        statement = select(Hero_T,Team).where(Hero_T.team_id == Team.id)
        # statement1 = select(team,hero).where(team.id == hero.id)
        # statement2 = select(hero,team).where(hero.id == team.id)

        result = session.exec(statement).all()
        # result1 = session.exec(statement1).all()
        # result2 = session.exec(statement2).all()

        # for res1 in result1:
            # print("Left Table Team: ",res1)

        # for res2 in result2:
            # print("Left Table Hero: ",res2)

        for res in result:
            print("Final Result",res)





if __name__ == "__main__":
    # create_hero()
    read_hero_teams()
