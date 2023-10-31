import datetime
import re
import pandas as pd

def InputCleaner(string):
  inputtext=string
  CleanText =re.sub("[^0-9]"," ",inputtext)
  NumList= CleanText.split()
  NumList = list(map(int, NumList))
  #print(NumList)
  Date = datetime.datetime(NumList[0], NumList[1],NumList[2], hour=NumList[3], minute=NumList[4], second=NumList[5], microsecond=NumList[6]*1000)
  return Date

def DeltaTimeFinder(list, list2):
  Column11 = []
  for i in range(len(list)):
    #print(list2[i])
    if list2[i]!="nan":
      DeltaTime = InputCleaner(list2[i]) - InputCleaner(list[i])
      #print(DeltaTime)
      #print(i)
      Column11.append(DeltaTime)
    else:
      Column11.append("Not Completed Yet.")
  return(Column11)

data= pd.read_csv("Data CRM.csv")

ticketOpen= data.iloc[:, 9].astype(str).tolist()
ticketClose= data.iloc[:, 10].astype(str).tolist()

TimeTakenData = DeltaTimeFinder(ticketOpen, ticketClose)  
data['TimeTaken'] = TimeTakenData

OutputFile = 'output.csv'
data.to_csv(OutputFile, index=False)

averageTime = {}
updatedData=pd.read_csv("output.csv")
uncompletedTickets = 0

for i in range(len(updatedData)):
  if updatedData.iat[i,11]=="Not Completed Yet." :
    uncompletedTickets+=1
  elif averageTime.get(updatedData.iat[i,3])!=None :
    print(i)
    averageTime.update({updatedData.iat[i,3]:TimeTakenData[i]+ averageTime[updatedData.iat[i,3]]}) 
    averageTime.update({f"{updatedData.iat[i,3]} Amount" : averageTime[f"{updatedData.iat[i,3]} Amount"]+1})
  else:
    averageTime.update({updatedData.iat[i,3]:TimeTakenData[i]}) 
    averageTime.update({f"{updatedData.iat[i,3]} Amount" :1})

uniqueProblems= set(data.iloc[:, 3].astype(str).tolist())

SortedTimeDeltas = {}
for i in uniqueProblems:
   AverageSeconds = averageTime.get(i).total_seconds() / averageTime.get(f"{i} Amount")
   SortedTimeDeltas.update({i:AverageSeconds})

# Sort key
def value_getter(item):
    return item[1]

SortedTimeDeltas = sorted(SortedTimeDeltas.items(), key=value_getter)
print(SortedTimeDeltas)

