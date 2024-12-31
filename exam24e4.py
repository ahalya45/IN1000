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


         

        


