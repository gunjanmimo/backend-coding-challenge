import json
from tqdm import tqdm
from datetime import datetime
#------------------LOCAL IMPORTS------------------#
from database import session,Base,engine
from database.models.planner_model import Planner


file = open("./planning.json")
json_data = json.load(file)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("--------------------INSERTING SAMPLE RECORDS--------------------")
    planner_objects = []
    for data in tqdm(json_data):
        data['startDate'] = datetime.strptime(data["startDate"], "%m/%d/%Y %I:%M %p")
        data['endDate']   = datetime.strptime(data["endDate"], "%m/%d/%Y %I:%M %p")
        planner_objects.append(
            Planner(**data)
        )
    session.bulk_save_objects(planner_objects)
    session.commit()
