from player import Player
import json


with open('data/player.json', 'r') as _json:
  data = json.load(_json)

fp = Player()
sp = Player()

number_of_players = 2
players_tags = [fp, sp]

def set_data_player():
  _id = 0
  for player in players_tags:
    for x in range(0, number_of_players):
      player.set_nickname(data['players'][_id]['nickname'])
      player.set_health(data['players'][_id]['health'])
      player.set_might(data['players'][_id]['might'])
      player.set_defence(data['players'][_id]['defence'])
      player.set_regen(data['players'][_id]['regen'])
      player.set_lifesteal(data['players'][_id]['lifesteal'])
      player.set_crit_bonus(data['players'][_id]['crit bonus'])
      player.set_crit_chance(data['players'][_id]['crit chance'])
      player.set_dodge_chance(data['players'][_id]['dodge chance']) 
      player.set_armor_penetration(data['players'][_id]['armor penetration']) 
    _id = _id + 1

set_data_player()