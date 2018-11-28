# hallo das ist der main-file
import regular_file as rg
import Modals_file as md
import irregular_file as ir


class Main():
    def __init__(self):
        self.allowed_persons = ["1ps", "2ps", "3ps", "1pp", "2pp", "3pp"]
        self.allowed_times = ["present", "past", "future", "conditional"]
        self.allowed_mode_simOrPer = ["simple", "perfect"]
        self.allowed_mode_conOrNor = ["continuous", "progressive"]
        self.allowed_positive = ["negation", "negative", "-", "negated", "not"]
        self.allowed_also = ["positive", "pro", "+", "yesbaabyy!"]
        self.all_modal_verbs = ["have", "be", "can", "may", "shall", "will", "must"]
        self.all_irregular_verbs = ['arise', 'awake', 'bear', 'beat', 'become', 'begin', 'bend', 'bet', 'bid', 'bind',
                                    'bite', 'bleed', 'blow', 'break', 'breed', 'bring', 'broadcast', 'build', 'burn',
                                    'buy', 'catch', 'choose', 'cling', 'come', 'cost', 'creep', 'cut', 'deal', 'dig',
                                    'do', 'draw', 'dream', 'drink', 'drive', 'eat', 'fall', 'feed', 'feel', 'fight',
                                    'find', 'fly', 'forbid', 'forget', 'forgive', 'freeze', 'get', 'give', 'go',
                                    'grind', 'grow', 'hang', 'hear', 'hide', 'hit', 'hold', 'hurt', 'keep', 'kneel',
                                    'know', 'lay', 'lead', 'learn', 'leave', 'lend', 'let', 'lie', 'lie', 'light',
                                    'lose', 'make', 'mean', 'meet', 'mow', 'pay', 'put', 'read', 'ride', 'ring', 'rise',
                                    'run', 'saw', 'say', 'see', 'sell', 'send', 'sew', 'shake', 'shed', 'shine',
                                    'shoot', 'show', 'shrink', 'shut', 'sing', 'sink', 'sit', 'sleep', 'slide', 'smell',
                                    'sow', 'speak', 'spell', 'spend', 'spill', 'spit', 'spread', 'stand', 'steal',
                                    'stick', 'sting', 'stink', 'strike', 'swear', 'sweep', 'swell', 'swim', 'swing',
                                    'take', 'teach', 'tear', 'tell', 'think', 'throw', 'understand', 'wake', 'wear',
                                    'weep', 'win', 'wind', 'write']
        self.all_irregular_verbs_pasts = ['arose', 'awoke', 'bore', 'beat', 'became', 'began', 'bent', 'bet', 'bid',
                                          'bound', 'bit', 'bled', 'blew', 'broke', 'bred', 'brougnt', 'broadcast',
                                          'built', 'burnt', 'bought', 'caught', 'chose', 'clung', 'came', 'cost',
                                          'crept', 'cut', 'dealt', 'dug', 'did', 'drew', 'dreamt', 'drank', 'drove',
                                          'ate', 'fell', 'fed', 'felt', 'fought', 'found', 'flew', 'forbade', 'forgot',
                                          'forgave', 'froze', 'got', 'gave', 'went', 'ground', 'grew', 'hung', 'heard',
                                          'hid', 'hit', 'held', 'hurt', 'kept', 'knelt', 'knew', 'laid', 'led',
                                          'learnt', 'left', 'lent', 'let', 'lay', 'lied', 'lit', 'lost', 'made',
                                          'meant', 'met', 'mowed', 'paid', 'put', 'read', 'rode', 'rang', 'rose', 'ran',
                                          'sawed', 'said', 'saw', 'sold', 'sent', 'sewed', 'shook', 'shed', 'shone',
                                          'shot', 'showed', 'shrank', 'shut', 'sang', 'sank', 'sat', 'slept', 'slid',
                                          'smelt', 'sowed', 'spoke', 'spelt', 'spent', 'spilt', 'spat', 'spread',
                                          'stood', 'stole', 'stuck', 'stung', 'stuank', 'struck', 'swore', 'swept',
                                          'swelled', 'swam', 'swung', 'took', 'taught', 'tore', 'told', 'thought',
                                          'threw', 'understood', 'woke', 'wore', 'wept', 'won', 'wound', 'wrote']
        self.all_irregular_verbs_pastp = ['arisen', 'awoken', 'been', 'born', 'beaten', 'become', 'begun', 'bent',
                                          'bet', 'bid', 'bound', 'bitten', 'bled', 'blown', 'broken', 'bred', 'brought',
                                          'broadcast', 'built', 'burnt', 'bought', 'could', 'caught', 'chosen', 'clung',
                                          'come', 'cost', 'crept', 'cut', 'dealt', 'dug', 'done', 'drawn', 'dreamt',
                                          'drunk', 'driven', 'eaten', 'fallen', 'fed', 'felt', 'fought', 'found',
                                          'flown', 'forbidden', 'forgotten', 'forgiven', 'frozen', 'got', 'given',
                                          'gone', 'ground', 'grown', 'hung', 'had', 'heard', 'hidden', 'hit', 'held',
                                          'hurt', 'kept', 'knelt', 'known', 'laid', 'led', 'learnt', 'left', 'lent',
                                          'let', 'lain', 'lied', 'lit', 'lost', 'made', 'meant', 'met', 'mown/mowed',
                                          'paid', 'put', 'read', 'ridden', 'rung', 'risen', 'run', 'sawn/sawed', 'said',
                                          'seen', 'sold', 'sent', 'sewn/sewed', 'shaken', '', 'shed', 'shone', 'shot',
                                          'shown', 'shrunk', 'shut', 'sung', 'sunk', 'sat', 'slept', 'slid', 'smelt',
                                          'sown/sowed', 'spoken', 'spelt', 'spent', 'spilt', 'spat', 'spread', 'stood',
                                          'stolen', 'stuck', 'stung', 'stunk', 'struck', 'sworn', 'swept',
                                          'swollen/swelled', 'swum', 'swung', 'taken', 'taught', 'torn', 'told',
                                          'thought', 'thrown', 'understood', 'woken', 'worn', 'wept', '-', 'won',
                                          'wound', 'written']
        self.all_modal_verbs = []
        self.persons_in_sentece = ["I", "You", "He/She/It", "We", "You", "They"]
        self.negations_in_sentence = ["don`t", "don`t", "doesn`t", "don`t", "don`t", "don`t"]
        self.get_user_input()
        self.sort_verb()
        self.grammar()

    def get_user_input(self):
        newInput = raw_input(" Give a verb, a person, a time, and + or -\n Example: walk, 2ps, past perfect continuous, + \n Your input: ")
        split_input = newInput.split(", ")
        for part in split_input:   #Das ist ein bischen brute-forcy (2 for-loops -> O=N^2)
            copy_part = part
            part_divided = copy_part.split(" ")
            if len(part_divided) > 1:
                split_input.remove(part)
                for element in part_divided:
                    split_input.append(element)
        for part in split_input:
            if part in self.allowed_persons:
                self.requested_person = part
            elif part in self.allowed_times:
                self.requested_time = part
            elif part in self.allowed_mode_simOrPer:
                self.requested_mode_simOrPer = part
            elif part in self.allowed_mode_conOrNor:
                self.requested_mode_conOrNor = "continuous"
            elif part in self.allowed_positive:
                self.requested_positive = "negative"
            elif part in self.allowed_also:
                self.requested_positive = "positive"
            else:
                self.verb = part
        if not hasattr(self, "requested_simorper"):  #GSEHT NACH COOLEM CODE US!
            self.requested_mode_simOrPer = "simple"
        if not hasattr(self, "requested_mode_conornor"):
            self.requested_mode_conOrNor = "normal"
        if not hasattr(self, "requested_positive"):
            self.requested_positive = "positive"

    def grammar(self):
    #PRESENT
        if self.requested_time == "present":

            if self.requested_mode_simOrPer == "simple":    #present simple (+/-)
                if self.requested_mode_conOrNor == "normal":
                    if self.requested_positive == "positive":
                        self.ANSWER = self.person_normalizer() + " " + self.verb_object.give_present(self.requested_person, False)
                    elif self.requested_positive == "negative":
                        self.ANSWER = self.person_normalizer() + " " + self.negation_normalizer() + " " + self.verb_object.give_present(self.requested_person, True)

                elif self.requested_mode_conOrNor == "continuous":  #present continuous   give_helpModal(person, beOrhave, negationBool):
                    if self.requested_positive == "positive":
                        self.ANSWER = self.person_normalizer() + " " + md.give_helpModal(self.requested_person, "be", False) + " " + self.verb_object.give_ing_form(self.requested_person)
                    elif self.requested_positive == "negative":
                        self.ANSWER = self.person_normalizer() + " " + md.give_helpModal(self.requested_person, "be", True) + " " + self.verb_object.give_ing_form(self.requested_person)

            elif self.requested_mode_simOrPer == "perfect":     #present perfect
                if self.requested_mode_conOrNor == "normal":
                    if self.requested_positive == "positive":
                        self.ANSWER = self.person_normalizer() + " " + md.give_helpModal(self.requested_person, "have", False, False) + " " + self.verb_object.give_past_participle(self.requested_person)
                    elif self.requested_positive == "negative":
                        self.ANSWER = self.person_normalizer() + " " + md.give_helpModal(self.requested_person, "have",True, False) + " " + self.verb_object.give_past_participle(self.requested_person)

                elif self.requested_mode_conOrNor == "continuous":    #present perfect continuous
                    if self.requested_positive == "positive":
                        self.ANSWER = self.person_normalizer() + " " + md.give_helpModal(self.requested_person, "have", False, True) + " " + self.verb_object.give_ing_form(self.requested_person)
                    elif self.requested_positive == "negative":
                        self.ANSWER = self.person_normalizer() + " " + md.give_helpModal(self.requested_person, "have",False, True) + " " + self.verb_object.give_ing_form(self.requested_person)
    #PAST
        elif self.requested_time == "past":

            if self.requested_mode_simOrPer == "simple":        #past simple
                if self.requested_mode_conOrNor == "normal":
                    if self.requested_positive == "positive":
                        self.ANSWER = self.person_normalizer() + " " + self.verb_object.give_past_simple(self.requested_person)
                    elif self.requested_positive == "negative":
                        self.ANSWER = self.person_normalizer() + " didn`t " + self.verb_object.give_past_simple(self.requested_person)

                elif self.requested_mode_conOrNor == "continuous":      #past continuous
                    if self.requested_positive == "positive":
                        self.ANSWER = self.person_normalizer() + " " + md.give_helpModal(self.requested_person, "be", False, False, True) + " " + self.verb_object.give_ing_form(self.requested_person)
                    elif self.requested_positive == "negative":
                        self.ANSWER = self.person_normalizer() + " " + md.give_helpModal(self.requested_person, "be",False, False,True) + " " + self.verb_object.give_ing_form(self.requested_person)

            elif self.requested_mode_simOrPer == "perfect":         #past perfect
                if self.requested_mode_conOrNor == "normal":
                    if self.requested_positive == "positive":
                        self.ANSWER = self.person_normalizer() + " had " + self.verb_object.give_past_participle(self.requested_person)
                    elif self.requested_positive == "negative":
                        self.ANSWER = self.person_normalizer() + " hadn`t " + self.verb_object.give_past_participle(self.requested_person)

                elif self.requested_mode_conOrNor == "continuous":      #past perfect continuous
                    if self.requested_positive == "positive":
                        self.ANSWER = self.person_normalizer() + " " + md.give_helpModal(self.requested_person, "had", False, False, True) + " " + md.give_helpModal(self.requested_person, "be", False, False, True) + " " + self.verb_object.give_ing_form(self.requested_person)
                    elif self.requested_positive == "negative":
                        self.ANSWER = self.person_normalizer() + " " + md.give_helpModal(self.requested_person, "had", True, False, True) + " " + md.give_helpModal(self.requested_person, "be", False, False, True) + " " + self.verb_object.give_ing_form(self.requested_person)

    #FUTURE
        elif self.requested_time == "future":
            if self.requested_mode_simOrPer == "simple":            #will future // future simple
                if self.requested_mode_conOrNor == "normal":
                    if self.requested_positive == "positive":
                        self.ANSWER = self.person_normalizer() + " will " + self.verb
                    elif self.requested_positive == "negative":
                        self.ANSWER = self.person_normalizer() + " won`t " + self.verb

                elif self.requested_mode_conOrNor == "continuous":          #future continuous
                    if self.requested_positive == "positive":
                        self.ANSWER = self.person_normalizer() + " will be " + self.verb_object.give_ing_form(self.requested_person)
                    elif self.requested_positive == "negative":
                        self.ANSWER = self.person_normalizer() + " won`t be " + self.verb_object.give_ing_form(self.requested_person)

            elif self.requested_mode_simOrPer == "perfect":             #future perfect
                if self.requested_mode_conOrNor == "normal":
                    if self.requested_positive == "positive":
                        self.ANSWER = self.person_normalizer() + " will have " + self.verb_object.give_past_participle(self.requested_person)
                    elif self.requested_positive == "negative":
                        self.ANSWER = self.person_normalizer() + " will not have " + self.verb_object.give_past_participle(self.requested_person)

                elif self.requested_mode_conOrNor == "continuous":      #future perfect continuous
                    if self.requested_positive == "positive":
                        self.ANSWER = self.person_normalizer() + " will have been " + self.verb_object.give_ing_form(self.requested_person)
                    elif self.requested_positive == "negative":
                        self.ANSWER = self.person_normalizer() + " will not have been " + self.verb_object.give_ing_form(self.requested_person)

    #CONDITIONAL
        elif self.requested_time == "conditional":
            if self.requested_mode_simOrPer == "simple":            #simple conditional
                if self.requested_mode_conOrNor == "normal":
                    if self.requested_positive == "positive":
                        self.ANSWER = self.person_normalizer() + " would " + self.verb
                    elif self.requested_positive == "negative":
                        self.ANSWER = self.person_normalizer() + " wouldn`t " + self.verb

                elif self.requested_mode_conOrNor == "continuous":      #conditional continuous
                    if self.requested_positive == "positive":
                        self.ANSWER = self.person_normalizer() + " would be " + self.verb_object.give_ing_form(self.requested_person)
                    elif self.requested_positive == "negative":
                        self.ANSWER = self.person_normalizer() + " wouldn`t be " + self.verb_object.give_ing_form(self.requested_person)

            elif self.requested_mode_simOrPer == "perfect":             #conditional perfect
                if self.requested_mode_conOrNor == "normal":
                    if self.requested_positive == "positive":
                        self.person_normalizer() + " would have " + self.verb_object.give_past_participle(self.requested_person)
                    elif self.requested_positive == "negative":
                        self.person_normalizer() + " wouldn`t have " + self.verb_object.give_past_participle(self.requested_person)

                elif self.requested_mode_conOrNor == "continuous":      #conditional perfect continuous
                    if self.requested_positive == "positive":
                        self.person_normalizer() + " would have been " + self.verb_object.give_ing_form(self.requested_person)
                    elif self.requested_positive == "negative":
                        self.person_normalizer() + " wouldn`t have been " + self.verb_object.give_ing_form(self.requested_person)

        print(self.ANSWER + "\n")


    def sort_verb(self):
        if self.verb in self.all_irregular_verbs:
            self.verb_object = ir.Irregular(self.verb)  #erstellt bei jedem verbtyp ein objekt der klasse des verbtyps
        elif self.verb in self.all_modal_verbs:
            self.verb_object = md.Modal(self.verb)
        else:
            self.verb_object = rg.Regular(self.verb)

    def person_normalizer(self):
        index = self.allowed_persons.index(self.requested_person)
        return self.persons_in_sentece[index]

    def negation_normalizer(self):
        place = self.allowed_persons.index(self.requested_person)
        return self.negations_in_sentence[place]

#=============================================================================================================================================
# MAIN PROGRAMM
#=============================================================================================================================================

print("                               _______")
print("                           ---         ---")
print("                        --                 --")
print("                      -                       -")
print("                     /       |           |     |")
print("                    |                           |")
print("                   |               /             |")
print("                   |              . .            |")
print("                   |                             |")
print("                    |         _         _       |")
print("                     \         \-------/       /")
print("                      -                       -")
print("                        --                 --")
print("                           ---         ---")
print("                               -------")
print("                              FUCK YEAH!")
print("               THIS IS OUR ENGLISH CONJUGATIOIN PROGRAMM!!")
print("               -------------------------------------------")
print("                                PASCAL")
print("                               ALEXANDER")
print("                          JONAS FUCKING STAUB\n\n")



while(True):
    main = Main()
    A = raw_input("Do You want to continue? ...\n enter=Yes // n=No\n ...")
    if A == "n":
        exit()
    print("\n ******************************************************** \n")