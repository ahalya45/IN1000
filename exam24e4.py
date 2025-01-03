class Abonnent:
    def __init__(self, subscriber_name:str, preferences:dict):
        self._subscriber_name = subscriber_name
        self._preferences = preferences
        self._started_series = {}

    def hent_preferenser(self):
        return self._preferences
    
    def sjekk_om_sett(self, name_of_series:str):
        return name_of_series in self.started_series
    
    def se_en_episode(self, the_name_of_series):
        if the_name_of_series in self._started_series:
            self._started_series[the_name_of_series] += 1
        else:
            self._started_series[the_name_of_series] = 1

class Serie:
    def __init__(self, the_name_of_series):
        self._the_name_of_series = the_name_of_series
        self._episode_in_the_series = {}
        self._tags_in_the_series = {}
        self._les_fra_fil()
    
    def _les_fra_fil(self):
        with open(self._the_name_of_series + ".txt", "r") as file:
            for linje in file:
                tags = linje.strip().split()
                for tag in tags:
                    if tag not in self._tags_in_the_series:
                        self._tags_in_the_series[tag] = 1
                    else:
                        self._tags_in_the_series[tag] += 1 
                self._episode_in_the_series[len(self._episode_in_the_series)+1] = tags
        file.close()

    def hent_serietags(self):
        seriestags_list = []
        for tag in self._tags_in_the_series:
            seriestags_list.append(tag)
        return seriestags_list
    
    def beregn_match(self, preferences):
        match = 0
        for tag in preferences:
            if tag in self._tags_in_the_series:
                match += self._tags_in_the_series[tag]* preferences[tag]
        return match

class Tjeneste:
    def __init__(self, names_of_series):
        self._series_offered_by_the_serice = {}
        self._tags_used_in_the_serivce = []
        self._subscribers = {}
        for name in names_of_series:
            new_series = Serie(name)
            self._series_offered_by_the_serice[name] = new_series
            tager = new_series.hent_serietags()
            for tag in tager:
                if tag not in self._tags_used_in_the_serivce:
                    self._tags_used_in_the_serivce.append(tag)
         

    def ny_abonnent(self, newsubscriber):
        subcriber_name = input("The subscriber name")
        preferences = {"tag":"like" or "dislike"}
        print("Please indicate your preference for each tag: 1(like), o(neutral) or -1 (dislike)")    
        for tag in self._tags_used_in_the_serivce:
            pref= input(tag+" : ")
            while pref not in ["-1", "0", "1"]:
                print("illegal value !")
                pref = input(tag + " : ")
                if pref != "0":
                    preferences[tag]= int(pref)
            self._subscribers[subcriber_name] = Abonnent(subcriber_name, preferences)

    def foreslå_serier(self, the_subscriber_name):

        subscriber = self._subscribers[the_subscriber_name]
        suggestion = []
        for seriesname in self._series_offered_by_the_serice:
            series = self._series_offered_by_the_serice[seriesname]
            match = series.beregn_match(subscriber.hent_preferenser())

