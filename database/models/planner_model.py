#------------------PYTHON IMPORTS-----------------#
import uuid
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Integer, Text,Float,JSON

#------------------LOCAL IMPORTS-----------------#
from database import Base

class Planner(Base):
    __tablename__ = "planner"
    id                = Column("id",Integer, primary_key=True)
    originalId        = Column("originalId",String, default=uuid.uuid4, unique=True, nullable=False)
    talentId          = Column("talentId",String, nullable=True)
    talentName        = Column("talentName",String, nullable=True)
    talentGrade       = Column("talentGrade",String, nullable=True)
    bookingGrade      = Column("bookingGrade",String, nullable=True)
    operatingUnit     = Column("operatingUnit",String, nullable=False)
    officeCity        = Column("officeCity",String, nullable=True)
    officePostalCode  = Column("officePostalCode",String, nullable=False)
    jobManagerName    = Column("jobManagerName",String, nullable=True)
    jobManagerId      = Column("jobManagerId",String, nullable=True)
    totalHours        = Column("totalHours",Float, nullable=False)
    startDate         = Column("startDate",DateTime(timezone=True), server_default=func.now(), nullable=False)
    endDate           = Column("endDate",DateTime(timezone=True), server_default=func.now(), nullable=False)
    clientName        = Column("clientName", String, nullable=True)
    clientId          = Column("clientId",String, nullable=False)
    industry          = Column("industry",String, nullable=True)
    requiredSkills    = Column("requiredSkills",JSON, nullable=True)
    optionalSkills    = Column("optionalSkills",JSON, nullable=True)
    isUnassigned      = Column("isUnassigned",Boolean)
    
    
