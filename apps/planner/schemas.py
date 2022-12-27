from pydantic import BaseModel

class PlannerPayload(BaseModel):
    page_no               : int             =  0
    page_limit            : int             =  50
    sort_by               : list            =  ['id']
    sort_order            : str             =  "desc"
    filter_by             : dict            =  {}