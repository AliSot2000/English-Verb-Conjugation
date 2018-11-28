#this is the regular file
class Regular():
    def __init__(self, verb):
        self.infinitive = verb
    def give_infinitive(self, person):
        return self.infinitive

    def give_present(self, person, negationBool):
        if person == "3ps":
            if self.infinitive[-1] == "o" or (self.infinitive[-1] == "h" and self.infinitive[-2] == "c"):  #HIER GIBT ES NOCH BUGS!!!!!!!
                return self.infinitive + "es"
            elif self.infinitive[-1] == "y":
                return self.infinitive.replace("y", "ies")
            elif negationBool == True:
                return self.infinitive
            else:
                return self.infinitive + "s"
        else:
            return self.infinitive

    def give_ing_form(self, person):
        return self.infinitive + "ing"

    def give_past_simple(self, person):
        if self.infinitive[-1] == "y":
            return self.infinitive + "ied"
        else:
            return self.infinitive + "ed"

    def give_past_participle(self, person):
        if self.infinitve[-1] == "y":
            return self.infinitive + "ied"
        else:
            return self.infinitive + "ed"