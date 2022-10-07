# 10 items or fewer express checkout lane: Daniel Liu, Anthony Sun, Jasmine Yuen
# SoftDev
# 2022-10-06

import csv
import random

# initializing dictionary + keys

def generate_dict(filename):
    jobDict = {}
    jobDict["Job Class"] = []
    jobDict["Percentage"] = []
    with open(filename) as f:
        r =  csv.DictReader(f)
        for row in r:
            # making sure the total percentage is not accounted for
            if (row['Job Class']!="Total"):
                jobDict["Job Class"].append(row['Job Class'])
                # making sure the percentage is a float, not a string
                jobDict["Percentage"].append(float(row['Percentage']))
    return jobDict

def get_all_occupations(jobDict):
    temp = list(jobDict["Job Class"])
    str = "<ul>"
    for x in temp:
        str += "<li>" + x + "</li>"
    return str + "</ul>"

def give_weighted_job(jobDict):
    temp = random.choices(jobDict["Job Class"], jobDict["Percentage"])
    stringV = str(temp).strip("[").strip("]").strip("'")
    return stringV

### TESTING RANGE OF ERROR

if __name__ == "__main__":
    ary = []
    times = 1000
    for num in range(times):
        ary+=(random.choices(jobDict["Job Class"], jobDict["Percentage"]))

    for i in range(len(jobDict['Job Class'])):
        job = jobDict['Job Class'][i]
        apercent = jobDict['Percentage'][i]
        cpercent = (ary.count(job)/times)*100
        print(job + ": " + str(cpercent) + "%")
        print("ACTUAL: " + str(apercent) + "% " + "DIFFERENCE: " + str(apercent-cpercent) + "\n")