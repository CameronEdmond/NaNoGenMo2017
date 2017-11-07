import sys
import pip
import re
import struct
import pprint
import random

#Counting citizens
count = 0
applicantno = 0
NewAttr = False
Problem = False
FlipCoin = False

#Setting up names
FirstNames = ["John", "Moira", "Leonardo", "Dodger", "Skunk", "Cho", "Doug", "Chuhong", "Sally", "Aya", "Layla",
              "Freya"]
LastNames = [" McTaggart ", " Booker ", " Cooper ", " Ting ", " De Leon ", " Molloy ", " Evans "]

#Setting up details
randheight = ["is tall", "is short", "is of medium height"]
randweight = ["is fat", "is skinny", "is muscular"]
randeyes = ["has two eyes", "has no eyes", "has one eye", "has a third eye"]
randeyecolour = ["has blue eyes", "has red eyes", "has green eyes", "has yellow eyes", "has brown eyes", "has grey eyes"]
randnipples = ["has one nipple", "has two nipples", "has three nipples", "has cat nipples", "is udderly inundated with nupples"]
minfunds = 0
maxfunds = 5000
FundsReq = 0

#Blank Citizen class
class Citizen:
    name = ""
    applicantno
    def __init__(self, height, weight, eyes, eyecolour, nipples):
        self.height = height
        self.weight = weight
        self.eyes = eyes
        self.eyecolour = eyecolour
        self.nipples = nipples

PerfectCitizen = Citizen ('default','default','default','default','default')



#Generating applicants until 5 citizens are found. Find a cleaner way to do this.
while count < 50:
    NewAttr = False
    Problem = False
    Applicant = Citizen(random.choice(randheight),random.choice(randweight),random.choice(randeyes),
                        random.choice(randeyecolour),random.choice(randnipples))
    Applicant.name = random.choice(FirstNames) + random.choice(LastNames)
    Applicant.funds = random.randrange(minfunds,maxfunds)


    print ("==================================================================================\n"
           "Applicant no." + str(applicantno) + ", " + Applicant.name + "is applying for citizenship.\n"
           + Applicant.name + Applicant.height + "\n" + Applicant.name + Applicant.weight + "\n"
           + Applicant.name + Applicant.eyes+ "\n" + Applicant.name + Applicant.eyecolour+ "\n"
           + Applicant.name + Applicant.nipples + "\n"
           + Applicant.name + "has " + str(Applicant.funds) + " to contribute to the nation's development fund. \n"
           + "==================================================================================")

    #Evaluate the applicant.
    for attr, value in PerfectCitizen.__dict__.items():
        if value is not "default":
            if Applicant.__getattribute__(attr) is not value:
                if Applicant.funds < FundsReq:
                    Problem = True
                else:
                    PerfectCitizen.__setattr__(attr, Applicant.__getattribute__(attr))

    #Are they in or out?
    if Problem == False:
        print(Applicant.name + "has been accepted for citizenship.")
        if Applicant.funds > FundsReq:
            FundsReq = Applicant.funds

        #Indoctrination
        for attr, value in PerfectCitizen.__dict__.items():
            if value is "default":
                if NewAttr == False:
                    FlipCoin = random.choice([True,False])
                    if FlipCoin == True:
                        PerfectCitizen.__setattr__(attr,Applicant.__getattribute__(attr))
                        NewAttr = True
        count += 1
    if Problem == True:
        print(Applicant.name + "is not suitable for citizenship.")
    applicantno += 1
    print ("==================================================================================\n"
           + "REMEMBER, THE PERFECT CITIZEN:\n" + str(PerfectCitizen.__dict__.values()) + "\n"
           + "There are currently " + str(count) + " citizens in our beautiful nation.\n"
           +"==================================================================================\n\n\n")
