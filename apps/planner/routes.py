from fastapi import APIRouter, Depends

# -------------------------------- sqlalchemy imports ---------------------------
from sqlalchemy import desc, asc, or_

from sqlalchemy.orm import Session

# ----------------------------local imports----------------------------#
from database import session, Base, get_db
from database.models.planner_model import Planner
from apps.planner.schemas import PlannerPayload

# from database.dbConnection import get_db

planner_routes = APIRouter(prefix="/planner", tags=["PLANNER"])


# TODO
"""
GET PLANNER API WHICH WILL DO FOLLOWING THINGS
    1. PAGINATION
    2. FILTERING 
    3. SORTING
    
    
# ? PAGINATION: TOTAL 5000 RECORDS AND 50 RECORDS ON EACH PAGE, SO PAGE NO RANGE 1-100
# ? SORTING: SUPPORTED FOLLOWING COLUMNS FOR SORTING. 
    1. talentName
    2. officeCity
    3. jobManagerName
    4. totalHours
    5. startDate
    6. endDate
    7. clientName
    
    
    // AT THE END
        no_requiredSkills,
        no_optionalSkills
    
    #* NOTE: SUPPORT SORTING BY MULTIPLE COLUMNS
# ? FILTERING: SUPPORTED FOLLOWING COLUMNS FOR FILTERING

    1. originalId
    2. talentId
    3. talentName
    4. talentGrade
    5. bookingGrade
    6. operatingUnit
    7. officeCity
    8. officePostalCode
    9. jobManagerName
    10. jobManagerId
    11. clientName
    12. clientId
    13. industry
    14. isUnassigned
    // AT THE END 
        1. FILTER BY TOTAL HOUR RANGE
        2. FILTER BY START DATE RANGE
        3. FILTER BY END DATE RANGE
        4. FILTER BY SKILL NAMES        
    
"""


@planner_routes.get("/get_planners")
async def get_planners(payload: PlannerPayload, db: Session = Depends(get_db)):

    payload = payload.__dict__
    page_no = payload["page_no"]
    page_limit = payload["page_limit"]
    sort_by = payload["sort_by"]
    sort_order = payload["sort_order"]
    filter_by = payload["filter_by"]

    # query
    query = session.query(Planner)

    # 1ST. FILTER
    for key, val in filter_by.items():
        if key in ["totalHours"]:
            filter_string = f"Planner.{key}.between({val[0]}, {val[1]})"
            query = query.filter(eval(filter_string))
        elif key in ["startDate", "endDate"]:
            filter_string = f"Planner.{key}.between('{val[0]}', '{val[1]}')"
            query = query.filter(eval(filter_string))
        elif key == "skills":

            query = query.filter(
                or_(
                    Planner.requiredSkills.contains(val),
                    Planner.optionalSkills.contains(val),
                )
            )
        else:
            query = query.filter(eval(f"Planner.{key}.in_({val})"))
    # 2ND SORT & PAGINATE
    offset = page_no * page_limit
    if sort_order == "asc":
        query = query.order_by(asc(", ".join(sort_by))).offset(offset).limit(page_limit)
    else:
        query = (
            query.order_by(desc(", ".join(sort_by))).offset(offset).limit(page_limit)
        )

    return {
        "status": "success",
        "message": "go ahead",
        "page_no": page_no,
        "data": query.all(),
    }
