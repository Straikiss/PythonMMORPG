from fight import fp, sp, fight
from conf import STOP_PROGRAM


while STOP_PROGRAM != True:
  if fight(fp, sp) == True or fight(sp, fp) == True:
    STOP_PROGRAM = True
    
if fp.get_health() > sp.get_health():
  print('\n' + '[' + fp.get_nickname() + '] victory with ' 
  + str(fp.get_health()) + ' health')
else:
  print('\n' + '['  + sp.get_nickname() + '] victory with ' 
  + str(sp.get_health()) + ' health')