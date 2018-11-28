# this is the irregular file
class Irregular():
    def __init__(self, verb):
        self.infinitive = verb
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

    def give_infinitive(self, person):
        return self.infinitive

    def give_present(self, person, negationBool):
        if person == "3ps":
            if self.infinitive[-1] == "o" or (self.infinitive[-1] == "h" and self.infinitive[-2] == "c"):
                return self.infinitive + "es"
            elif self.infinitive[-1] == "y":
                return self.infinitive + "ies"
            elif negationBool == False:
                return self.infinitive
            else:
                return self.infinitive + "s"
        else:
            return self.infinitive


def give_ing_form(self, person):
    return self.infinitive + "ing"


def give_past_simple(self, person):
    for i in range(len(self.all_irregular_verbs)):
        if self.infinitive == self.all_irregular_verbs[i]:
            return self.all_irregular_verbs_pasts[i]


def give_past_participle(self, person):
    for i in range(len(self.all_irregular_verbs)):
        if self.infinitive == self.all_irregular_verbs[i]:
            return self.all_irregular_verbs_pastp[i]