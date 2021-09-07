import requests

class ChampRunes():
    perk0id = int()
    perk1id = int()
    perk2id = int()
    perk3id = int()
    perk4id = int()
    perk5id = int()
    perkPrimaryStyleid = int()
    perkSubStyleid = int()
    perk0icon = str()
    perk1icon = str()
    perk2icon = str()
    perk3icon = str()
    perk4icon = str()
    perk5icon = str()
    perkPrimaryStyleicon = str()
    perkSubStyleicon = str()
    """
    perk0 = str()
    perk1 = str()
    perk2 = str()
    perk3 = str()
    perk4 = str()
    perk5 = str()
    perkPrimaryStyle = str()
    perkSubStyle = str()
    """

    def __init__(self, match, matchPID):
        
        self.perk0id = int(match["participants"][matchPID]["stats"]["perk0"])
        self.perk1id = int(match["participants"][matchPID]["stats"]["perk1"])
        self.perk2id = int(match["participants"][matchPID]["stats"]["perk2"])
        self.perk3id = int(match["participants"][matchPID]["stats"]["perk3"])
        self.perk4id = int(match["participants"][matchPID]["stats"]["perk4"])
        self.perk5id = int(match["participants"][matchPID]["stats"]["perk5"])
        self.perkPrimaryStyleid = int(match["participants"][matchPID]["stats"]["perkPrimaryStyle"])
        self.perkSubStyleid = int(match["participants"][matchPID]["stats"]["perkSubStyle"])

       

    def getRunesInfo(self):
        RuneIDs = dict()
        Slots = dict()
        
        RuneIDs[8100] = 0   # Domination
        RuneIDs[8300] = 1   # Inspiration
        RuneIDs[8000] = 2   # Precision
        RuneIDs[8400] = 3   # Resolve
        RuneIDs[8200] = 4   # Sorcery 

        
        RuneIDs[8112] = 0 
        Slots[8112] = 0
        RuneIDs[8124] = 1 
        Slots[8124] = 0
        RuneIDs[8128] = 2 
        Slots[8128] = 0
        RuneIDs[9923] = 3
        Slots[9923] = 0

        RuneIDs[8126] = 0 
        Slots[8126] = 1
        RuneIDs[8139] = 1 
        Slots[8139] = 1
        RuneIDs[8143] = 2 
        Slots[8143] = 1

        RuneIDs[8136] = 0 
        Slots[8136] = 2
        RuneIDs[8120] = 1 
        Slots[8120] = 2
        RuneIDs[8138] = 2 
        Slots[8138] = 2

        RuneIDs[8135] = 0 
        Slots[8135] = 3
        RuneIDs[8134] = 1 
        Slots[8134] = 3
        RuneIDs[8105] = 2 
        Slots[8105] = 3
        RuneIDs[8106] = 3 
        Slots[8106] = 3


        # Inspiration Runes 8300
        RuneIDs[8351] = 0 
        Slots[8351] = 0
        RuneIDs[8360] = 1
        Slots[8360] = 0
        RuneIDs[8358] = 2 
        Slots[8358] = 0

        RuneIDs[8306] = 0 
        Slots[8306] = 1
        RuneIDs[8304] = 1 
        Slots[8304] = 1
        RuneIDs[8313] = 2 
        Slots[8313] = 1

        RuneIDs[8321] = 0 
        Slots[8321] = 2
        RuneIDs[8316] = 1 
        Slots[8316] = 2
        RuneIDs[8345] = 2 
        Slots[8345] = 2

        RuneIDs[8347] = 0 
        Slots[8347] = 3
        RuneIDs[8410] = 1 
        Slots[8410] = 3
        RuneIDs[8352] = 2 
        Slots[8352] = 3


        # Sorcery Runes [8200]
        RuneIDs[8214] = 0 
        Slots[8214] = 0
        RuneIDs[8229] = 1 
        Slots[8229] = 0
        RuneIDs[8230] = 2 
        Slots[8230] = 0

        RuneIDs[8224] = 0 
        Slots[8224] = 1
        RuneIDs[8226] = 1 
        Slots[8226] = 1
        RuneIDs[8275] = 2 
        Slots[8275] = 1

        RuneIDs[8210] = 0 
        Slots[8210] = 2
        RuneIDs[8234] = 1 
        Slots[8234] = 2
        RuneIDs[8233] = 2 
        Slots[8233] = 2

        RuneIDs[8237] = 0 
        Slots[8237] = 3
        RuneIDs[8232] = 1 
        Slots[8232] = 3
        RuneIDs[8236] = 2 
        Slots[8236] = 3


        # Precision Runes [8000]
        RuneIDs[8005] = 0 
        Slots[8005] = 0
        RuneIDs[8008] = 1 
        Slots[8008] = 0
        RuneIDs[8021] = 2 
        Slots[8021] = 0
        RuneIDs[8010] = 3 
        Slots[8010] = 0

        RuneIDs[9101] = 0 
        Slots[9101] = 1
        RuneIDs[9111] = 1 
        Slots[9111] = 1
        RuneIDs[8009] = 2 
        Slots[8009] = 1

        RuneIDs[9104] = 0 
        Slots[9104] = 2
        RuneIDs[9105] = 1 
        Slots[9105] = 2
        RuneIDs[9103] = 2 
        Slots[9103] = 2

        RuneIDs[8014] = 0 
        Slots[8014] = 3
        RuneIDs[8017] = 1 
        Slots[8017] = 3
        RuneIDs[8299] = 2 
        Slots[8299] = 3



        # Resolve Runes [8400]
        RuneIDs[8437] = 0 
        Slots[8437] = 0
        RuneIDs[8439] = 1 
        Slots[8439] = 0
        RuneIDs[8465] = 2 
        Slots[8465] = 0

        RuneIDs[8446] = 0 
        Slots[8446] = 1
        RuneIDs[8463] = 1 
        Slots[8463] = 1
        RuneIDs[8401] = 2 
        Slots[8401] = 1

        RuneIDs[8429] = 0 
        Slots[8429] = 2
        RuneIDs[8444] = 1 
        Slots[8444] = 2
        RuneIDs[8473] = 2 
        Slots[8473] = 2

        RuneIDs[8451] = 0 
        Slots[8451] = 3
        RuneIDs[8453] = 1 
        Slots[8453] = 3
        RuneIDs[8242] = 2 
        Slots[8242] = 3
        
        Runesj = requests.get("http://ddragon.leagueoflegends.com/cdn/11.15.1/data/en_US/runesReforged.json")
        RunesObject = Runesj.json()
        print("Runes: ")
        perk0 = str(RunesObject[RuneIDs[self.perkPrimaryStyleid]]["slots"][Slots[self.perk0id]]["runes"][RuneIDs[self.perk0id]]["name"])
        perk0icon = str(RunesObject[RuneIDs[self.perkPrimaryStyleid]]["slots"][Slots[self.perk0id]]["runes"][RuneIDs[self.perk0id]]["icon"])
        perk1 = str(RunesObject[RuneIDs[self.perkPrimaryStyleid]]["slots"][Slots[self.perk1id]]["runes"][RuneIDs[self.perk1id]]["name"])
        perk1icon = str(RunesObject[RuneIDs[self.perkPrimaryStyleid]]["slots"][Slots[self.perk1id]]["runes"][RuneIDs[self.perk1id]]["icon"])
        perk2 = str(RunesObject[RuneIDs[self.perkPrimaryStyleid]]["slots"][Slots[self.perk2id]]["runes"][RuneIDs[self.perk2id]]["name"])
        perk2icon = str(RunesObject[RuneIDs[self.perkPrimaryStyleid]]["slots"][Slots[self.perk2id]]["runes"][RuneIDs[self.perk2id]]["icon"])
        perk3 = str(RunesObject[RuneIDs[self.perkPrimaryStyleid]]["slots"][Slots[self.perk3id]]["runes"][RuneIDs[self.perk3id]]["name"])
        perk3icon = str(RunesObject[RuneIDs[self.perkPrimaryStyleid]]["slots"][Slots[self.perk3id]]["runes"][RuneIDs[self.perk3id]]["icon"])
        perk4 = str(RunesObject[RuneIDs[self.perkSubStyleid]]["slots"][Slots[self.perk4id]]["runes"][RuneIDs[self.perk4id]]["name"])
        perk4icon = str(RunesObject[RuneIDs[self.perkSubStyleid]]["slots"][Slots[self.perk4id]]["runes"][RuneIDs[self.perk4id]]["icon"])
        perk5 = str(RunesObject[RuneIDs[self.perkSubStyleid]]["slots"][Slots[self.perk5id]]["runes"][RuneIDs[self.perk5id]]["name"])
        perk5icon = str(RunesObject[RuneIDs[self.perkSubStyleid]]["slots"][Slots[self.perk5id]]["runes"][RuneIDs[self.perk5id]]["icon"])
        perkPrimaryStyle = str(RunesObject[RuneIDs[self.perkPrimaryStyleid]]["name"])
        perkPrimaryStyleicon = str(RunesObject[RuneIDs[self.perkPrimaryStyleid]]["icon"])
        perkSubStyle = str(RunesObject[RuneIDs[self.perkSubStyleid]]["name"])
        perkSubStyleicon = str(RunesObject[RuneIDs[self.perkSubStyleid]]["icon"])

        print("Primary" + " " + perkPrimaryStyle)
        print("Runes: " + perk0 + " " + perk1 + " " + perk2 + " " + perk3)
        print("Secondary:" + " " + perkSubStyle)
        print("Runes:" + " " + perk4 + " " + perk5)

        return [perk0, perk1, perk2, perk3, perk4, perk5, perkPrimaryStyle, perkSubStyle,
                perk0icon, perk1icon, perk2icon, perk3icon, perk4icon, perk5icon,
                perkPrimaryStyleicon, perkSubStyleicon] 
        
        

