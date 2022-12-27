from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker  



Base = declarative_base()

# SQL DATABASE ENGINE INITIALIZATION
engine = create_engine("sqlite:///planner.db",echo=False,connect_args={'check_same_thread': False})
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session =  Session()





def get_db():
    db: Session = session
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
    finally:
        db.close()