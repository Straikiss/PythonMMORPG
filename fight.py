from set import fp, sp
from random import randint
from conf import SHOW_FULLLOG


def fight(fp, sp):
  print('')

  crit = randint(0, fp.get_crit_chance())
  dodge = randint(0, sp.get_dodge_chance())

  if dodge == 0:
    print('[' + fp.get_nickname() + '] ' + sp.get_nickname() + ' dodge')

  if fp.get_health() and sp.get_health() and dodge > 0:
    # save fp.get_might() to reset after every hit
    default_might = fp.get_might()

    if crit == 0:    
      fp.set_might(fp.get_might() * fp.get_crit_bonus())
      print('[' + fp.get_nickname() + '] crit might: ' + str(fp.get_might()))
    else:
      print('[' + fp.get_nickname() + '] might: ' + str(fp.get_might()))
            
    print('[' + fp.get_nickname() + '] ' + sp.get_nickname() 
    + ' health before attack: ' + str(sp.get_health()))

    if sp.get_defence() > 0:
      if fp.get_armor_penetration() > 0:
        # save sp.get_defence() to reset after every hit
        default_defence = sp.get_defence()

        # set 2nd player defence after 1st player armor penetration
        sp.set_defence((sp.get_defence() - fp.get_armor_penetration()) / 100)           

        # set 1st player might after 2nd player defence
        fp.set_might(fp.get_might() - int(fp.get_might() * sp.get_defence()))

        # reset sp.set_defence to default
        sp.set_defence(default_defence)

        if SHOW_FULLLOG == True:
          print('[' + fp.get_nickname() + '] '  + sp.get_nickname() 
          + ' defence before armor penetration: ' + str(sp.get_defence()))
          print('[' + fp.get_nickname() + '] armor penetration: ' 
          + str(fp.get_armor_penetration()))
          print('[' + fp.get_nickname() + '] '  + sp.get_nickname() 
          + ' defence after armor penetration: ' 
          + str(sp.get_defence() - fp.get_armor_penetration()))
      else: 
        # set 1st player might after 2nd player defence
        fp.set_might(fp.get_might() - fp.get_might() * sp.get_defence() / 100)

      if SHOW_FULLLOG == True:
        print('[' + fp.get_nickname() + '] ' + sp.get_nickname() + ' defence: ' 
        + str(sp.get_defence()))
        print('[' + fp.get_nickname() + '] might after ' + sp.get_nickname() 
        + ' defence: ' + str(fp.get_might()))

    if fp.get_lifesteal() > 0:
      lifesteal = 0

      if SHOW_FULLLOG == True:
        print('[' + fp.get_nickname() + '] health before lifesteal: ' 
        + str(fp.get_health()))

      # lifesteal % can't be more than sp.get_health()
      if sp.get_health() < fp.get_might():
        lifesteal += int((sp.get_health() * (fp.get_lifesteal() / 100)))
      else:
        lifesteal += int((fp.get_might() * (fp.get_lifesteal() / 100)))

      # set health to fp.set_health() with lifesteal after a hit
      fp.set_health(fp.get_health() + lifesteal)

      if SHOW_FULLLOG == True:
        print('[' + fp.get_nickname() + '] lifesteal: ' + str(lifesteal))
        print('[' + fp.get_nickname() + '] health after lifesteal: ' 
        + str(fp.get_health()))

    # set health after fp.get_might() to get less health
    sp.set_health(sp.get_health() - fp.get_might())
        
    # reset fp.get_might() to default
    fp.set_might(default_might)

    if sp.get_health() < 0:
      sp.set_health(0)
      print('[' + fp.get_nickname() + '] ' + sp.get_nickname() 
      + ' health after attack: ' + str(sp.get_health()))

    if sp.get_health() > 0 and sp.get_regen() > 0:
      if SHOW_FULLLOG == True:
        print('[' + fp.get_nickname() + '] ' + sp.get_nickname() 
        + ' health before regen: ' + str(sp.get_health()))
        print('[' + fp.get_nickname() + '] ' + sp.get_nickname() 
        + ' regen: ' + str(sp.get_regen()))

        # add regen to sp.get_health()
        sp.set_health(sp.get_health() + sp.get_regen())

      if SHOW_FULLLOG == True:
        print('[' + fp.get_nickname() + '] ' + sp.get_nickname() 
        + ' health after regen: ' + str(sp.get_health()))

  if sp.get_health() == 0:
    return True