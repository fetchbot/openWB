#!/usr/bin/env
import sys



leaftimer = open('/var/www/html/openWB/ramdisk/soctimer', 'r')
leaftimer = int(leaftimer.read())

if ( leaftimer < 60 ):
    leaftimer += 1
    f = open('/var/www/html/openWB/ramdisk/soctimer', 'w')
    f.write(str(leaftimer))
    f.close()

else:
    from leaf import Leaf
    leaf = Leaf(sys.argv[1], sys.argv[2])
    socit = leaf.BatteryStatusRecordsRequest()
    justsoc = socit['BatteryStatusRecords']['BatteryStatus']['SOC']['Value']
    f = open('/var/www/html/openWB/ramdisk/soc', 'w')
    f.write(str(justsoc))
    f.close()
    f = open('/var/www/html/openWB/ramdisk/soctimer', 'w')
    f.write(str(0))
    f.close()

    
    


