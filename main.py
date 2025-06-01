import obspython as obs
import urllib.request
from xml import etree

import time

# --------------------DATA------------------------------------------

HOME_PLAYER_SOURCE = "Zawodnik_1"
GUEST_PLAYER_SOURCE = "Zawodnik_2"
HOME_SETS_SOURCE = "Set_1"
GUEST_SETS_SOURCE = "Set_2"
HOME_POINTS_SOURCE = "Punkty_1"
GUEST_POINTS_SOURCE = "Punkty_2"

pkt_zawodnik_1 = 0
pkt_zawodnik_2 = 0

set_zawodnik_1 = 0
set_zawodnik_2 = 0


# --------------------Script Functions------------------------------

def script_properties():
    """
    Called to define user properties associated with the script. These
    properties are used to define how to show settings properties to a user.
    """
    props = obs.obs_properties_create()
    obs.obs_properties_add_text(props, "zawodnik_1_tekst", "zawodnik_1", obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_button(props, "zwieksz_pkt_zawodnik_1", "+ (punkty)", zwieksz_pkt_zawodnik_1)
    obs.obs_properties_add_button(props, "zmniejsz_pkt_zawodnik_1", "- (punkty)", zmniejsz_pkt_zawodnik_1)
    obs.obs_properties_add_button(props, "wyzeruj_pkt_zawodnik_1", "Wyzeruj (punkty)", wyzeruj_punkty_1)
    obs.obs_properties_add_button(props, "zwieksz_set_zawodnik_1", "+ (sety)", zwieksz_set_zawodnik_1)
    obs.obs_properties_add_button(props, "zmniejsz_set_zawodnik_1", "- (sety)", zmniejsz_set_zawodnik_1)
    obs.obs_properties_add_button(props, "wyzeruj_set_zawodnik_1", "Wyzeruj (sety)", wyzeruj_sety_1)

    obs.obs_properties_add_text(props, "zawodnik_2_tekst", "zawodnik_2", obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_button(props, "zwieksz_pkt_zawodnik_2", "+ (punkty)", zwieksz_pkt_zawodnik_2)
    obs.obs_properties_add_button(props, "zmniejsz_pkt_zawodnik_2", "- (punkty)", zmniejsz_pkt_zawodnik_2)
    obs.obs_properties_add_button(props, "wyzeruj_pkt_zawodnik_2", "Wyzeruj (punkty)", wyzeruj_punkty_2)
    obs.obs_properties_add_button(props, "zwieksz_set_zawodnik_2", "+ (sety)", zwieksz_set_zawodnik_2)
    obs.obs_properties_add_button(props, "zmniejsz_set_zawodnik_2", "- (sety)", zmniejsz_set_zawodnik_2)
    obs.obs_properties_add_button(props, "wyzeruj_set_zawodnik_2", "Wyzeruj (sety)", wyzeruj_sety_2)
    return props
# --------------------------------------------------------------

# --------------------Zawodnik 1 ------------------------------
def zwieksz_pkt_zawodnik_1(props, prop):
    global pkt_zawodnik_1
    pkt_zawodnik_1=pkt_zawodnik_1+1
    update_text_gui(HOME_POINTS_SOURCE, pkt_zawodnik_1)
    

def zmniejsz_pkt_zawodnik_1(props, prop):
    global pkt_zawodnik_1
    pkt_zawodnik_1=pkt_zawodnik_1-1
    update_text_gui(HOME_POINTS_SOURCE, pkt_zawodnik_1)
    

def wyzeruj_punkty_1(props, prop):
    global pkt_zawodnik_1
    pkt_zawodnik_1=0
    update_text_gui(HOME_POINTS_SOURCE, pkt_zawodnik_1)
    

def zwieksz_set_zawodnik_1(props, prop):
    global set_zawodnik_1
    set_zawodnik_1=set_zawodnik_1+1
    update_text_gui(HOME_SETS_SOURCE, set_zawodnik_1)
    

def zmniejsz_set_zawodnik_1(props, prop):
    global set_zawodnik_1
    set_zawodnik_1=set_zawodnik_1-1
    update_text_gui(HOME_SETS_SOURCE, set_zawodnik_1)
    

def wyzeruj_sety_1(props, prop):
    global set_zawodnik_1
    set_zawodnik_1=0
    update_text_gui(HOME_SETS_SOURCE, set_zawodnik_1)
    
# --------------------------------------------------------------


# --------------------Zawodnik 2 ------------------------------
def zwieksz_pkt_zawodnik_2(props, prop):
    global pkt_zawodnik_2
    pkt_zawodnik_2=pkt_zawodnik_2+1
    update_text_gui(GUEST_POINTS_SOURCE, pkt_zawodnik_2)
    

def zmniejsz_pkt_zawodnik_2(props, prop):
    global pkt_zawodnik_2
    pkt_zawodnik_2=pkt_zawodnik_2-1
    update_text_gui(GUEST_POINTS_SOURCE, pkt_zawodnik_2)
    

def wyzeruj_punkty_2(props, prop):
    global pkt_zawodnik_2
    pkt_zawodnik_2=0
    update_text_gui(GUEST_POINTS_SOURCE, pkt_zawodnik_2)
    

def zwieksz_set_zawodnik_2(props, prop):
    global set_zawodnik_2
    set_zawodnik_2=set_zawodnik_2+1
    update_text_gui(GUEST_SETS_SOURCE, set_zawodnik_2)
    

def zmniejsz_set_zawodnik_2(props, prop):
    global set_zawodnik_2
    set_zawodnik_2=set_zawodnik_2-1
    update_text_gui(GUEST_SETS_SOURCE, set_zawodnik_2)
    

def wyzeruj_sety_2(props, prop):
    global set_zawodnik_2
    set_zawodnik_2=0
    update_text_gui(GUEST_SETS_SOURCE, set_zawodnik_2)
    
# --------------------------------------------------------------



# --------------------Functions--------------------------------------
def update_text_gui(source, text):
    source = obs.obs_get_source_by_name(source)
    if source is not None:
        settings = obs.obs_data_create()
        obs.obs_data_set_string(settings, "text", str(text))  # <- konwersja na string
        obs.obs_source_update(source, settings)
        obs.obs_data_release(settings)
        obs.obs_source_release(source)