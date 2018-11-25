#hallo das ist der main-file
import regularV2 as rg
import modal as md
import irregular as ir

class Main():
    def __init__(self):
        self.allowed_persons = ["1ps", "2ps", "3ps", "1pp", "2pp", "3pp"]
        self.allowed_times = ["present", "past", "future", "conditional"]
        self.allowed_mode_simorper = ["simple", "perfect"]
        self.allowed_mode_conornor = ["continuous", "progressive"]
        self.allowed_positive = ["negation", "negative", "-", "negated", "not"]
        self.allowed_also = ["positive", "pro", "+"]
        self.all_irregular_verbs = ['arise', 'awake', 'bear', 'beat', 'become', 'begin', 'bend', 'bet', 'bid', 'bind', 'bite', 'bleed', 'blow', 'break', 'breed', 'bring', 'broadcast', 'build', 'burn', 'buy', 'catch', 'choose', 'cling', 'come', 'cost', 'creep', 'cut', 'deal', 'dig', 'do', 'draw', 'dream', 'drink', 'drive', 'eat', 'fall', 'feed', 'feel', 'fight', 'find', 'fly', 'forbid', 'forget', 'forgive', 'freeze', 'get', 'give', 'go', 'grind', 'grow', 'hang', 'hear', 'hide', 'hit', 'hold', 'hurt', 'keep', 'kneel', 'know', 'lay', 'lead', 'learn', 'leave', 'lend', 'let', 'lie', 'lie', 'light', 'lose', 'make', 'mean', 'meet', 'mow', 'pay', 'put', 'read', 'ride', 'ring', 'rise', 'run', 'saw', 'say', 'see', 'sell', 'send', 'sew', 'shake', 'shed', 'shine', 'shoot', 'show', 'shrink', 'shut', 'sing', 'sink', 'sit', 'sleep', 'slide', 'smell', 'sow', 'speak', 'spell', 'spend', 'spill', 'spit', 'spread', 'stand', 'steal', 'stick', 'sting', 'stink', 'strike', 'swear', 'sweep', 'swell', 'swim', 'swing', 'take', 'teach', 'tear', 'tell', 'think', 'throw', 'understand', 'wake', 'wear', 'weep', 'win', 'wind', 'write']
        self.all_irregular_verbs_pasts = ['arose', 'awoke', 'bore', 'beat', 'became', 'began', 'bent', 'bet', 'bid', 'bound', 'bit', 'bled', 'blew', 'broke', 'bred', 'brougnt', 'broadcast', 'built', 'burnt', 'bought', 'caught', 'chose', 'clung', 'came', 'cost', 'crept', 'cut', 'dealt', 'dug', 'did', 'drew', 'dreamt', 'drank', 'drove', 'ate', 'fell', 'fed', 'felt', 'fought', 'found', 'flew', 'forbade', 'forgot', 'forgave', 'froze', 'got', 'gave', 'went', 'ground', 'grew', 'hung', 'heard', 'hid', 'hit', 'held', 'hurt', 'kept', 'knelt', 'knew', 'laid', 'led', 'learnt', 'left', 'lent', 'let', 'lay', 'lied', 'lit', 'lost', 'made', 'meant', 'met', 'mowed', 'paid', 'put', 'read', 'rode', 'rang', 'rose', 'ran', 'sawed', 'said', 'saw', 'sold', 'sent', 'sewed', 'shook', 'shed', 'shone', 'shot', 'showed', 'shrank', 'shut', 'sang', 'sank', 'sat', 'slept', 'slid', 'smelt', 'sowed', 'spoke', 'spelt', 'spent', 'spilt', 'spat', 'spread', 'stood', 'stole', 'stuck', 'stung', 'stuank', 'struck', 'swore', 'swept', 'swelled', 'swam', 'swung', 'took', 'taught', 'tore', 'told', 'thought', 'threw', 'understood', 'woke', 'wore', 'wept', 'won', 'wound', 'wrote']
        self.all_irregular_verbs_pastp = ['arisen', 'awoken', 'been', 'born', 'beaten', 'become', 'begun', 'bent', 'bet', 'bid', 'bound', 'bitten', 'bled', 'blown', 'broken', 'bred', 'brought', 'broadcast', 'built', 'burnt', 'bought', 'could', 'caught', 'chosen', 'clung', 'come', 'cost', 'crept', 'cut', 'dealt', 'dug', 'done', 'drawn', 'dreamt', 'drunk', 'driven', 'eaten', 'fallen', 'fed', 'felt', 'fought', 'found', 'flown', 'forbidden', 'forgotten', 'forgiven', 'frozen', 'got', 'given', 'gone', 'ground', 'grown', 'hung', 'had', 'heard', 'hidden', 'hit', 'held', 'hurt', 'kept', 'knelt', 'known', 'laid', 'led', 'learnt', 'left', 'lent', 'let', 'lain', 'lied', 'lit', 'lost', 'made', 'meant', 'met', 'mown/mowed', 'paid', 'put', 'read', 'ridden', 'rung', 'risen', 'run', 'sawn/sawed', 'said', 'seen', 'sold', 'sent', 'sewn/sewed', 'shaken', '', 'shed', 'shone', 'shot', 'shown', 'shrunk', 'shut', 'sung', 'sunk', 'sat', 'slept', 'slid', 'smelt', 'sown/sowed', 'spoken', 'spelt', 'spent', 'spilt', 'spat', 'spread', 'stood', 'stolen', 'stuck', 'stung', 'stunk', 'struck', 'sworn', 'swept', 'swollen/swelled', 'swum', 'swung', 'taken', 'taught', 'torn', 'told', 'thought', 'thrown', 'understood', 'woken', 'worn', 'wept', '-', 'won', 'wound', 'written']
        self.all_modal_verbs = ['have', 'be', 'can', 'may', 'shall', 'will', 'must']
        self.persons_in_sentece = ["I", "You", "He/She/It", "We", "You", "They"]
        self.get_user_input()
        self.sort_verb()
        self.grammar()        
    def get_user_input(self):
        raw_input = input(" Give a verb, a person, a time, and + or - !\n Example: walk, 2ps, past perfect continuous, + \n Your input: ")
        split_input = raw_input.split(", ")
        for part in split_input:
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
            elif part in self.allowed_mode_simorper:
                self.requested_mode_simorper = part
            elif part in self.allowed_mode_conornor:
                self.requested_mode_conornor = "continuous"
            elif part in self.allowed_positive:
                self.requested_positive = "negative"
            elif part in self.allowed_also:
                self.requested_positive = "positive"
            else:
                self.verb = part
        if not hasattr(self, "requested_simorper"):
            self.requested_mode_simorper = "simple"
        if not hasattr(self, "requested_mode_conornor"):
            self.requested_mode_conornor = "normal"
        if not hasattr(self, "requested_positive"):
            self.requested_positive = "positive"
    def grammar(self):
        if self.requested_time == "present":
            if self.requested_mode_simorper == "simple":
                if self.requested_mode_conornor == "normal":
                    if self.requested_positive == "positive":
                        print(self.person_normalizer() + " " + self.verb_object.give_present(self.requested_person))
                    elif self.requested_positive == "negative":
                        print("Not defined!")
                elif self.requested_mode_conornor == "continuous":
                    if self.requested_positive == "positive":
                        print("Not defined!")
                    elif self.requested_positive == "negative":
                        print("Not defined!")
            elif self.requested_mode_simorper == "perfect":
                if self.requested_mode_conornor == "normal":
                    if self.requested_positive == "positive":
                        print("Not defined!")
                    elif self.requested_positive == "negative":
                        print("Not defined!")
                elif self.requested_mode_conornor == "continuous":
                    if self.requested_positive == "positive":
                        print("Not defined!")
                    elif self.requested_positive == "negative":
                        print("Not defined!")
        elif self.requested_time == "past":
            if self.requested_mode_simorper == "simple":
                if self.requested_mode_conornor == "normal":
                    if self.requested_positive == "positive":
                        print(self.person_normalizer() + " " + self.verb_object.give_past_simple(self.requested_person))
                    elif self.requested_positive == "negative":
                        print("Not defined!")
                elif self.requested_mode_conornor == "continuous":
                    if self.requested_positive == "positive":
                        print("Not defined!")
                    elif self.requested_positive == "negative":
                        print("Not defined!")
            elif self.requested_mode_simorper == "perfect":
                if self.requested_mode_conornor == "normal":
                    if self.requested_positive == "positive":
                        print("Not defined!")
                    elif self.requested_positive == "negative":
                        print("Not defined!")
                elif self.requested_mode_conornor == "continuous":
                    if self.requested_positive == "positive":
                        print("Not defined!")
                    elif self.requested_positive == "negative":
                        print("Not defined!")
        elif self.requested_time == "future":
            if self.requested_mode_simorper == "simple":
                if self.requested_mode_conornor == "normal":
                    if self.requested_positive == "positive":
                        print("Not defined")
                    elif self.requested_positive == "negative":
                        print("Not defined!")
                elif self.requested_mode_conornor == "continuous":
                    if self.requested_positive == "positive":
                        print("Not defined!")
                    elif self.requested_positive == "negative":
                        print("Not defined!")
            elif self.requested_mode_simorper == "perfect":
                if self.requested_mode_conornor == "normal":
                    if self.requested_positive == "positive":
                        print("Not defined!")
                    elif self.requested_positive == "negative":
                        print("Not defined!")
                elif self.requested_mode_conornor == "continuous":
                    if self.requested_positive == "positive":
                        print("Not defined!")
                    elif self.requested_positive == "negative":
                        print("Not defined!")
        elif self.requested_time == "conditional":
            if self.requested_mode_simorper == "simple":
                if self.requested_mode_conornor == "normal":
                    if self.requested_positive == "positive":
                        print("Not defined")
                    elif self.requested_positive == "negative":
                        print("Not defined!")
                elif self.requested_mode_conornor == "continuous":
                    if self.requested_positive == "positive":
                        print("Not defined!")
                    elif self.requested_positive == "negative":
                        print("Not defined!")
            elif self.requested_mode_simorper == "perfect":
                if self.requested_mode_conornor == "normal":
                    if self.requested_positive == "positive":
                        print("Not defined!")
                    elif self.requested_positive == "negative":
                        print("Not defined!")
                elif self.requested_mode_conornor == "continuous":
                    if self.requested_positive == "positive":
                        print("Not defined!")
                    elif self.requested_positive == "negative":
                        print("Not defined!")
    def sort_verb(self):
        if self.verb in self.all_irregular_verbs:
            self.verb_object = ir.Irregular(self.verb)
        elif self.verb in self.all_modal_verbs:
            self.verb_object = md.Modal(self.verb)
        else:
            self.verb_object = rg.Regular(self.verb)
    def person_normalizer(self):
        index = self.allowed_persons.index(self.requested_person)
        return self.persons_in_sentece[index]

run = True
while run:
    main = Main()
    run_again = input("Do you want to run the program again? \n Yes / No")
    if run_again == "No":
        run = False
