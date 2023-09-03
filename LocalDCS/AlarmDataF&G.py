import sqlite3

conn = sqlite3.connect('AlarmData.db')

cursor = conn.cursor()

#cursor.execute("""
#    CREATE TABLE AlarmDataFandG (
#        TagNo TEXT,
#        Description TEXT, 
#        Priority TEXT,
#        Actions TEXT, 
#        Consequences TEXT, 
#        Causes TEXT
#    )
#"""
#)
#conn.commit()

cursor.execute("""
            INSERT INTO AlarmDataFandG (TagNo ,Description, Priority, Actions, Consequences, Causes)

        VALUES
            ("EDSD1000", "East Deck Smoke Detector 1", "1", "N/A"                                       , "N/A"                         , "N/A"),
            ("EDSD1000", "East Deck Smoke Detector 1", "2", "evacuate area"                             , "risk of smoke inhalation"    , "excessive smoke detected"),
            ("EDSD1000", "East Deck Smoke Detector 1", "3", "evacuate area and shutdown production"     , "Consequences"                , "excessive smoke detected"),

            ("EDSD1001", "East Deck Smoke Detector 2", "1", "N/A"                                       , "N/A"                         , "N/A"),
            ("EDSD1001", "East Deck Smoke Detector 2", "2", "evacuate area"                             , "risk of smoke inhalation"    , "excessive smoke detected"),
            ("EDSD1001", "East Deck Smoke Detector 2", "3", "evacuate area and shutdown production"     , "Consequences"                , "excessive smoke detected"),

            ("EDSD1002", "East Deck Smoke Detector 3", "1", "N/A"                                       , "N/A"                         , "N/A"),
            ("EDSD1002", "East Deck Smoke Detector 3", "2", "evacuate area"                             , "risk of smoke inhalation"    , "excessive smoke detected"),
            ("EDSD1002", "East Deck Smoke Detector 3", "3", "evacuate area and shutdown production"     , "Consequences"                , "excessive smoke detected"),

            ("EDSD1003", "East Deck Smoke Detector 4", "1", "N/A"                                       , "N/A"                         , "N/A"),
            ("EDSD1003", "East Deck Smoke Detector 4", "2", "evacuate area"                             , "risk of smoke inhalation"    , "excessive smoke detected"),
            ("EDSD1003", "East Deck Smoke Detector 4", "3", "evacuate area and shutdown production"     , "Consequences"                , "excessive smoke detected"),

            ("EDSD1004", "East Deck Smoke Detector 5", "1", "N/A"                                       , "N/A"                         , "N/A"),
            ("EDSD1004", "East Deck Smoke Detector 5", "2", "evacuate area"                             , "risk of smoke inhalation"    , "excessive smoke detected"),
            ("EDSD1004", "East Deck Smoke Detector 5", "3", "evacuate area and shutdown production"     , "Consequences"                , "excessive smoke detected"),

            ("EDSD1005", "East Deck Smoke Detector 6", "1", "N/A"                                       , "N/A"                         , "N/A"),
            ("EDSD1005", "East Deck Smoke Detector 6", "2", "evacuate area"                             , "risk of smoke inhalation"    , "excessive smoke detected"),
            ("EDSD1005", "East Deck Smoke Detector 6", "3", "evacuate area and shutdown production"     , "Consequences"                , "excessive smoke detected"),

            ("EDSD1006", "East Deck Smoke Detector 7", "1", "N/A"                                       , "N/A"                         , "N/A"),
            ("EDSD1006", "East Deck Smoke Detector 7", "2", "evacuate area"                             , "risk of smoke inhalation"    , "excessive smoke detected"),
            ("EDSD1006", "East Deck Smoke Detector 7", "3", "evacuate area and shutdown production"     , "Consequences"                , "excessive smoke detected"),

            ("EDSD1007", "East Deck Smoke Detector 8", "1", "N/A"                                       , "N/A"                         , "N/A"),
            ("EDSD1007", "East Deck Smoke Detector 8", "2", "evacuate area"                             , "risk of smoke inhalation"    , "excessive smoke detected"),
            ("EDSD1007", "East Deck Smoke Detector 8", "3", "evacuate area and shutdown production"     , "Consequences"                , "excessive smoke detected"),

            ("EDSD1008", "East Deck Smoke Detector 9", "1", "N/A"                                       , "N/A"                         , "N/A"),
            ("EDSD1008", "East Deck Smoke Detector 9", "2", "evacuate area"                             , "risk of smoke inhalation"    , "excessive smoke detected"),
            ("EDSD1008", "East Deck Smoke Detector 9", "3", "evacuate area and shutdown production"     , "Consequences"                , "excessive smoke detected"),

            ("EDSD1009", "East Deck Smoke Detector 10", "1", "N/A"                                      , "N/A"                         , "N/A"),
            ("EDSD1009", "East Deck Smoke Detector 10", "2", "evacuate area"                            , "risk of smoke inhalation"    , "excessive smoke detected"),
            ("EDSD1009", "East Deck Smoke Detector 10", "3", "evacuate area and shutdown production"    , "Consequences"                , "excessive smoke detected"),

            ("EDFD2000", "Descrp", "1", "N/A"                                   , "Consequences"                                                , "excessive smoke detected"),
            ("EDFD2000", "Descrp", "2", "evacuate area"                         , "moderate injuries burns/ slight damage to equipment"         , "excessive heat detected"),
            ("EDFD2000", "Descrp", "3", "evacuate area and shutdown production" ,"major burns, risk of small outbreak, potential asset damage"  , "excessive heat detected"),

            ("EDFD2001", "Descrp", "1", "N/A"                                   , "Consequences"                                                , "Causes"),
            ("EDFD2001", "Descrp", "2", "evacuate area"                         , "moderate injuries burns/ slight damage to equipment"         , "excessive heat detected"),
            ("EDFD2001", "Descrp", "3", "evacuate area and shutdown production" , "major burns, risk of small outbreak, potential asset damage" , "excessive heat detected"),

            ("EDFD2002", "Descrp", "1", "N/A"                                   , "Consequences"                                                , "Causes"),
            ("EDFD2002", "Descrp", "2", "evacuate area"                         , "moderate injuries burns/ slight damage to equipment"         , "excessive heat detected"),
            ("EDFD2002", "Descrp", "3", "evacuate area and shutdown production" , "major burns, risk of small outbreak, potential asset damage" , "excessive heat detected"),

            ("EDHV3000", "Descrp", "1", "Send tech to investigate"      , "Lack of ventilation"                 , "Fault with HVAC system"),
            ("EDHV3000", "Descrp", "2", "evacuate area"                 , "risk of chemical inhalation"         , "Fault with HVAC system"),
            ("EDHV3000", "Descrp", "3", "Shutdown & evacuate area"      , "high risk of chemical inhalation"    , "Fault with HVAC system"),

            ("EDHV3001", "Descrp", "1", "Send tech to investigate"      , "Lack of ventilation"                 , "Fault with HVAC system"),
            ("EDHV3001", "Descrp", "2", "evacuate area"                 , "risk of chemical inhalation"         , "Fault with HVAC system"),
            ("EDHV3001", "Descrp", "3", "Shutdown & evacuate area"      , "high risk of chemical inhalation"    , "Fault with HVAC system")

""")
conn.commit()

conn.close()