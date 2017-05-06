add = os.path.dirname(os.path.realpath(__file__))
os.chdir(add+'\Foursquare\ ')

import GTS
db.child('City').child(GTS.getCity()).child(GTS.getGlobalTimeStamp()).set(finalList)
