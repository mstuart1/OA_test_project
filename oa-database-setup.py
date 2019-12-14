import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class AISurv(Base):
    __tablename__ = 'aleutian_islands_surveys'
    LATITUDE = Column(Float)
    LONGITUDE = Column(Float)
    STATION = Column(String(20))
    STRATUM = Column(Integer, ForeignKey('aleutian_islands_strata.StratumCode'))
    YEAR = Column(String(4))
    DATETIME = Column(String(80))
    WTCPUE = Column(Float)
    NUMCPUE = Column(Float)
    COMMON = Column(String(250))
    SCIENTIFIC = Column(String(250))
    SID = Column(Integer, primary_key = True)
    BOT_DEPTH = Column(Float)
    BOT_TEMP = Column(Float)
    SURF_TEMP = Column(Float)
    VESSEL = Column(Integer, primary_key = True)
    CRUISE = Column(Integer, primary_key = True)
    HAUL = Column(Integer, primary_key = True)

    @property
    def serialize(self):
        return {
        'LATITUDE' : self.LATITUDE,
        'LONGITUDE' : self.LONGITUDE,
        'STATION' : self.STATION,
        'STRATUM' : self.STRATUM,
        'YEAR' : self.YEAR,
        'DATETIME' : self.DATETIME,
        'WTCPUE' : self.WTCPUE,
        'NUMCPUE' : self.NUMCPUE,
        'COMMON' : self.COMMON,
        'SCIENTIFIC' : self.SCIENTIFIC,
        'SID' : self.SID,
        'BOT_DEPTH' : self.BOT_DEPTH,
        'BOT_TEMP' : self.BOT_TEMP,
        'SURF_TEMP' : self.SURF_TEMP,
        'VESSEL' : self.VESSEL,
        'CRUISE' : self.CRUISE,
        'HAUL' : self.HAUL,
        }
    

class AIStrat(Base):
    __tablename__ = 'aleutian_islands_strata'
    NPFMCArea = Column(String(250))
    SubareaDescription = Column(String(250))
    StratumCode = Column(Integer, primary_key = True)
    DepthIntervalm = Column(String(250))
    Areakm2 = Column(Integer)

    @property
    def serialize(self):
        return{
            'NPFMCArea' : self.NPFMCArea
            'SubareaDescription' : self.SubareaDescription
            'StratumCode' : self.StratumCode
            'DepthIntervalm' : self.DepthIntervalm
            'Areakm2' : self.Areakm2
        }



engine = create_engine('sqlite:///oceanadapt.db')

Base.metadata.create_all(engine)

