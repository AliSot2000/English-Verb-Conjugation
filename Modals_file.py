#this is a class to get the modals and the help modals

from main_file import Main as M

#this is just a function to give helpmo
def give_helpModal(person, beOrhave, negationBool, weird, preterite):
    beForms = ["am", "are", "is", "are", "are", "are"]
    beFormsWeird = ["have been", "have been", "has been", "have been", "have been", "have been"]
    bePreterite = ["was", "were", "was", "were", "were", "were"]
    havePreterite = ["had", "had", "had", "had", "had", "had"]
    haveForms = ["have", "have", "has", "have", "have", "have"]
    Index = M.allowed_persons[person]

    if beOrhave == "be":
        if preterite == True:
            if negationBool == False:
                ANSWER = bePreterite[Index]
            else:
                ANSWER = bePreterite[Index]
                ANSWER += "n`t"
        elif weird == True:  # for all present perfect progressive cases    WEIRD KANN MAN AUS PRETERITE UND SHIT ZUSAMMENSETZEN !! => FALLS MAN DEN CODE VERSCHOENERN MOECHTE!
            if negationBool == False:
                ANSWER = beFormsWeird[Index]
            else:
                ANSWER = beFormsWeird[Index]
                if len(ANSWER) == 8:
                    ANSWER = "has not been"
                else:
                    ANSWER = "haven`t been"
        elif negationBool == False:
            ANSWER = beForms[Index]
        else :
            ANSWER = beForms[Index]
            if "e" in ANSWER:
                ANSWER.replace("e", "n`t")
            else:
                ANSWER += " not"
    else:
        if preterite == True:
            if negationBool == False:
                ANSWER = havePreterite[Index]
            else:
                ANSWER = havePreterite[Index]
                ANSWER += "n`t"
        elif negationBool == False:
            ANSWER = haveForms[Index]
        else:
            ANSWER = haveForms[Index]
            if "e" in ANSWER:
                ANSWER.replace("e", "n`t")
            else:
                ANSWER += " not"

    return ANSWER

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#here is the class for the "normal" operations

class Modal():
    def __init__(self, verb):
        self.given_verb = verb
        self.all_persons = ["1ps", "2ps", "3ps", "1pp", "2pp", "3pp"]
        self.all_modals_infinitive = ["have", "be", "can", "may", "shall", "will", "must"]

        self.conjugated_modals_present = [["have", "have", "has", "have", "have", "have"],
                                               ["am", "are", "is", "are", "are", "are"],
                                               ["can", "can", "can", "can", "can", "can"],
                                               ["may", "may", "may", "may", "may", "may"],
                                               ["shall", "shall", "shall", "shall", "shall", "shall"],
                                               ["will", "will", "will", "will", "will", "will"],
                                               ["must", "must", "must", "must", "must", "must"]]

        self.conjugated_modal_verbs_simplePast = [["had", "had", "had", "had", "had", "had"],
                                            ["was", "were", "was", "were", "were", "were"],
                                            ["canned", "canned", "canned", "canned", "canned", "canned"],
                                            ["might", "might", "might", "might", "might", "might"],
                                            ["should", "should", "should", "should", "should", "should"],
                                            ["would", "would", "would", "would", "would", "would"],
                                            []]#fuer must giebts keinen shit!!

        self.conjugated_modal_verbs_pastParticiple = ["had", "been", "canned", "might", "should", "would", ""]      # fuer must giebt es kein past participle

    def give_infinitive(self):
        return self.given_verb

    def give_present(self, person):
        indexPerson = self.all_persons[person]
        indexVerb = self.all_modals_infinitive[self.given_verb]
        return self.conjugated_modals_present[indexVerb][indexPerson]

    def give_past_simple(self, person):
        indexPerson = self.all_persons[person]
        indexVerb = self.all_modals_infinitive[self.given_verb]
        try:
            return self.conjugated_modal_verbs_simplePast[indexVerb][indexPerson]
        except:
            return "MUST DOES NOT HAVE A PAST SIMPLE FORM!!"

    def give_past_participle(self, person):
        indexVerb = self.all_modals_infinitive[self.given_verb]
        try:
            return self.conjugated_modal_verbs_pastParticiple[indexVerb]
        except:
            return "MUST DOES NOT HAVE A PAST PARTICIPLE!!"






