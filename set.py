from player import *
import json

with open('data/data.json', 'r') as txt:
    data = json.load(txt)

fp = Player()
fp.set_nickname(data['players'][0]['nickname'])
fp.set_health(data['players'][0]['health'])
fp.set_might(data['players'][0]['might'])
fp.set_defence(data['players'][0]['defence'])
fp.set_regen(data['players'][0]['regen'])
fp.set_lifesteal(data['players'][0]['lifesteal'])
fp.set_crit_bonus(data['players'][0]['crit bonus'])
fp.set_crit_chance(data['players'][0]['crit chance'])
fp.set_dodge_chance(data['players'][0]['dodge chance'])

sp = Player()
sp.set_nickname(data['players'][1]['nickname'])
sp.set_health(data['players'][1]['health'])
sp.set_might(data['players'][1]['might'])
sp.set_defence(data['players'][1]['defence'])
sp.set_regen(data['players'][1]['regen'])
sp.set_lifesteal(data['players'][1]['lifesteal'])
sp.set_crit_bonus(data['players'][1]['crit bonus'])
sp.set_crit_chance(data['players'][1]['crit chance'])
sp.set_dodge_chance(data['players'][1]['dodge chance'])