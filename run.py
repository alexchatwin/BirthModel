import pandas as pd
from Woman import Woman 

ageBreakdownDf=pd.read_csv("./data/ageBreakdown.csv")
totalFemalePop=ageBreakdownDf[ageBreakdownDf["Age"]=="All Ages"]["Count"].values[0]
print(ageBreakdownDf)

populationSize = 100

populationList=[]

for i in range(populationSize):
    populationList.append(Woman())
