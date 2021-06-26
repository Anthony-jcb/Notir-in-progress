from database import *
from navegacion import *
from interfaz import *


connect_database()
create_alarm()
database_alarms()
update_clock()
root.mainloop()