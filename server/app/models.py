import datetime

from sqlalchemy import BigInteger, Column, Date, DateTime, Enum, ForeignKey, Index, Boolean
from sqlalchemy import Float, Integer, Numeric, SmallInteger, String, Table, Text, Time
from sqlalchemy import desc, distinct, text, func

from sqlalchemy.orm import relationship, backref, column_property

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata

db = None



class CensusOriginDestinationEmployment(Base):
    __tablename__ = 'census_origin_destination_employment'

    id = Column(Integer, primary_key=True)
    w_geocode = Column(String(15), nullable=False)
    h_geocode = Column(String(15), nullable=False)
    S000 = Column(Integer, nullable=False)
    SA01 = Column(Integer, nullable=False)
    SA02 = Column(Integer, nullable=False)
    SA03 = Column(Integer, nullable=False)
    SE01 = Column(Integer, nullable=False)
    SE02 = Column(Integer, nullable=False)
    SE03 = Column(Integer, nullable=False)
    SI01 = Column(Integer, nullable=False)
    SI02 = Column(Integer, nullable=False)
    SI03 = Column(Integer, nullable=False)
    createdate = Column(String(8), nullable=False)




class CensusTractNonResidentWorker(Base):
    __tablename__ = 'census_tract_non_resident_workers'

    id = Column(Integer, primary_key=True)
    geocode_tract = Column(String(11), nullable=False, index=True)
    workers_in = Column(Integer, nullable=False)
    workers_out = Column(Integer, nullable=False)
    workers_diff = Column(Integer, nullable=False)


