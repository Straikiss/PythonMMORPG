class Player():
  def set_nickname(self, nickname):
    self.nickname = nickname 

  def get_nickname(self):
    return self.nickname

  def set_health(self, health):
    self.health = health
    if health > 3000:
      health = 3000
    if health < 1000:
       health = 1000

  def get_health(self):
    return self.health

  def set_might(self, might):
    self.might = might
    if might > 500:
      might = 500
    if might < 100:
      might = 100

  def get_might(self):
    return self.might

  def set_defence(self, defence):
    self.defence = defence
    if defence > 70:
      defence = 70

  def get_defence(self):
    return self.defence

  def set_regen(self, regen):
    self.regen = regen
    if regen > 50:
      regen = 50

  def get_regen(self):
    return self.regen

  def set_lifesteal(self, lifesteal):
    self.lifesteal = lifesteal
    if lifesteal > 100:
      lifesteal = 100

  def get_lifesteal(self):
    return self.lifesteal

  def set_crit_bonus(self, crit_bonus):
    self.crit_bonus = crit_bonus
    if crit_bonus > 5:
      crit_bonus = 5

  def get_crit_bonus(self):
    return self.crit_bonus

  def set_crit_chance(self, crit_chance):
    self.crit_chance = crit_chance
    if crit_chance < 1:
      crit_chance = 1

  def get_crit_chance(self):
    return self.crit_chance   

  def set_dodge_chance(self, dodge_chance):
    self.dodge_chance = dodge_chance
    if dodge_chance < 1:
      dodge_chance = 1

  def get_dodge_chance(self):
    return self.dodge_chance    

  def set_armor_penetration(self, armor_penetration):
    self.armor_penetration = armor_penetration
    if armor_penetration < 0:
      armor_penetration = 0
    if armor_penetration > 30:
      armor_penetration = 30

  def get_armor_penetration(self):
    return self.armor_penetration   