from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

strDB='postgresql+psycopg2://postgres:gszh8899@127.0.0.1:5432/wisdomMarket'\
      # 'jdbc:postgresql://{host}[:{port}]/[{database}]'
eng=create_engine(strDB,echo=True,client_encoding='utf8')

DB_session=sessionmaker(bind=eng)
session=DB_session()
data=session.execute("select * from auth_user ")
for row in data:
    for col in row:
        print(col)

    print()
session.close()