#Here are the Modal Verbs

#Information für Pascal und Jonas
#Ich konnte nicht rausfinden, wie man Klassen aus einem anderen Dokument in dieses importiert.
#Also erstelle ich die Listen erneut


class Modal():
    def __init__(self, verb):
        self.infinitive = verb
        self.allowed_persons = ["1ps", "2ps", "3ps", "1pp", "2pp", "3pp"]
        self.modal_verbs_list_infinitive = ["have", "be", "can", "may", "shall", "will", "must"]
        self.modal_not_aide_verb = ["can", "may", "shall", "must", "will"]
        self.modal_verbs_aide_conj = [["have", "have", "has", "have", "have", "have"], ["am", "are", "is", "are", "are", "are"]]
#Diese Variabeln werden je nach Bedarf erstellt um den Prozess ausführen zu können. Dann werden sie auch definiert
        self.verb_location = None
        self.verb_person = None
        self.invinitive_aid = None
    def give_infinitive(self, person):
        return self.infinitive

    def give_present(self, person):
        if self.infinitive == "have" or self.infinitive == "be":
            if self.infinitive == "have":
                self.verb_location = 0
            else:
                self.verb_location = 1
            for i in range(len(self.allowed_persons)):
                if person == self.allowed_persons[i]:
                    self.verb_person = i
            return self.modal_verbs_aide_conj[self.verb_location][self.verb_person]

        for i in range(len(self.modal_not_aide_verb)):
            if self.infinitive == self.modal_not_aide_verb[i]:
                return self.modal_not_aide_verb[i]

    def give_ing_form(self, person):
        return self.infinitive + "ing"

# ==> Man muss noch die past simple funktion schreiben, ich bin noch nicht dazu gekommen, weil mir das Fachwissen fehlte
    #def give_past_simple(self, person):
#
#        if self.infinitive == "have":
#            return "had"
#        if self.infinitive == "be":
#            if person == "3ps":
#                return "was"
#            else:
#                return "were"
#       if self.infinitive == "can":
#            return "could"
#       if self.infinitive == "may":
#        if self.invinitive == "shall":


    def give_past_participle(self, person):
        if self.infinitive == "be":
            return "been"
        if self.invinitive == "have":
            return "had"

