class Dad:
    def football(self):
        print("Dad likes watching football")

class Mom:
    def cooking(self):
        print("Mom likes cooking")

class Boy(Dad):
    def boyage(self):
        print("I'm 17 years old.")

class Girl(Mom):
    def girl(self):
        print("I'm 18 years old.")


my_boy = Boy()
my_boy.football()
my_boy.boyage()
my_girl = Girl()
my_girl.girl()
my_girl.cooking()
