from flask import Flask, jsonify
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Pozwala na Cross-Origin Resource Sharing

class ChampPicker:
    def __init__(self):
        self.top = ['Ornn'] #seba
        self.jg = ['Viego', 'Amumu', 'Poppy', 'Morgana', 'Diana', 'Lilia', 'Singed', 'Rammus','Udyr','Nocturne','Wukong','Gwen','Master Yi','Kayn'] #michal
        self.mid = ['Annie', 'Vex', 'Sylas','Orianna'] #filip
        self.adc1 = ['Ezreal','Brand','Swain'] #adc rudy
        self.adc2 = ['MF', 'Jinx', 'Jhin','Vayne',"Kai'Sa",'Tristana','Nilah','Varus','Caitlyn','Ashe','Twitch','Jinx',"Kog'Maw",'Zeri','Ziggs'] #adc milosz
        self.supp1 = ['Milio','Alistar', 'Braum','Rakan','Lulu','Soraka'] #supp milosz
        self.supp2 = ['Leona', 'Nautilius', 'Pyke','Zyra','Brand','Lux','Morgana','Swain','Blitzcrank','Zilean','Rakan','Karma','Amumu','Maokai','Rell','Tresh','Alistar','Neeko','Seraphine','Sona'] #supp rudy
        self.adcplayer = ['Rudy', 'Miłosz'] #wybor adc

    #losowanie postaci
    def randomizer(self):
        topnum = random.randint(0,len(self.top)-1)
        jgnum = random.randint(0,len(self.jg)-1)
        midnum = random.randint(0,len(self.mid)-1)
        adcnum1 = random.randint(0, len(self.adc1)-1)
        adcnum2 = random.randint(0, len(self.adc2)-1)
        suppnum1 = random.randint(0, len(self.supp1)-1)
        suppnum2 = random.randint(0, len(self.supp2)-1)
        adcplayernum = random.randint(0, len(self.adcplayer) -1)

        #jesli rudy to adc to milosz gra supp i odwrotnie
        if self.adcplayer[adcplayernum] == 'Rudy':
            return {
                'top': self.top[topnum],
                'jg': self.jg[jgnum],
                'mid': self.mid[midnum],
                'adc': self.adc1[adcnum1],
                'supp': self.supp1[suppnum1],
                'adcplayer': self.adcplayer[adcplayernum]
            }
        else:
            return {
                'top': self.top[topnum],
                'jg': self.jg[jgnum],
                'mid': self.mid[midnum],
                'adc': self.adc2[adcnum2],
                'supp': self.supp2[suppnum2],
                'adcplayer': self.adcplayer[adcplayernum]
            }

@app.route('/api/randomize', methods=['GET'])
def randomize():
    date_picker = ChampPicker()
    result = date_picker.randomizer()
    return jsonify(result)

if __name__ == '__main__':
    app.run()
