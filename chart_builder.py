'''
Chart builder function call here!
 - If you added song and want to play them, you have to add chart to them!
 - Fill in the form between ############## lines!

'''
import os, sys
########################################## Import your chart builder python file here as follows
from chart_test import Chart_Test
from chart_another_way import *
from chart_crystal import *
from chart_H2O import *
from chart_waikiki import *

# add below

##########################################


def write_chart(song_name,instance):
    APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))+'/charts/'
    full_path = os.path.join(APP_FOLDER, '%s.txt'%song_name)

    #build_method = getattr(instance, method_holding_instance.method.__name__)
    build_method = getattr(instance, instance.__class__.build_chart.__name__)
    if build_method:
        build_method(full_path)

    print("Chart updated: %s"%song_name)



chart_builder_list = []
################################################ Make instance of it and give it to the list!
# TEST = Chart_Test()
# DropsOfH2O = Chart_DropsOfH2O()
# Waikiki = Chart_Waikiki()
# AnotherWay = Chart_AnotherWay()

chart_builder_list.extend([Chart_Test(), Chart_DropsOfH2O(), Chart_Waikiki(), Chart_AnotherWay(),Chart_Crystal()])

# add below!

################################################
for cb in chart_builder_list:
    write_chart(cb.song_name,cb)

