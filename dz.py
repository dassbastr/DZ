class TankfactoryKV2:
    def __init__(self,name):
        self.name = name


class ArmorDetais:
    def __init__(self,frontarmor,sidearmor,backarmor,towerarmor):
        self.frontarmor = frontarmor
        self.sidearmor = sidearmor
        self.backarmor = backarmor
        self.towerarmor = towerarmor
        if self.frontarmor >=7 and self.frontarmor <=10:
            self.frontarmor_quality = True
            if self.sidearmor >=7 and self.sidearmor <=10:
                self.sidearmor_quality = True
                if self.backarmor >=7 and self.backarmor <=10:
                    self.backarmor_quality = True
                    if self.towerarmor >=7 and self.towerarmor <=10:
                        self.towerarmor_quality = True
                    else:
                        self.towerarmor_quality = False
                else:
                    self.backarmor_quality = False
            else:
                self.sidearmor_quality = False
        else:
            self.frontarmor_quality = False


class Mechanisms:
    def __init__(self,engine,runninggear,caterpillars ):
        self.engine = engine
        self.runninggear = runninggear
        self.caterpillars = caterpillars
        if self.engine >=7 and self.engine <=10:
            self.engine_quality = True
            if self.runninggear >=7 and self.runninggear <=10:
                self.runninggear_quality = True
                if self.caterpillars >=7 and self.caterpillars <=10:
                    self.caterpillars_quality = True
                else:
                    self.caterpillars_quality = False
            else:
                self.runninggear_quality = False
        else:
            self.engine_quality = False


class Insidesofelectricity:
    def __init__(self,light,communication,ectricitymechanisms):
        self.light = light
        self.communication = communication
        self.ectricitymechanisms = ectricitymechanisms
        if self.light >=7 and self.light <=10:
            self.light_quality = True
            if self.communication >=7 and self.communication <=10:
                self.communication_quality = True
                if self.ectricitymechanisms >=7 and self.ectricitymechanisms <=10:
                    self.ectricitymechanisms_quality = True
                else:
                    self.ectricitymechanisms_quality = False
            else:
                self.communication_quality = False
        else:
            self.light_quality = False


def name():
    nameFactory = TankfactoryKV2('ТАНКОВИЙ ЗАВОД ІМЕНІ ЛАПЧАКА')
    print(nameFactory.name)


def collectingparts1():
    armorDetais = ArmorDetais(9,9,7,10)
    if armorDetais.frontarmor_quality == True and armorDetais.sidearmor_quality == True and armorDetais.backarmor_quality == True and armorDetais.towerarmor_quality == True:
        print("Броня танка у порядку")
    else:
        print("Броня танка не у порядку")


def collectingparts2():
    mechanisms = Mechanisms(8,8,9)
    if mechanisms.engine_quality == True and mechanisms.runninggear_quality == True and mechanisms.caterpillars_quality == True:
        print("Механізм танка у порядку")
    else:
        print("Механізм танка не у порядку")


def collectingparts3():
    insidesofelectricity = Insidesofelectricity(10,7,8)
    if insidesofelectricity.light_quality == True and insidesofelectricity.communication_quality == True and insidesofelectricity.ectricitymechanisms_quality == True:
        print("Нутрощі електрики танка у порядку")
    else:
        print("Нутрощі електрики танка не у порядку")


def tank():
    armorDetais = ArmorDetais(2,9,7,10)
    mechanisms = Mechanisms(8,8,9)
    insidesofelectricity = Insidesofelectricity(10,7,8)
    if armorDetais.frontarmor_quality == True and armorDetais.sidearmor_quality == True and armorDetais.backarmor_quality == True and armorDetais.towerarmor_quality == True and mechanisms.engine_quality == True and mechanisms.runninggear_quality == True and mechanisms.caterpillars_quality == True and insidesofelectricity.light_quality == True and insidesofelectricity.communication_quality == True and insidesofelectricity.ectricitymechanisms_quality == True:
        print("Танк можна збирати")
    else:
        print("Танк не можна збирати")


def main():
    name()
    collectingparts1()
    collectingparts2()
    collectingparts3()
    tank()

main()