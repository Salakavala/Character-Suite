from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

def IterSum(source):
    #Modified version of the Sum() function that allows the setting of an ending point.
    #Currently set at 3, but may change to include argument of 'end' if needed for additional purposes.
    x = 0
    y = 0
    for i in source:
        if x != 3:
            y += i
            x +=1
        else:
            break
    return y
#Create character class, which is used for storing character information. For now, this is mostly for saving/loading
#from text files, but will eventually be passed to more interactive windows.
class Character(object):
    def __init__(self, filename, details, exp, traits, skills, abilities):
        self.filename = filename
        self.details = details
        self.exp = exp
        self.traits = traits
        self.skills = skills
        self.abilities = abilities

    def New(self):
        #Establish default python variable values for iteration/sanity purposes.
        self.filename = ""
        self.details = ["", "", "", "", "", "", ""]
        self.exp = [1, 0, 0, 15, -5, 0, 0, 0]
        self.traits = {
            "dex": [0, 0, 0, 0],
            "end": [0, 0, 0, 0],
            "per": [0, 0, 0, 0],
            "str": [0, 0, 0, 0],
            "con": [0, 0, 0, 0],
            "int": [0, 0, 0, 0],
            "rat": [0, 0, 0, 0],
            "res": [0, 0, 0, 0],
            "dip": [0, 0, 0, 0],
            "gui": [0, 0, 0, 0],
            "itd": [0, 0, 0, 0],
            "lea": [0, 0, 0, 0]
        }
        self.skills = {
            "aca": [0, 0, 0, 0],
            "cod": [0, 0, 0, 0],
            "com": [0, 0, 0, 0],
            "eng": [0, 0, 0, 0],
            "mec": [0, 0, 0, 0],
            "med": [0, 0, 0, 0],
            "met": [0, 0, 0, 0],
            "pil": [0, 0, 0, 0],
            "ste": [0, 0, 0, 0]
        }
        self.abilities = {}

    def LevelAdjust(self):
        #Get Character level and extrapolate reliant values.
        if self.exp[1] == self.exp[2]:
            self.exp[0] += 1
        else:
            pass
        self.exp[2] = 10 + ((self.exp[0] -2) * 5)
        self.exp[3] = 15 + (5 * (self.exp[0] - 1))
        self.exp[5] = 3 + ((self.traits["int"][3] / 3) * self.exp[0])
        self.exp[6] = 2 + (self.exp[0] / 2)
        self.exp[7] = self.exp[0] / 5

    def Save(self):
        #Duh. Writes variables to text file on separate lines.
        with open(self.filename+".txt" , "w") as File:
            File.write(self.filename + "\n")
            File.write(str(self.details) + "\n")
            File.write(str(self.exp) + "\n")
            File.write(str(self.traits) + "\n")
            File.write(str(self.skills) + "\n")
            File.write(str(self.abilities) + "\n")

    def SaveAs(self):
        #Also duh.
        self.filename = simpledialog.askstring("Save New Character", "Enter the desired filename below.")
        self.Save()

    def Load(self):
        #Extract variables from file as strings, translate to lists/dicts with eval as necessary.
        #Override current values, then push to interface with Update. Saving and loading works perfectly,
        #however, Update() is failing me right now.
        with open(simpledialog.askstring("Load Character", "Enter Character Name Below")+".txt", "r") as File:
            self.filename = File.readline().rstrip("\n")
            self.details = eval(File.readline().rstrip("\n"))
            self.exp = eval(File.readline().rstrip("\n"))
            self.traits = eval(File.readline().rstrip("\n"))
            self.skills = eval(File.readline().rstrip("\n"))
            self.abilities = eval(File.readline().rstrip("\n"))
            my_gui.Update()
        print(self.filename)
        print(self.details)
        print(type(self.details))
        print(self.exp)
        print(type(self.exp))
        print(self.traits)
        print(type(self.traits))
        print(self.skills)
        print(type(self.skills))
        print(self.abilities)
        #Print is for debugging/verification purposes. Will be removed once the entire process is known to work.

#Establish character object. Additional instances not necessary as
#long term storage for values is on external file.
CurrentChar = Character("",[],[],{},{},{})
CurrentChar.New()
print(CurrentChar)

class MainGui:
    #Clusterfuck of a Gui. Really might need to look 
    #into learning how to clean this up and make the code more compact.
    def __init__(self, master):
        self.master = master
        self.master.title("Fallen Legacy Character Suite")
        
        #Declare all tkinter variables.
        cName = StringVar()
        cName.set("")
        cRace = StringVar()
        cRace.set("")
        cSubRace = StringVar()
        cSubRace.set("")
        cAge = StringVar()
        cGender = StringVar()
        cHeight = StringVar()
        cWeight = StringVar()
        cLuck = IntVar()
        cLevel = IntVar()
        cLevel.set(1)
        cExp = IntVar()
        cGoal = IntVar()
        tPnts = IntVar()
        sPnts = IntVar()
        pPnts = IntVar()
        cDex = IntVar()
        bDex = IntVar()
        pDex = IntVar()
        tDex = IntVar()
        cEnd = IntVar()
        bEnd = IntVar()
        pEnd = IntVar()
        tEnd = IntVar()
        cPer = IntVar()
        bPer = IntVar()
        pPer = IntVar()
        tPer = IntVar()
        cStr = IntVar()
        bStr = IntVar()
        pStr = IntVar()
        tStr = IntVar()
        cCon = IntVar()
        bCon = IntVar()
        pCon = IntVar()
        tCon = IntVar()
        cInt = IntVar()
        bInt = IntVar()
        pInt = IntVar()
        tInt = IntVar()
        cRat = IntVar()
        bRat = IntVar()
        pRat = IntVar()
        tRat = IntVar()
        cRes = IntVar()
        bRes = IntVar()
        pRes = IntVar()
        tRes = IntVar()
        cDip = IntVar()
        bDip = IntVar()
        pDip = IntVar()
        tDip = IntVar()
        cGui = IntVar()
        bGui = IntVar()
        pGui = IntVar()
        tGui = IntVar()
        cItd = IntVar()
        bItd = IntVar()
        pItd = IntVar()
        tItd = IntVar()
        cLea = IntVar()
        bLea = IntVar()
        pLea = IntVar()
        tLea = IntVar()
        cAca = IntVar()
        bAca = IntVar()
        pAca = IntVar()
        tAca = IntVar()
        cCod = IntVar()
        bCod = IntVar()
        pCod = IntVar()
        tCod = IntVar()
        cCom = IntVar()
        bCom = IntVar()
        pCom = IntVar()
        tCom = IntVar()
        cEng = IntVar()
        bEng = IntVar()
        pEng = IntVar()
        tEng = IntVar()
        cMec = IntVar()
        bMec = IntVar()
        pMec = IntVar()
        tMec = IntVar()
        cMed = IntVar()
        bMed = IntVar()
        pMed = IntVar()
        tMed = IntVar()
        cMet = IntVar()
        bMet = IntVar()
        pMet = IntVar()
        tMet = IntVar()
        cPil = IntVar()
        bPil = IntVar()
        pPil = IntVar()
        tPil = IntVar()
        cSte = IntVar()
        bSte = IntVar()
        pSte = IntVar()
        tSte = IntVar()

        #Begin Gui
        mFrame = Frame(master)
        mFrame.grid()

        self.New = Button(mFrame, text="New", command=CurrentChar.New)
        self.New.grid(row=0, column=0)

        self.Load = Button(mFrame, text="Load", command=CurrentChar.Load)
        self.Load.grid(row=0, column=1)

        self.Save = Button(mFrame, text="Save", command=CurrentChar.Save)
        self.Save.grid(row=0, column=2)

        self.Save = Button(mFrame, text="SaveAs", command=CurrentChar.SaveAs)
        self.Save.grid(row=0, column=3)
                
        dFrame = LabelFrame(mFrame, text="Character Details")
        dFrame.grid(pady=5)

        self.nLabel = Label(dFrame, text="Name:")
        self.nLabel.grid(row=1, column=1)

        self.nEntry = Entry(dFrame, textvariable=cName)
        self.nEntry.grid(row=1, column=2)

        self.rLabel = Label(dFrame, text="Race:")
        self.rLabel.grid(row=1, column=3)

        self.rSelect1 = OptionMenu(dFrame, cRace, "Fentoran", "Ishgaran", "Lectikin", "Onak'tar", "Panssari", "Reth", "Sylvid", "Synthetic Intelligence", "Yallamiri")
        self.rSelect1.grid(row=1, column=4)

        self.rSelect2 = OptionMenu(dFrame, cSubRace, "Android", "Cyborg", "Fentoran", "Ishgaran", "Lectikin", "Panssari", "Reth", "Sylvid", "Yallamiri")
        self.rSelect2.grid(row=1, column=5)
        
        self.aLabel = Label(dFrame, text="Age:")
        self.aLabel.grid(row=1, column=6)

        self.aEntry = Entry(dFrame, width=3, textvariable=cAge)
        self.aEntry.grid(row=1, column=7)

        self.gLabel = Label(dFrame, text="Gender:")
        self.gLabel.grid(row=1, column=8)

        self.gEntry = Entry(dFrame, width=8, textvariable=cGender)
        self.gEntry.grid(row=1, column=9)

        self.hLabel = Label(dFrame, text="Height:")
        self.hLabel.grid(row=1, column=10)

        self.hEntry = Entry(dFrame, width=8, textvariable=cHeight)
        self.hEntry.grid(row=1, column=11)

        self.wLabel = Label(dFrame, text="Weight:")
        self.wLabel.grid(row=1, column=12)

        self.wEntry = Entry(dFrame, width=8, textvariable=cWeight)
        self.wEntry.grid(row=1, column=13)

        xpFrame = LabelFrame(mFrame, text="Exp")
        xpFrame.grid(pady=5)

        self.rLabel = Label(xpFrame, text="Level:")
        self.rLabel.grid(row=2, column=0)

        self.lvlSelect = OptionMenu(xpFrame, cLevel, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
        self.lvlSelect.grid(row=2, column=1)

        self.expLabel = Label(xpFrame, text="Experience:")
        self.expLabel.grid(row=2, column=2)

        self.xpEntry = Entry(xpFrame, width=8, textvariable=cExp)
        self.xpEntry.grid(row=2, column=3)

        self.xpLabel = Label(xpFrame, text="/")
        self.xpLabel.grid(row=2, column=4)

        self.goalEntry = Label(xpFrame, width=8, textvariable=cGoal)
        self.goalEntry.grid(row=2, column=5)
        
        tFrame = LabelFrame(mFrame, text="Traits")
        tFrame.grid(pady=5)

        self.rPhysLabel = Label(tFrame, text="Rank")
        self.rPhysLabel.grid(row=4, column=1)

        self.bPhysLabel = Label(tFrame, text="Bonus")
        self.bPhysLabel.grid(row=4, column=2)

        self.pPhysLabel = Label(tFrame, text="Penalty")
        self.pPhysLabel.grid(row=4, column=3)

        self.tPhysLabel = Label(tFrame, text="Total")
        self.tPhysLabel.grid(row=4, column=4)

        self.cDexLabel = Label(tFrame, text="DEX:")
        self.cDexLabel.grid(row=5, column=0)

        self.cDexEntry = Entry(tFrame, width=3, textvariable=cDex)
        self.cDexEntry.grid(row=5, column=1)

        self.bDexEntry = Entry(tFrame, width=3, textvariable=bDex)
        self.bDexEntry.grid(row=5, column=2)

        self.pDexEntry = Entry(tFrame, width=3, textvariable=pDex)
        self.pDexEntry.grid(row=5, column=3)

        self.tDexLabel = Label(tFrame, width=3, textvariable=tDex)
        self.tDexLabel.grid(row=5, column=4)

        self.cEndLabel = Label(tFrame, text="END:")
        self.cEndLabel.grid(row=6, column=0)

        self.cEndEntry = Entry(tFrame, width=3, textvariable=cEnd)
        self.cEndEntry.grid(row=6, column=1)

        self.bEndEntry = Entry(tFrame, width=3, textvariable=bEnd)
        self.bEndEntry.grid(row=6, column=2)

        self.pEndEntry = Entry(tFrame, width=3, textvariable=pEnd)
        self.pEndEntry.grid(row=6, column=3)

        self.tEndLabel = Label(tFrame, width=3, textvariable=tEnd)
        self.tEndLabel.grid(row=6, column=4)

        self.cPerLabel = Label(tFrame, text="PER:")
        self.cPerLabel.grid(row=7, column=0)

        self.cPerEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.cPerEntry.grid(row=7, column=1)

        self.bPerEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.bPerEntry.grid(row=7, column=2)

        self.pPerEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.pPerEntry.grid(row=7, column=3)

        self.tPerEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.tPerEntry.grid(row=7, column=4)

        self.cStrLabel = Label(tFrame, text="STR:")
        self.cStrLabel.grid(row=8, column=0)

        self.cStrEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.cStrEntry.grid(row=8, column=1)

        self.bStrEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.bStrEntry.grid(row=8, column=2)

        self.pStrEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.pStrEntry.grid(row=8, column=3)

        self.tStrEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.tStrEntry.grid(row=8, column=4)

        self.rMenLabel = Label(tFrame, text="Rank")
        self.rMenLabel.grid(row=4, column=6)

        self.bMenLabel = Label(tFrame, text="Bonus")
        self.bMenLabel.grid(row=4, column=7)

        self.pMenLabel = Label(tFrame, text="Penalty")
        self.pMenLabel.grid(row=4, column=8)

        self.tMenLabel = Label(tFrame, text="Total")
        self.tMenLabel.grid(row=4, column=9)

        self.cConLabel = Label(tFrame, text="CON:")
        self.cConLabel.grid(row=5, column=5)

        self.cConEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.cConEntry.grid(row=5, column=6)

        self.bConEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.bConEntry.grid(row=5, column=7)

        self.pConEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.pConEntry.grid(row=5, column=8)

        self.tConEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.tConEntry.grid(row=5, column=9)

        self.cIntLabel = Label(tFrame, text="INT:")
        self.cIntLabel.grid(row=6, column=5)

        self.cIntEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.cIntEntry.grid(row=6, column=6)

        self.bIntEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.bIntEntry.grid(row=6, column=7)

        self.pIntEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.pIntEntry.grid(row=6, column=8)

        self.tIntEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.tIntEntry.grid(row=6, column=9)

        self.cRatLabel = Label(tFrame, text="RAT:")
        self.cRatLabel.grid(row=7, column=5)

        self.cRatEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.cRatEntry.grid(row=7, column=6)

        self.bRatEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.bRatEntry.grid(row=7, column=7)

        self.pRatEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.pRatEntry.grid(row=7, column=8)

        self.tRatEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.tRatEntry.grid(row=7, column=9)

        self.cResLabel = Label(tFrame, text="RES:")
        self.cResLabel.grid(row=8, column=5)

        self.cResEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.cResEntry.grid(row=8, column=6)

        self.bResEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.bResEntry.grid(row=8, column=7)

        self.pResEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.pResEntry.grid(row=8, column=8)

        self.tResEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.tResEntry.grid(row=8, column=9)

        self.rSocLabel = Label(tFrame, text="Rank")
        self.rSocLabel.grid(row=4, column=11)

        self.bSocLabel = Label(tFrame, text="Bonus")
        self.bSocLabel.grid(row=4, column=12)

        self.pSocLabel = Label(tFrame, text="Penalty")
        self.pSocLabel.grid(row=4, column=13)

        self.tSocLabel = Label(tFrame, text="Total")
        self.tSocLabel.grid(row=4, column=14)

        self.cDipLabel = Label(tFrame, text="DIP:")
        self.cDipLabel.grid(row=5, column=10)

        self.cDipEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.cDipEntry.grid(row=5, column=11)

        self.bDipEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.bDipEntry.grid(row=5, column=12)

        self.pDipEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.pDipEntry.grid(row=5, column=13)

        self.tDipEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.tDipEntry.grid(row=5, column=14)

        self.cGuiLabel = Label(tFrame, text="GUI:")
        self.cGuiLabel.grid(row=6, column=10)

        self.cGuiEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.cGuiEntry.grid(row=6, column=11)

        self.bGuiEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.bGuiEntry.grid(row=6, column=12)

        self.pGuiEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.pGuiEntry.grid(row=6, column=13)

        self.tGuiEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.tGuiEntry.grid(row=6, column=14)

        self.cItdLabel = Label(tFrame, text="ITD:")
        self.cItdLabel.grid(row=7, column=10)

        self.cItdEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.cItdEntry.grid(row=7, column=11)

        self.bItdEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.bItdEntry.grid(row=7, column=12)

        self.pItdEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.pItdEntry.grid(row=7, column=13)

        self.tItdEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.tItdEntry.grid(row=7, column=14)

        self.cLeaLabel = Label(tFrame, text="LEA:")
        self.cLeaLabel.grid(row=8, column=10)

        self.cLeaEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.cLeaEntry.grid(row=8, column=11)

        self.bLeaEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.bLeaEntry.grid(row=8, column=12)

        self.pLeaEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.pLeaEntry.grid(row=8, column=13)

        self.tLeaEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.tLeaEntry.grid(row=8, column=14)

        self.tLeaEntry = Entry(tFrame, width=3, textvariable=IntVar)
        self.tLeaEntry.grid(row=8, column=14)

        sFrame = LabelFrame(mFrame, text="Skills")
        sFrame.grid(pady=5)

        self.rSkillLabel = Label(sFrame, text="Rank")
        self.rSkillLabel.grid(row=10, column=1)

        self.bSkillLabel = Label(sFrame, text="Bonus")
        self.bSkillLabel.grid(row=10, column=2)

        self.pSkillLabel = Label(sFrame, text="Penalty")
        self.pSkillLabel.grid(row=10, column=3)

        self.tSkillLabel = Label(sFrame, text="Total")
        self.tSkillLabel.grid(row=10, column=4)

        self.cAcaLabel = Label(sFrame, text="ACA:")
        self.cAcaLabel.grid(row=11, column=0)

        self.cAcaEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.cAcaEntry.grid(row=11, column=1)

        self.bAcaEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.bAcaEntry.grid(row=11, column=2)

        self.pAcaEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.pAcaEntry.grid(row=11, column=3)

        self.tAcaEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.tAcaEntry.grid(row=11, column=4)

        self.cCodLabel = Label(sFrame, text="COD:")
        self.cCodLabel.grid(row=12, column=0)

        self.cCodEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.cCodEntry.grid(row=12, column=1)

        self.bCodEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.bCodEntry.grid(row=12, column=2)

        self.pCodEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.pCodEntry.grid(row=12, column=3)

        self.tCodEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.tCodEntry.grid(row=12, column=4)

        self.cComLabel = Label(sFrame, text="COM:")
        self.cComLabel.grid(row=13, column=0)

        self.cComEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.cComEntry.grid(row=13, column=1)

        self.bComEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.bComEntry.grid(row=13, column=2)

        self.pComEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.pComEntry.grid(row=13, column=3)

        self.tComEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.tComEntry.grid(row=13, column=4)

        self.rSkillLabel = Label(sFrame, text="Rank")
        self.rSkillLabel.grid(row=10, column=6)

        self.bSkillLabel = Label(sFrame, text="Bonus")
        self.bSkillLabel.grid(row=10, column=7)

        self.pSkillLabel = Label(sFrame, text="Penalty")
        self.pSkillLabel.grid(row=10, column=8)

        self.tSkillLabel = Label(sFrame, text="Total")
        self.tSkillLabel.grid(row=10, column=9)

        self.cEngLabel = Label(sFrame, text="ENG:")
        self.cEngLabel.grid(row=11, column=5)

        self.cEngEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.cEngEntry.grid(row=11, column=6)

        self.bEngEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.bEngEntry.grid(row=11, column=7)

        self.pEngEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.pEngEntry.grid(row=11, column=8)

        self.tEngEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.tEngEntry.grid(row=11, column=9)

        self.cMecLabel = Label(sFrame, text="MEC:")
        self.cMecLabel.grid(row=12, column=5)

        self.cMecEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.cMecEntry.grid(row=12, column=6)

        self.bMecEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.bMecEntry.grid(row=12, column=7)

        self.pMecEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.pMecEntry.grid(row=12, column=8)

        self.tMecEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.tMecEntry.grid(row=12, column=9)

        self.cMedLabel = Label(sFrame, text="MED:")
        self.cMedLabel.grid(row=13, column=5)

        self.cMedEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.cMedEntry.grid(row=13, column=6)

        self.bMedEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.bMedEntry.grid(row=13, column=7)

        self.pMedEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.pMedEntry.grid(row=13, column=8)

        self.tMedEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.tMedEntry.grid(row=13, column=9)

        self.rSkillLabel = Label(sFrame, text="Rank")
        self.rSkillLabel.grid(row=10, column=11)

        self.bSkillLabel = Label(sFrame, text="Bonus")
        self.bSkillLabel.grid(row=10, column=12)

        self.pSkillLabel = Label(sFrame, text="Penalty")
        self.pSkillLabel.grid(row=10, column=13)

        self.tSkillLabel = Label(sFrame, text="Total")
        self.tSkillLabel.grid(row=10, column=14)

        self.cMetLabel = Label(sFrame, text="MET:")
        self.cMetLabel.grid(row=11, column=10)

        self.cMetEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.cMetEntry.grid(row=11, column=11)

        self.bMetEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.bMetEntry.grid(row=11, column=12)

        self.pMetEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.pMetEntry.grid(row=11, column=13)

        self.tMetEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.tMetEntry.grid(row=11, column=14)

        self.cPilLabel = Label(sFrame, text="PIL:")
        self.cPilLabel.grid(row=12, column=10)

        self.cPilEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.cPilEntry.grid(row=12, column=11)

        self.bPilEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.bPilEntry.grid(row=12, column=12)

        self.pPilEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.pPilEntry.grid(row=12, column=13)

        self.tPilEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.tPilEntry.grid(row=12, column=14)

        self.cSteLabel = Label(sFrame, text="STE:")
        self.cSteLabel.grid(row=13, column=10)

        self.cSteEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.cSteEntry.grid(row=13, column=11)

        self.bSteEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.bSteEntry.grid(row=13, column=12)

        self.pSteEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.pSteEntry.grid(row=13, column=13)

        self.tSteEntry = Entry(sFrame, width=3, textvariable=IntVar)
        self.tSteEntry.grid(row=13, column=14)

        def Import(self):
            # Get tkinter variables, store in python variables, do math as necessary.
            CurrentChar.details[0] = cName.get()
            CurrentChar.details[1] = cRace.get()
            CurrentChar.details[2] = cSubRace.get()
            CurrentChar.details[3] = cAge.get()
            CurrentChar.details[4] = cHeight.get()
            CurrentChar.details[5] = cWeight.get()
            CurrentChar.details[6] = cLuck.get()
            CurrentChar.exp[0] = cLevel.get()
            CurrentChar.exp[1] = cExp.get()
            CurrentChar.traits["dex"][0] = cDex.get()
            CurrentChar.traits["dex"][1] = bDex.get()
            CurrentChar.traits["dex"][2] = pDex.get()
            CurrentChar.traits["dex"][3] = IterSum(CurrentChar.traits["dex"])
            CurrentChar.traits["end"][0] = cEnd.get()
            CurrentChar.traits["end"][1] = bEnd.get()
            CurrentChar.traits["end"][2] = pEnd.get()
            CurrentChar.traits["end"][3] = IterSum(CurrentChar.traits["end"])
            CurrentChar.traits["per"][0] = cPer.get()
            CurrentChar.traits["per"][1] = bPer.get()
            CurrentChar.traits["per"][2] = pPer.get()
            CurrentChar.traits["per"][3] = IterSum(CurrentChar.traits["per"])
            CurrentChar.traits["str"][0] = cStr.get()
            CurrentChar.traits["str"][1] = bStr.get()
            CurrentChar.traits["str"][2] = pStr.get()
            CurrentChar.traits["str"][3] = IterSum(CurrentChar.traits["str"])
            CurrentChar.traits["con"][0] = cCon.get()
            CurrentChar.traits["con"][1] = bCon.get()
            CurrentChar.traits["con"][2] = pCon.get()
            CurrentChar.traits["con"][3] = IterSum(CurrentChar.traits["con"])
            CurrentChar.traits["int"][0] = cInt.get()
            CurrentChar.traits["int"][1] = bInt.get()
            CurrentChar.traits["int"][2] = pInt.get()
            CurrentChar.traits["int"][3] = IterSum(CurrentChar.traits["int"])
            CurrentChar.traits["rat"][0] = cRat.get()
            CurrentChar.traits["rat"][1] = bRat.get()
            CurrentChar.traits["rat"][2] = pRat.get()
            CurrentChar.traits["rat"][3] = IterSum(CurrentChar.traits["rat"])
            CurrentChar.traits["res"][0] = cRes.get()
            CurrentChar.traits["res"][1] = bRes.get()
            CurrentChar.traits["res"][2] = pRes.get()
            CurrentChar.traits["res"][3] = IterSum(CurrentChar.traits["res"])
            CurrentChar.traits["dip"][0] = cDip.get()
            CurrentChar.traits["dip"][1] = bDip.get()
            CurrentChar.traits["dip"][2] = pDip.get()
            CurrentChar.traits["dip"][3] = IterSum(CurrentChar.traits["dip"])
            CurrentChar.traits["gui"][0] = cGui.get()
            CurrentChar.traits["gui"][1] = bGui.get()
            CurrentChar.traits["gui"][2] = pGui.get()
            CurrentChar.traits["gui"][3] = IterSum(CurrentChar.traits["gui"])
            CurrentChar.traits["itd"][0] = cItd.get()
            CurrentChar.traits["itd"][1] = bItd.get()
            CurrentChar.traits["itd"][2] = pItd.get()
            CurrentChar.traits["itd"][3] = IterSum(CurrentChar.traits["itd"])
            CurrentChar.traits["lea"][0] = cLea.get()
            CurrentChar.traits["lea"][1] = bLea.get()
            CurrentChar.traits["lea"][2] = pLea.get()
            CurrentChar.traits["lea"][3] = IterSum(CurrentChar.traits["lea"])
            CurrentChar.skills["aca"][0] = cAca.get()
            CurrentChar.skills["aca"][1] = bAca.get()
            CurrentChar.skills["aca"][2] = pAca.get()
            CurrentChar.skills["aca"][3] = IterSum(CurrentChar.skills["aca"])
            CurrentChar.skills["cod"][0] = cCod.get()
            CurrentChar.skills["cod"][1] = bCod.get()
            CurrentChar.skills["cod"][2] = pCod.get()
            CurrentChar.skills["cod"][3] = IterSum(CurrentChar.skills["cod"])
            CurrentChar.skills["com"][0] = cCom.get()
            CurrentChar.skills["com"][1] = bCom.get()
            CurrentChar.skills["com"][2] = pCom.get()
            CurrentChar.skills["com"][3] = IterSum(CurrentChar.skills["com"])
            CurrentChar.skills["eng"][0] = cEng.get()
            CurrentChar.skills["eng"][1] = bEng.get()
            CurrentChar.skills["eng"][2] = pEng.get()
            CurrentChar.skills["eng"][3] = IterSum(CurrentChar.skills["eng"])
            CurrentChar.skills["mec"][0] = cMec.get()
            CurrentChar.skills["mec"][1] = bMec.get()
            CurrentChar.skills["mec"][2] = pMec.get()
            CurrentChar.skills["mec"][3] = IterSum(CurrentChar.skills["mec"])
            CurrentChar.skills["med"][0] = cMed.get()
            CurrentChar.skills["med"][1] = bMed.get()
            CurrentChar.skills["med"][2] = pMed.get()
            CurrentChar.skills["med"][3] = IterSum(CurrentChar.skills["med"])
            CurrentChar.skills["met"][0] = cMet.get()
            CurrentChar.skills["met"][1] = bMet.get()
            CurrentChar.skills["met"][2] = pMet.get()
            CurrentChar.skills["met"][3] = IterSum(CurrentChar.skills["met"])
            CurrentChar.skills["pil"][0] = cPil.get()
            CurrentChar.skills["pil"][1] = bPil.ge
            CurrentChar.skills["pil"][2] = pPil.get()
            CurrentChar.skills["pil"][3] = IterSum(CurrentChar.skills["pil"])
            CurrentChar.skills["ste"][0] = cSte.get()
            CurrentChar.skills["ste"][1] = bSte.get()
            CurrentChar.skills["ste"][2] = pSte.get()
            CurrentChar.skills["ste"][3] = IterSum(CurrentChar.skills["ste"])
            CurrentChar.LevelAdjust()        

        def Update(self):
        #Set tkinter variables based on loaded or adjusted python variables.
        #Need to find way around tkinter variables not being global?
            cName.set(CurrentChar.details[0])
            cRace.set(CurrentChar.details[1])
            cSubRace.set(CurrentChar.details[2])
            cAge.set(CurrentChar.details[3])
            cGender.set(CurrentChar.details[4])
            cHeight.set(CurrentChar.details[5])
            cWeight.set(CurrentChar.details[6])
            cLuck.set(CurrentChar.details[7])
            cLevel.set(CurrentChar.exp[0])
            cExp.set(CurrentChar.exp[1])
            cGoal.set(CurrentChar.exp[2])
            tPnts.set(CurrentChar.exp[3])
            sPnts.set(CurrentChar.exp[4])
            pPnts.set(CurrentChar.exp[5])
            aPnts.set(CurrentChar.exp[6])
            uPnts.set(CurrentChar.exp[7])
            cDex.set(CurrentChar.traits["dex"][0])
            bDex.set(CurrentChar.traits["dex"][1])
            pDex.set(CurrentChar.traits["dex"][2])
            tDex.set(CurrentChar.traits["dex"][3])
            cEnd.set(CurrentChar.traits["end"][0])
            bEnd.set(CurrentChar.traits["end"][1])
            pEnd.set(CurrentChar.traits["end"][2])
            tEnd.set(CurrentChar.traits["end"][3])
            cPer.set(CurrentChar.traits["per"][0])
            bPer.set(CurrentChar.traits["per"][1])
            pPer.set(CurrentChar.traits["per"][2])
            tPer.set(CurrentChar.traits["per"][3])
            cStr.set(CurrentChar.traits["str"][0])
            bStr.set(CurrentChar.traits["str"][1])
            pStr.set(CurrentChar.traits["str"][2])
            tStr.set(CurrentChar.traits["str"][3])
            cCon.set(CurrentChar.traits["con"][0])
            bCon.set(CurrentChar.traits["con"][1])
            pCon.set(CurrentChar.traits["con"][2])
            tCon.set(CurrentChar.traits["con"][3])
            cInt.set(CurrentChar.traits["int"][0])
            bInt.set(CurrentChar.traits["int"][1])
            pInt.set(CurrentChar.traits["int"][2])
            tInt.set(CurrentChar.traits["int"][3])
            cRat.set(CurrentChar.traits["rat"][0])
            bRat.set(CurrentChar.traits["rat"][1])
            pRat.set(CurrentChar.traits["rat"][2])
            tRat.set(CurrentChar.traits["rat"][3])
            cRes.set(CurrentChar.traits["res"][0])
            bRes.set(CurrentChar.traits["res"][1])
            pRes.set(CurrentChar.traits["res"][2])
            tRes.set(CurrentChar.traits["res"][3])
            cDip.set(CurrentChar.traits["dip"][0])
            bDip.set(CurrentChar.traits["dip"][1])
            pDip.set(CurrentChar.traits["dip"][2])
            tDip.set(CurrentChar.traits["dip"][3])
            cGui.set(CurrentChar.traits["gui"][0])
            bGui.set(CurrentChar.traits["gui"][1])
            pGui.set(CurrentChar.traits["gui"][2])
            tGui.set(CurrentChar.traits["gui"][3])
            cItd.set(CurrentChar.traits["itd"][0])
            bItd.set(CurrentChar.traits["itd"][1])
            pItd.set(CurrentChar.traits["itd"][2])
            tItd.set(CurrentChar.traits["itd"][3])
            cLea.set(CurrentChar.traits["lea"][0])
            bLea.set(CurrentChar.traits["lea"][1])
            pLea.set(CurrentChar.traits["lea"][2])
            tLea.set(CurrentChar.traits["lea"][3])
            cAca.set(CurrentChar.skills["aca"][0])
            bAca.set(CurrentChar.skills["aca"][1])
            pAca.set(CurrentChar.skills["aca"][2])
            tAca.set(CurrentChar.skills["aca"][3])
            cCod.set(CurrentChar.skills["cod"][0])
            bCod.set(CurrentChar.skills["cod"][1])
            pCod.set(CurrentChar.skills["cod"][2])
            tCod.set(CurrentChar.skills["cod"][3])
            cCom.set(CurrentChar.skills["com"][0])
            bCom.set(CurrentChar.skills["com"][1])
            pCom.set(CurrentChar.skills["com"][2])
            tCom.set(CurrentChar.skills["com"][3])
            cEng.set(CurrentChar.skills["eng"][0])
            bEng.set(CurrentChar.skills["eng"][1])
            pEng.set(CurrentChar.skills["eng"][2])
            tEng.set(CurrentChar.skills["eng"][3])
            cMec.set(CurrentChar.skills["mec"][0])
            bMec.set(CurrentChar.skills["mec"][1])
            pMec.set(CurrentChar.skills["mec"][2])
            tMec.set(CurrentChar.skills["mec"][3])
            cMed.set(CurrentChar.skills["med"][0])
            bMed.set(CurrentChar.skills["med"][1])
            pMed.set(CurrentChar.skills["med"][2])
            tMed.set(CurrentChar.skills["met"][3])
            cMet.set(CurrentChar.skills["met"][0])
            bMet.set(CurrentChar.skills["met"][1])
            pMet.set(CurrentChar.skills["met"][2])
            tMet.set(CurrentChar.skills["met"][3])
            cPil.set(CurrentChar.skills["pil"][0])
            bPil.set(CurrentChar.skills["pil"][1])
            pPil.set(CurrentChar.skills["pil"][2])
            tPil.set(CurrentChar.skills["pil"][3])
            cSte.set(CurrentChar.skills["ste"][0])
            bSte.set(CurrentChar.skills["ste"][1])
            pSte.set(CurrentChar.skills["ste"][2])
            tSte.set(CurrentChar.skills["ste"][3])

        #Begin annoying variable trace callbacks for selecting
        #character race. Placeholder for now to ensure functionality
        #and prevent illegal combinations. Will eventually include
        #stat changes for the various combinations. Don't forget
        #need to consider that with the Import/Update functions!
        def CheckRace(a, b, c):
            if cRace.get() == "Onak'tar" or cRace.get() == "Synthetic Intelligence":
                self.rSelect2.config(state="disabled")
                if cRace.get() == "Onak'tar":
                    pass
                else:
                    pass
            else:
                self.rSelect2.config(state="active")

        def CheckSubRace(a, b, c):
            if cRace.get() == "Sylvid":
                if cSubRace.get() == "Cyborg" or cSubRace.get() == "Android":
                    messagebox.showerror("Racial Compatibility Error", "Sylvid are technophobes. What are you smoking?")
                else:
                    pass
            else:
                pass
        #Yay for the long list of variable traces. Blegh.
        cRace.trace("w", CheckRace)
        cSubRace.trace("w", CheckSubRace)

        
        

root  = Tk()
my_gui = MainGui(root)
root.mainloop()

        


    


