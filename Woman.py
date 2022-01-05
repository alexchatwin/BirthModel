from datetime import datetime, timedelta


import datetime
from random import seed, random, gauss, randint


class Woman:
    ageYears: int
    ageDays: int
    pregnant: bool
    conceptionDt: datetime
    dueDt: datetime
    termWeeks: int
    termDays: int
    formerPregnancies=[]
    
    def __init__(self, _age):
        
        self.ageYears=_age
        self.ageDays=0
        
    def runDay(self, _date):
        
        
        if (self.pregnant==False):
            self.pregnant=chanceOfGettingPregnant(self.ageYears)
            if self.pregnant:
                self.termWeeks=0
                self.termDays=0
                self.conceptionDt=_date
                self.dueDt=_date+timedelta(days=280)
                
        else:
            self.termDays+=1
            if self.termDays>=7:
                self.termWeeks+=1
                self.termDays=0
            if chanceOfMiscarriage(self.ageYears, self.termWeeks):
                self.pregnant=False
                self.formerPregnancies.append("Miscarriage")
            if chanceOfTermination(self.ageYears, self.termWeeks):
                self.pregnant=False
                self.formerPregnancies.append("Termination")
            
        if self.pregnant:
            inLabour=chanceOfLabour(self.ageYears, self.termWeeks)
            if inLabour:
                firstLatentStageStDT, firstActiveStageStDT, secondStageStDT, thirsStageStDT=labourStageCalcs(self.ageYears, self.termWeeks, _date)
            
            
            
            


def chanceOfGettingPregnant(_age):
    rnd=random()
    prob=73/(1000*365)
    if rnd<prob:
        return True
    else:
        return False
    
def chanceOfMiscarriage(_ageYears, _termWeeks):
    rnd=random()
    if _termWeeks<=12:
        prob=(0.2/12) #1 in 4 chance, 80% weighted to first 12 weeks
    if _termWeeks>12 and _termWeeks<=20:
        prob=(0.5/8) #1 in 4 chance, 80% weighted to first 12 weeks
    if rnd<prob:
            return True
    else:
        return False
    
def chanceOfTermination(_ageYears, _termWeeks):
    rnd=random()
    if _termWeeks<26:
        prob=(.25/26)
    if rnd<prob:
        return True
    else:
        return False

def chanceOfLabour(_ageYears, _termWeeks):
    rnd=random()
    if _termWeeks < 30: prob=0
    elif _termWeeks < 31: prob=(.2/700)
    elif _termWeeks < 32: prob=(.3/700)
    elif _termWeeks < 33: prob=(.5/700)
    elif _termWeeks < 34: prob=(1/700)
    elif _termWeeks < 35: prob=(1.5/700)
    elif _termWeeks < 36: prob=(3/700)
    elif _termWeeks < 37: prob=(9/700)
    elif _termWeeks < 38: prob=(15/700)
    elif _termWeeks < 39: prob=(26/700)
    elif _termWeeks < 40: prob=(24/700)
    elif _termWeeks < 41: prob=(14/700)
    elif _termWeeks < 42: prob=(2/700)
    else: prob=1
    if rnd<prob:
        return True
    else:
        return False

def labourStageCalcs(_ageYears, _termWeeks, _date):
    offset=randint(0,23)
    lenFirstLatent=gauss(12,4) #assume mean 12h, SD 4
    lenFirstActive=gauss(6,2)
    lenSecond=gauss(1,0.5)
    lenThird=0.5
        