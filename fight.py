from set import *
from random import randint

show_fulllog = False

def fight(fp, sp):
    print('')

    # 50% to get crit chance
    crit = randint(0, fp.get_crit_chance())
    
    # 25% to get dodge chance
    dodge = randint(0, sp.get_dodge_chance())

    # got dodge
    if dodge == 0:
        print('[' + fp.get_nickname() + '] ' + sp.get_nickname() + ' dodge')

    if fp.get_health() and sp.get_health() and dodge > 0:
        # save fp.get_might() for reset after every hit
        default_might = fp.get_might()

        # got crit
        if crit == 0:    
            fp.set_might(fp.get_might() * fp.get_crit_bonus())
            print('[' + fp.get_nickname() + '] crit might: ' + str(fp.get_might()))
        else:
            print('[' + fp.get_nickname() + '] might: ' + str(fp.get_might()))
            
        print('[' + fp.get_nickname() + '] ' + sp.get_nickname() + ' health before attack: ' + str(sp.get_health()))

        if sp.get_defence() > 0:
            # get % by sp.get_defence() to get less might
            fp.set_might(int((fp.get_might() * (sp.get_defence() / 100))))

            if show_fulllog == True:
                print('[' + fp.get_nickname() + '] ' + sp.get_nickname() + ' defence: ' + str(sp.get_defence()))
                print('[' + fp.get_nickname() + '] might after ' + sp.get_nickname() + ' defence: ' + str(fp.get_might()))

        if fp.get_lifesteal() > 0:
            lifesteal = 0

            if show_fulllog == True:
                print('[' + fp.get_nickname() + '] health before lifesteal: ' + str(fp.get_health()))

            # lifesteal % can't be more than sp.get_health()
            if sp.get_health() < fp.get_might():
                lifesteal += int((sp.get_health() * (fp.get_lifesteal() / 100)))
            else:
                lifesteal += int((fp.get_might() * (fp.get_lifesteal() / 100)))

            # set health to fp.set_health() with lifesteal after a hit
            fp.set_health(fp.get_health() + lifesteal)

            if show_fulllog == True:
                print('[' + fp.get_nickname() + '] lifesteal: ' + str(lifesteal))
                print('[' + fp.get_nickname() + '] health after lifesteal: ' + str(fp.get_health()))

        # set health after fp.get_might() to get less health
        sp.set_health(sp.get_health() - fp.get_might())
        
        # reset fp.get_might() to default
        fp.set_might(default_might)

        if sp.get_health() < 0:
            sp.set_health(0)

        print('[' + fp.get_nickname() + '] ' + sp.get_nickname() + ' health after attack: ' + str(sp.get_health()))

        if sp.get_health() > 0 and sp.get_regen() > 0:
            if show_fulllog == True:
                print('[' + fp.get_nickname() + '] ' + sp.get_nickname() + ' health before regen: ' + str(sp.get_health()))
                print('[' + fp.get_nickname() + '] ' + sp.get_nickname() + ' regen: ' + str(sp.get_regen()))

            # add regen to sp.get_health()
            sp.set_health(sp.get_health() + sp.get_regen())

            if show_fulllog == True:
                print('[' + fp.get_nickname() + '] ' + sp.get_nickname() + ' health after regen: ' + str(sp.get_health()))

    if sp.get_health() == 0:
        return True