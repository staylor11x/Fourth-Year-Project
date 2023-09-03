import sqlite3

conn = sqlite3.connect('AlarmData.db')

cursor = conn.cursor()

#create table 

cursor.execute("""
    CREATE TABLE AlarmData (
        TagNo TEXT,
        Description TEXT,
        TripLvl TEXT,
        Actions TEXT, 
        Consequences TEXT, 
        Causes TEXT
    )
"""
)

#commit the transaction
conn.commit()

#close the connection
#conn.close()

#add values
cursor.execute("""
        INSERT INTO AlarmData (TagNo, Description, TripLvl, Actions, Consequences, Causes)

    VALUES
        ("LDTT2000", "Lower Deck Temperature Sensor Valve1"     , "LL"  ,"Dispatch Technitian to investigate",              "loss of production"        , "input temp too low"),
        ("LDTT2000", "Lower Deck Temperature Sensor Valve1"     , "L"   ,"Increase temperature",                            "Production out of spec"    , "input temp too low"),
        ("LDTT2000", "Lower Deck Temperature Sensor Valve1"     , "H"   ,"decrease temp",                                   "Production out of spec"    , "input temp too high"),
        ("LDTT2000", "Lower Deck Temperature Sensor Valve1"     , "HH"  ,"Isolate Module, dispatch tech to investigate",    "Damage to asset"           , "input temp too high"),

        ("LDPT2000", "Lower Deck Pressure Transmitter Valve1"   , "LL"  ,"increase input pressure "                         , "loss of production"                                          , "input pressure too low"),
        ("LDPT2000", "Lower Deck Pressure Transmitter Valve1"   , "L"   ,"increase input pressure "                         , "Production out of spec"                                      , "Input pressure too low"),
        ("LDPT2000", "Lower Deck Pressure Transmitter Valve1"   , "H"   ,"decrease input pressure"                          , "Production out of spec"                                      , "Input pressure too high"),
        ("LDPT2000", "Lower Deck Pressure Transmitter Valve1"   , "HH"  ,"isolate module, dispatch tech to investigate"     , "damage to asset, possible flaring event, loss of production" , "Input pressure too high"),

        ("LDTT2001", "Lower Deck Temperature Sensor Valve2"     , "LL"  ,"Dispatch Technitian to investigate",              "loss of production"        , "input temp too low"),
        ("LDTT2001", "Lower Deck Temperature Sensor Valve2"     , "L"   ,"Increase temperature",                            "Production out of spec"    , "input temp too low"),
        ("LDTT2001", "Lower Deck Temperature Sensor Valve2"     , "H"   ,"decrease temp",                                   "Production out of spec"    , "input temp too high "),
        ("LDTT2001", "Lower Deck Temperature Sensor Valve2"     , "HH"  ,"Isolate Module, dispatch tech to investigate",    "Damage to asset"           , "input temp too high "),

        ("LDPT2001", "Lower Deck Pressure Transmitetr Valve2"   , "LL"  ,"increase input pressure "                         , "loss of production"                                          , "input pressure too low"),
        ("LDPT2001", "Lower Deck Pressure Transmitetr Valve2"   , "L"   ,"increase input pressure "                         , "Production out of spec"                                      , "Input pressure too low"),
        ("LDPT2001", "Lower Deck Pressure Transmitetr Valve2"   , "H"   ,"decrease input pressure"                          , "Production out of spec"                                      , "Input pressure too high"),
        ("LDPT2001", "Lower Deck Pressure Transmitetr Valve2"   , "HH"  ,"isolate module, dispatch tech to investigate"     , "damage to asset, possible flaring event, loss of production" , "Input pressure too high"),

        ("LDTT2002", "Lower Deck Temperature Sensor Valve3"     , "LL"  ,"Dispatch Technitian to investigate",              "loss of production"        , "input temp too low"),
        ("LDTT2002", "Lower Deck Temperature Sensor Valve3"     , "L"   ,"Increase temperature",                            "Production out of spec"    , "input temp too low"),
        ("LDTT2002", "Lower Deck Temperature Sensor Valve3"     , "H"   ,"decrease temp",                                   "Production out of spec"    , "input temp too high "),
        ("LDTT2002", "Lower Deck Temperature Sensor Valve3"     , "HH"  ,"Isolate Module, dispatch tech to investigate",    "Damage to asset"           , "input temp too high "),

        ("LDPT2002", "Lower Deck Pressure Transmitetr Valve3"   , "LL"  ,"increase input pressure "                         , "loss of production"                                          , "input pressure too low"),
        ("LDPT2002", "Lower Deck Pressure Transmitetr Valve3"   , "L"   ,"increase input pressure "                         , "Production out of spec"                                      , "Input pressure too low"),
        ("LDPT2002", "Lower Deck Pressure Transmitetr Valve3"   , "H"   ,"decrease input pressure"                          , "Production out of spec"                                      , "Input pressure too high"),
        ("LDPT2002", "Lower Deck Pressure Transmitetr Valve3"   , "HH"  ,"isolate module, dispatch tech to investigate"     , "damage to asset, possible flaring event, loss of production" , "Input pressure too high"),

        ("LDTT2003", "Lower Deck Temperature Sensor Valve4"     , "LL"  ,"Dispatch Technitian to investigate",              "loss of production"        , "input temp too low"),
        ("LDTT2003", "Lower Deck Temperature Sensor Valve4"     , "L"   ,"Increase temperature",                            "Production out of spec"    , "input temp too low"),
        ("LDTT2003", "Lower Deck Temperature Sensor Valve4"     , "H"   ,"decrease temp",                                   "Production out of spec"    , "input temp too high "),
        ("LDTT2003", "Lower Deck Temperature Sensor Valve4"     , "HH"  ,"Isolate Module, dispatch tech to investigate",    "Damage to asset"           , "input temp too high "),

        ("LDPT2003", "Lower Deck Pressure Transmitetr Valve4"   , "LL"  ,"increase input pressure "                         , "loss of production"                                          , "input pressure too low"),
        ("LDPT2003", "Lower Deck Pressure Transmitetr Valve4"   , "L"   ,"increase input pressure "                         , "Production out of spec"                                      , "Input pressure too low"),
        ("LDPT2003", "Lower Deck Pressure Transmitetr Valve4"   , "H"   ,"decrease input pressure"                          , "Production out of spec"                                      , "Input pressure too high"),
        ("LDPT2003", "Lower Deck Pressure Transmitetr Valve4"   , "HH"  ,"isolate module, dispatch tech to investigate"     , "damage to asset, possible flaring event, loss of production" , "Input pressure too high"),

        ("LDTT1000", "Lower Deck Temperature Sensor Vessel1"    ,"LL"   ,"isolate module, dispatch tech to investigate "    , "loss of production, production out of spec "         , "temperature too low "),
        ("LDTT1000", "Lower Deck Temperature Sensor Vessel1"    ,"L"    ,"Dispatch tech to investigate "                    , "Production out of spec "                             , "temperature too low "),
        ("LDTT1000", "Lower Deck Temperature Sensor Vessel1"    ,"H"    ,"Dispatch tech to investigate "                    , "loss of production "                                 , "temperature too high "),
        ("LDTT1000", "Lower Deck Temperature Sensor Vessel1"    ,"HH"   ,"isolate module, dispatch tech to investigate "    , "loss of production, production out of spec "         , "temperature too high "),

        ("LDPT1000", "Lower Deck Pressure Transmitter Vessel1"  ,"LL" ,"Dispatch tech to investigate "                          , "loss of production "                                                         , "pressure too low "),
        ("LDPT1000", "Lower Deck Pressure Transmitter Vessel1"  ,"L"  ,"Increase input pressure, Dispatch tech to investigate " , "loss of production "                                                         , "pressure too low "),
        ("LDPT1000", "Lower Deck Pressure Transmitter Vessel1"  ,"H"  ,"Reduce input pressure, Dispatch tech to investigate "   , "loss of production, risk of damage to asset "                                , "pressure too high  "),
        ("LDPT1000", "Lower Deck Pressure Transmitter Vessel1"  ,"HH" ,"Automatic Plant Shutdown "                              , "loss of production, damage to asset, damage to environment, loss of life "   , "pressure too high  "),

        ("LDLT1000", "Lower Deck Level Transmitter Vessel1"     ,"LL" ,"increase flow, dispatch tech to investigate "           , "Large loss of production "                                                   , "level too low "),
        ("LDLT1000", "Lower Deck Level Transmitter Vessel1"     ,"L"  ,"increase flow  "                                        , "loss of production "                                                         , "level too low "),
        ("LDLT1000", "Lower Deck Level Transmitter Vessel1"     ,"H"  ,"decrease input flow, dispatch tech to investigate "     , "loss of production, risk of damage to asset "                                , "level too high "),
        ("LDLT1000", "Lower Deck Level Transmitter Vessel1"     ,"HH" ,"Automatic Plant Shutdown "                              , "loss of production, damage to asset, damage to environment, loss of life "   , "level too high "),

        ("LDTT1001", "Lower Deck Temperature Sensor Vessel2"    ,"LL"   ,"isolate module, dispatch tech to investigate "    , "loss of production, production out of spec "         , "temperature too low "),
        ("LDTT1001", "Lower Deck Temperature Sensor Vessel2"    ,"L"    ,"Dispatch tech to investigate "                    , "Production out of spec "                             , "temperature too low "),
        ("LDTT1001", "Lower Deck Temperature Sensor Vessel2"    ,"H"    ,"Dispatch tech to investigate "                    , "loss of production "                                 , "temperature too high "),
        ("LDTT1001", "Lower Deck Temperature Sensor Vessel2"    ,"HH"   ,"isolate module, dispatch tech to investigate "    , "loss of production, production out of spec "         , "temperature too high "),

        ("LDPT1001", "Lower Deck Pressure Transmitter Vessel2"  ,"LL" ,"Dispatch tech to investigate "                          , "loss of production "                                                         , "pressure too low "),
        ("LDPT1001", "Lower Deck Pressure Transmitter Vessel2"  ,"L"  ,"Increase input pressure, Dispatch tech to investigate " , "loss of production "                                                         , "pressure too low "),
        ("LDPT1001", "Lower Deck Pressure Transmitter Vessel2"  ,"H"  ,"Reduce input pressure, Dispatch tech to investigate "   , "loss of production, risk of damage to asset "                                , "pressure too high  "),
        ("LDPT1001", "Lower Deck Pressure Transmitter Vessel2"  ,"HH" ,"Automatic Plant Shutdown "                              , "loss of production, damage to asset, damage to environment, loss of life "   , "pressure too high  "),

        ("LDLT1001", "Lower Deck Level Transmitter Vessel2"     ,"LL" ,"increase flow, dispatch tech to investigate "           , "Large loss of production "                                                   , "level too low "),
        ("LDLT1001", "Lower Deck Level Transmitter Vessel2"     ,"L"  ,"increase flow  "                                        , "loss of production "                                                         , "level too low "),
        ("LDLT1001", "Lower Deck Level Transmitter Vessel2"     ,"H"  ,"decrease input flow, dispatch tech to investigate "     , "loss of production, risk of damage to asset "                                , "level too high "),
        ("LDLT1001", "Lower Deck Level Transmitter Vessel2"     ,"HH" ,"Automatic Plant Shutdown "                              , "loss of production, damage to asset, damage to environment, loss of life "   , "level too high "),

        ("LDTT3000", "Lower Deck Temperature Sensor Pump1"      ,"LL" ,"Increase input temperature, Dispatch tech to investigate"   ,"loss of production, damage to asset "             , "temperature too low "),
        ("LDTT3000", "Lower Deck Temperature Sensor Pump1"      ,"L"  ,"increase input temperature "                                , "loss of production, risk of damage to asset "    , "temperature too low "),
        ("LDTT3000", "Lower Deck Temperature Sensor Pump1"      ,"H"  ,"decrease input temperature "                                , "loss of production, risk of damage to asset "    , "temperature too high "),
        ("LDTT3000", "Lower Deck Temperature Sensor Pump1"      ,"HH" ,"decrease input temperature "                                , "loss of production, damage to asset "            , "temperature too high "),

        ("LDPT3000", "Lower Deck Pressure Transmitter Pump1"    ,"LL" ,"isolate module, dispatch tech to investigate "  , "loss of production, damage to asset "                                            , "pressure too low "),
        ("LDPT3000", "Lower Deck Pressure Transmitter Pump1"    ,"L"  ,"increase input pressure "                       , "loss of production "                                                             , "pressure too low "),
        ("LDPT3000", "Lower Deck Pressure Transmitter Pump1"    ,"H"  ,"decrease input pressure "                       , "loss of production "                                                             , "pressure too high  "),
        ("LDPT3000", "Lower Deck Pressure Transmitter Pump1"    ,"HH" ,"Automatic Plant Shutdown "                      , "loss of production, damage to asset, damage to environment, loss of life "       , "pressure too high  ")
   
    """)
conn.commit()
conn.close()
#
## define search parameters
#param1 = "LDPT3000"
#aram2 = "HH"
#cursor.execute("SELECT * FROM AlarmData WHERE TagNo=? AND TripLvl=?", (param1, param2))
#
#
##fetch the results
#results = cursor.fetchone()
#
##print the results
#print(results[3])

conn.close()

