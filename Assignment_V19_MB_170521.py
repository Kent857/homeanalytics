import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

#read the data and preprocess it
data = pd.read_csv("elecrData.csv")
data["time"] = pd.to_datetime(data["time"], format="%Y/%m/%d")
data.sort_values("time", inplace=True)
data_power = data.dropna(subset=['power'])
data_vrms= data.dropna(subset=['vrms'])

data_weather = pd.read_csv("weatherData.csv")
data_weather["time"] = pd.to_datetime(data_weather["time"], format="%Y/%m/%d")
data_weather.sort_values("time", inplace=True)
data_weather_garage = data_weather.loc[data_weather['location']=='garage']
data_weather_meterBox = data_weather.loc[data_weather['location']=='meter_box']
data_weather_tempest1 = data_weather.loc[data_weather['location']=='tempest']
data_weather_tempest1= data_weather_tempest1.dropna(subset=['air_temperature'])
data_weather_tempest2 = data_weather.loc[data_weather['location']=='tempest']
data_weather_tempest2= data_weather_tempest2.dropna(subset=['direction'])
data_weather_windAvg = data_weather.dropna(subset=['wind_avg'])
data_weather_windGust = data_weather.dropna(subset=['wind_gust'])
data_weather_tempest3 = data_weather.loc[data_weather['location']=='tempest']
data_weather_tempest3= data_weather_tempest3.dropna(subset=['relative_humidity'])
data_weather_garage1 = data_weather.loc[data_weather['location']=='garage']
data_weather_garage = data_weather.dropna(subset=['relative_humidity'])
data_weather_Solar = data_weather.dropna(subset=['solar_radiation'])

data_pool = pd.read_csv("poolData.csv")
data_pool["time"] = pd.to_datetime(data_pool["time"], format="%Y/%m/%d")
data_pool.sort_values("time", inplace=True)
data_pool_temp = data_pool.dropna(subset=['water_temperature'])
data_pool_pH_ORV = data_pool.dropna(subset=['pH'])
data_pool_ORP = data_pool.dropna(subset=['ORPmV'])

data_tank = pd.read_csv("Water_TankData.csv")
data_tank["time"] = pd.to_datetime(data_tank["time"], format="%Y/%m/%d")
data_tank.sort_values("time", inplace=True)

data_station = pd.read_csv("weatherStationData.csv")
data_station["time"] = pd.to_datetime(data_station["time"], format="%Y/%m/%d")
data_station.sort_values("time", inplace=True)
data_station_temp = data_station.loc[data_station['location']=='tempest']

data_water_meter= pd.read_csv("Water_MeterData.csv")
data_water_meter["time"] = pd.to_datetime(data_water_meter["time"], format= "%Y/%m/%d")
data_water_meter.sort_values("time", inplace=True)

data_security = pd.read_csv("securityData.csv")
data_security["time"] = pd.to_datetime(data_security["time"], format="%Y/%m/%d")
data_security.sort_values("time", inplace=True)
#note: need to double check the security files to check all locations are listed
data_security_bathroom= data_security[data_security.zone_desc == 'Bathroom']
data_security_cabana= data_security[data_security.zone_desc == 'Cabana']
data_security_cabana_NE = data_security[data_security.zone_desc =='Cabana_North_East_Door']
data_security_cabana_SE = data_security[data_security.zone_desc =='Cabana_South_East_Door']
data_security_conservatory= data_security[data_security.zone_desc == 'Conservatory']
data_security_deck= data_security[data_security.zone_desc == 'Deck']
data_security_entryHall= data_security[data_security.zone_desc == 'Entry_Hallway']
data_security_floorSpace= data_security[data_security.zone_desc == 'Floor_Space']
data_security_frontGate = data_security[data_security.zone_desc == 'Front_Gate']
data_security_frontPorch = data_security[data_security.zone_desc == 'Front_Porch']
data_security_garage = data_security[data_security.zone_desc == 'Garage']
data_security_guestBath = data_security[data_security.zone_desc == 'Guest_Bathroom']
data_security_guestBed = data_security[data_security.zone_desc == 'Guest_Bedroom']
data_security_katieBed = data_security[data_security.zone_desc == 'Katie_Bedroom']
data_security_kitchen = data_security[data_security.zone_desc == 'Kitchen']
data_security_laundry = data_security[data_security.zone_desc == 'Laundry']
data_security_lPantry = data_security[data_security.zone_desc == 'Left_Pantry_Door']
data_security_living = data_security[data_security.zone_desc == 'Living_Room']
data_security_lowHall = data_security[data_security.zone_desc == 'Lower_Hallway']
data_security_mainBed = data_security[data_security.zone_desc == 'Main_Bedroom']
data_security_net = data_security[data_security.zone_desc == 'Network_Room']
data_security_powder = data_security[data_security.zone_desc == 'Powder_Room']
data_security_rain = data_security[data_security.zone_desc == 'Rain_Sensor']
data_security_rPantry = data_security[data_security.zone_desc == 'Right_Pantry_Door']
data_security_rumpus = data_security[data_security.zone_desc == 'Rumpus_Room']
data_security_sam = data_security[data_security.zone_desc == 'Sam_Bedroom']
data_security_PathSE = data_security[data_security.zone_desc == 'South_East_Path']
data_security_porchS = data_security[data_security.zone_desc == 'South_Porch']
data_security_study = data_security[data_security.zone_desc == 'Study']
data_security_upperHall = data_security[data_security.zone_desc == 'Upper_Hallway']
data_security_wine = data_security[data_security.zone_desc == 'Wine_Cellar']
data_security_pool = data_security[data_security.zone == 45] #zone_desc was blank so used numerical identifier

data_lighting = pd.read_csv("lightingData.csv")
data_lighting["time"] = pd.to_datetime(data_lighting["time"], format="%Y/%m/%d")
data_lighting.sort_values("time", inplace=True)
#note: need to double check the security files to check all locations are listed
data_lighting_BalconyBlind = data_lighting[data_lighting.group_desc == 'Balcony_Blind']
data_lighting_Balcony = data_lighting[data_lighting.group_desc == 'Balcony_Lights']
data_lighting_BalconyUp = data_lighting[data_lighting.group_desc == 'Balcony_Uplights']
data_lighting_BathroomDown = data_lighting[data_lighting.group_desc == 'Bathroom_Downlights']
data_lighting_BathroomFan = data_lighting[data_lighting.group_desc == 'Bathroom_Fan']
data_lighting_BathroomHeat = data_lighting[data_lighting.group_desc == 'Bathroom_Heat_Light']
data_lighting_BathroomTowel = data_lighting[data_lighting.group_desc == 'Bathroom_Towel_Rail']
data_lighting_Christmas = data_lighting[data_lighting.group_desc == 'Christmas_Lights']
data_lighting_ConservatoryDown = data_lighting[data_lighting.group_desc == 'Conservatory_Downlights']
data_lighting_DeckBlind = data_lighting[data_lighting.group_desc == 'Deck_Blind']
data_lighting_Deck = data_lighting[data_lighting.group_desc == 'Deck_Lights']
data_lighting_DiningTable = data_lighting[data_lighting.group_desc == 'Dining_Table_Downlights']
data_lighting_EastSpot = data_lighting[data_lighting.group_desc == 'East_Spotlights']
data_lighting_EastUp = data_lighting[data_lighting.group_desc == 'East_Up_Lights']
data_lighting_EastUp = data_lighting[data_lighting.group_desc == 'East_Up_Lights']
data_lighting_EnsuiteDown = data_lighting[data_lighting.group_desc == 'Ensuite_Downlights']
data_lighting_EnsuiteFan = data_lighting[data_lighting.group_desc == 'Ensuite_Fan']
data_lighting_EnsuiteTowel = data_lighting[data_lighting.group_desc == 'Ensuite_Towel_Rail']
data_lighting_FloorSpace = data_lighting[data_lighting.group_desc == 'Floor_Space_Lights']
data_lighting_FrontDoor = data_lighting[data_lighting.group_desc == 'Front_Door_Light']
data_lighting_GarageExternal = data_lighting[data_lighting.group_desc == 'Garage_External_Lights']
data_lighting_Garage = data_lighting[data_lighting.group_desc == 'Garage_Light']
data_lighting_Garden1 = data_lighting[data_lighting.group_desc == 'Garden_Lights_1']
data_lighting_Garden2 = data_lighting[data_lighting.group_desc == 'Garden_Lights_2']
data_lighting_GuestBathroomDown = data_lighting[data_lighting.group_desc == 'Guest_Bathroom_Downlight']
data_lighting_GuestBathroomFan = data_lighting[data_lighting.group_desc == 'Guest_Bathroom_Fan']
data_lighting_GuestBathroom = data_lighting[data_lighting.group_desc == 'Guest_Bathroom_Light']
data_lighting_IslandBenchStrip = data_lighting[data_lighting.group_desc == 'Island_Bench_Strip_Light']
data_lighting_KateBedroomFan = data_lighting[data_lighting.group_desc == 'Kate_Bedroom_Fan']
data_lighting_KateBedroom = data_lighting[data_lighting.group_desc == 'Kate_Bedroom_Light']
data_lighting_KitchenPendant = data_lighting[data_lighting.group_desc == 'Kitchen_Pendant_Lights']
data_lighting_KitchenDown = data_lighting[data_lighting.group_desc == 'Kitchen_Downlights']
data_lighting_KitchenStrip = data_lighting[data_lighting.group_desc == 'Kitchen_Strip_Light']
data_lighting_LaundryDown = data_lighting[data_lighting.group_desc == 'Laundry_Downlights']
data_lighting_LeftPantry = data_lighting[data_lighting.group_desc == 'Left_Pantry_Light']
data_lighting_Subfloor = data_lighting[data_lighting.group_desc == 'MF_Subfloor_Fan']
data_lighting_NetworkRoom = data_lighting[data_lighting.group_desc == 'Network_Room_Downlight']
data_lighting_NorthWest = data_lighting[data_lighting.group_desc == 'North_West_Downlights']
data_lighting_PlantRoom = data_lighting[data_lighting.group_desc == 'Plant_Room_Lights']
data_lighting_PlantRoomFan = data_lighting[data_lighting.group_desc == 'Plant_Room_Subfloor_Fan']
data_lighting_PlantRoomVoid = data_lighting[data_lighting.group_desc == 'Plant_Room_Void_Lights']
data_lighting_powerRoomDown = data_lighting[data_lighting.group_desc == 'Power_Room_Downlight']
data_lighting_powerFan = data_lighting[data_lighting.group_desc == 'Powder_Room_Fan']
data_lighting_rightPantry = data_lighting[data_lighting.group_desc == 'Right_Pantry_Light']
data_lighting_RumpusWest = data_lighting[data_lighting.group_desc == 'Rumpus_West_Downlights']
data_lighting_SamBedroomFan = data_lighting[data_lighting.group_desc == 'Sam_Bedroom_Fan']
data_lighting_SamBedroom = data_lighting[data_lighting.group_desc == 'Sam_Bedroom_Light']
data_lighting_SouthEast = data_lighting[data_lighting.group_desc == 'South_East_Spotlight']
data_lighting_SouthPorch = data_lighting[data_lighting.group_desc == 'South_Porch_Lights']
data_lighting_StudyDown = data_lighting[data_lighting.group_desc == 'Study_Downlights']
data_lighting_TomBedroomFan = data_lighting[data_lighting.group_desc == 'Tom_Bedroom_Fan']
data_lighting_TomeBedroom = data_lighting[data_lighting.group_desc == 'Tom_Bedroom_Light']
data_lighting_UpperHallwayDown = data_lighting[data_lighting.group_desc == 'Upper_Hallway_Downlights']
data_lighting_UpperHallwayFloor = data_lighting[data_lighting.group_desc == 'Upper_Hallway_Floor_Lights']
data_lighting_UpperStair = data_lighting[data_lighting.group_desc == 'Upper_Stair_Lights']
data_lighting_UpperStairPendant = data_lighting[data_lighting.group_desc == 'Upper_Stair_Pendant_Lights']
data_lighting_WalkInRobe = data_lighting[data_lighting.group_desc == 'Walk_In_Robe_Light']
data_lighting_WestSpot = data_lighting[data_lighting.group_desc == 'West_Spotlights']
data_lighting_WineCellar = data_lighting[data_lighting.group_desc == 'Wine_Cellar_Downlights']


#create an instance of the Dash class
app = dash.Dash(__name__)
server=app.server

app.layout = html.Div(children=[

#Row 1
    html.Div([
        #Column 1 (1/1)
        html.Div([
            html.H1(children='Home IOT data Analytics'),
            ]),
    ],className="rowHeading"),
#Row 2
    html.Div([
        #Column 1 (1/1)
        html.Div([
            html.H2(children = 'Welcome Glenn!'),
        ]),
    ],className="row"),

#Graph Section:
#Row 3
    html.Div([
        #Column 1 (1/1)
        html.Div([
            html.H3(children='Graphs'),
        ]),
    ],className="row"),

#Row 4
    html.Div([
        #Column 1(1/1)
        html.Div([
            html.Label(children='Select Desired Graphs',)
        ]),
    ],className="row column"),

# Row 5
    html.Div([
        #Column 1(1/1)
        html.Div([
            dcc.Dropdown(
                id = 'graph_selector',
                options=[
                    {'label': 'Electricity - Power', 'value': 'Elec_Pow'},
                    {'label': 'Tempest - Air Temperature', 'value': 'Temp_Air'},
                    {'label': 'Tempest - Relative Humidity ', 'value': 'Temp_Hum'},
                    {'label': 'Garage - Relative Humidity ', 'value': 'Gar_Hum'},
                    {'label': 'Garage - Air Temperature', 'value': 'Gar_Air'},
                    {'label': 'Meter Box - Air Temperature', 'value': 'MB_Air'},
                    {'label': 'Solar Radiation', 'value': 'Solar_Rad'},
                    {'label': 'Wind Direction', 'value': 'Wind_Dir'},
                    {'label': 'Wind Average ', 'value': 'Wind_Avg'},
                    {'label': 'Wind Gust ', 'value': 'Wind_Gust'},
                    {'label': 'Tempest - Voltage','value': 'Temp_Vol'},
                    {'label': 'Water Tank','value': 'Water_Tank'},
                    {'label': 'Water Meters','value': 'Water_Meter'},
                    {'label': 'Pool - ORP', 'value': 'Pool_ORP'},
                    {'label': 'Pool - Water Temperature', 'value': 'Pool_Temp'}

                ],
            value = 'Elec_Pow',
            placeholder="choice",
            multi=False,
            clearable= False
            )
        ]),
    ],className="row column"),
#Row 6
    html.Div([
        #Column (1/1)
        html.Div([
            dcc.Graph(id='data_graph', className='columnGraph')
        ],className="row column"),
    ]),

#Statistics
#Row 7
    html.Div([
        html.H3(children='Statistical Analysis')
    ],className="row"),

#Row 8
    html.Div([
        html.Table([
            html.Tr([html.Th('Mean'),html.Th('Sum'), html.Th('Max'),html.Th('Min'),html.Th('Median'),
                    html.Th('Number of data points'),html.Th('Standard Variation'), html.Th('Variance')]),
            html.Tr([html.Td(id='mean'),html.Td(id='sum'),html.Td(id='max'),html.Td(id='min'),html.Td(id='median'),
                     html.Td(id='count'),html.Td(id='std'), html.Td(id='var')]),
        ])
    ],className="row column"),

#Reading section

#Row 7+1
    html.Div([
        # Column 1 (1/1)
        html.Div([
            html.H3(children='Latest Readings'),
         ]),
    ],className="row"),

#Row 8
    html.Div([
        #Column 1 (1/3)
        html.Div([
            html.H4(children='Electricity'),
            html.P(children='    Time'),
            html.P(id='Power_latest_readings',
                   children='    ' + str(data_power.iloc[-1][1]) + '    Power=' + str(data_power.iloc[-1][2]) +
                            '\n    ' + str(data_vrms.iloc[-1][1]) + '     VRMs=' + str(data_vrms.iloc[-1][3]),
                   style={'white-space': 'pre'}),
            html.H4(children='Weather'),
            html.H5(children='Garage'),
            html.P(children='    Time'),
            html.P(id='Weather_Garage_latest_readings',
                   children='    ' + str(data_weather_garage.iloc[-1][1]) + '    Air Temperature=' + str(data_weather_garage.iloc[-1][2]) +
                            '\n    ' + str(data_weather_garage.iloc[-1][1]) + '     Relative Humidity=' + str(data_weather_garage.iloc[-1][15]),
                   style={'white-space': 'pre'}),
            html.H5(children='Meter Box'),
            html.P(children='    Time'),
            html.P(id='Weather_meterBox_latest_readings',
                   children='    ' + str(data_weather_meterBox.iloc[-1][1]) + '    Air Temperature=' + str(data_weather_meterBox.iloc[-1][2]),
                   style={'white-space': 'pre'}),
            html.H5(children='Tempest'),
            html.P(children='    Time'),
            html.P(
                id='Weather_tempest_latest_readings',
                children='    ' + str(data_weather_tempest1.iloc[-1][1]) + '     Battery=' + str(data_weather_tempest1.iloc[-1][3])+
                         '\n    ' + str(data_weather_tempest1.iloc[-1][1]) + '     Air Temperature=' + str(data_weather_tempest1.iloc[-1][2])+
                         '\n    ' + str(data_weather_tempest2.iloc[-1][1]) + '     Direction=' + str(data_weather_tempest2.iloc[-1][4])+
                         '\n    ' + str(data_weather_tempest2.iloc[-1][1]) + '     Speed=' + str(data_weather_tempest2.iloc[-1][18])+
                         '\n    ' + str(data_weather_tempest1.iloc[-1][1]) + '     Illuminance=' + str(data_weather_tempest1.iloc[-1][9])+
                         '\n    ' + str(data_weather_tempest1.iloc[-1][1]) + '     Lightning Strike Distance=' + str(data_weather_tempest1.iloc[-1][10])+
                         '\n    ' + str(data_weather_tempest1.iloc[-1][1]) + '     Lightning Strike Count=' + str(data_weather_tempest1.iloc[-1][11])+
                         '\n    ' + str(data_weather_tempest1.iloc[-1][1]) + '     Accumulated Precipitation=' + str(data_weather_tempest1.iloc[-1][13])+
                         '\n    ' + str(data_weather_tempest1.iloc[-1][1]) + '     Relative Humidity=' + str(data_weather_tempest1.iloc[-1][15])+
                         '\n    ' + str(data_weather_tempest1.iloc[-1][1]) + '     Solar Radiation=' + str(data_weather_tempest1.iloc[-1][17])+
                         '\n    ' + str(data_weather_tempest1.iloc[-1][1]) + '     Station Pressure=' + str(data_weather_tempest1.iloc[-1][19])+
                         '\n    ' + str(data_weather_tempest1.iloc[-1][1]) + '     UV=' + str(data_weather_tempest1.iloc[-1][21])+
                         '\n    ' + str(data_weather_tempest1.iloc[-1][1]) + '     Wind Average=' + str(data_weather_tempest1.iloc[-1][22])+
                         '\n    ' + str(data_weather_tempest1.iloc[-1][1]) + '     Wind Direction=' + str(data_weather_tempest1.iloc[-1][23])+
                         '\n    ' + str(data_weather_tempest1.iloc[-1][1]) + '     Wind Gust=' + str(data_weather_tempest1.iloc[-1][24])+
                         '\n    ' + str(data_weather_tempest1.iloc[-1][1]) + '     Wind Lull=' + str(data_weather_tempest1.iloc[-1][25]),
                style={'white-space': 'pre'}),
        ], className="column-3"),

        #Column 2 (2/3)
        html.Div([
            html.H4(children='Water Meter'),
            html.P(children='    Time'),
            html.P(
                id='Water_meter_latest_readings',
                children='    ' + str(data_water_meter.iloc[-1][1]) + '     Delta Volume=' + str(data_water_meter.iloc[-1][2])+
                         '\n    ' + str(data_water_meter.iloc[-1][1]) + '     Total Accumulated Volume=' + str(data_water_meter.iloc[-1][3])+
                         '\n    ' + str(data_water_meter.iloc[-1][1]) + '     Total Pulse Count=' + str(data_water_meter.iloc[-1][4]),
                style={'white-space': 'pre'}),
            html.H4(children='Pool'),
            html.P(children='    Time'),
            html.P(id='Pool_latest_readings',
                   children='    ' + str(data_pool_temp.iloc[-1][1]) + '     Water Temperature=' + str(data_pool_temp.iloc[-1][4])+
                            '\n    ' + str(data_pool_pH_ORV.iloc[-1][1]) + '     OPR(mV)=' + str(data_pool_pH_ORV.iloc[-1][2])+
                            '\n    ' + str(data_pool_pH_ORV.iloc[-1][1]) + '     pH=' + str(data_pool_pH_ORV.iloc[-1][3]),
                   style={'white-space': 'pre'}),
            html.H4(children='Water Tank'),
            html.P(children='    Time'),
            html.P(id='Water_tank_latest_readings',
                   children='    ' + str(data_tank.iloc[-1][1]) + '     Litres=' + str(data_tank.iloc[-1][2])),
            html.H4(children='Security'),
            html.P(children='    Time'),
            html.P(
                id='Security_latest_readings',
                children='    ' + str(data_security_bathroom.iloc[-1][1]) + '      Bathroom=' + str(data_security_bathroom.iloc[-1][6])+
                         '\n    ' + str(data_security_cabana.iloc[-1][1]) + '      Cabana=' + str(data_security_cabana.iloc[-1][6])+
                         '\n    ' + str(data_security_cabana_NE.iloc[-1][1]) + '     Cabana (NE)=' + str(data_security_cabana_NE.iloc[-1][6])+
                         '\n    ' + str(data_security_cabana_SE.iloc[-1][1]) + '     Cabana (SE)=' + str(data_security_cabana_SE.iloc[-1][6])+
                         '\n    ' + str(data_security_conservatory.iloc[-1][1]) + '     Conservatory=' + str(data_security_conservatory.iloc[-1][6])+
                         '\n    ' + str(data_security_deck.iloc[-1][1]) + '     Deck=' + str(data_security_deck.iloc[-1][6])+
                         '\n    ' + str(data_security_entryHall.iloc[-1][1]) + '     Entry Hall=' + str(data_security_entryHall.iloc[-1][6])+
                         '\n    ' + str(data_security_floorSpace.iloc[-1][1]) + '     Floor Space=' + str(data_security_floorSpace.iloc[-1][6])+
                         '\n    ' + str(data_security_frontGate.iloc[-1][1]) + '     Front Gate=' + str(data_security_frontGate.iloc[-1][6])+
                         '\n    ' + str(data_security_frontPorch.iloc[-1][1]) + '     Front Porch=' + str(data_weather_tempest1.iloc[-1][6])+
                         '\n    ' + str(data_security_garage.iloc[-1][1]) + '     Garage=' + str(data_security_garage.iloc[-1][6])+
                         '\n    ' + str(data_security_guestBath.iloc[-1][1]) + '     Guest Bathroom=' + str(data_security_guestBath.iloc[-1][6])+
                         '\n    ' + str(data_security_guestBed.iloc[-1][1]) + '     Guest Bedroom =' + str(data_security_guestBed.iloc[-1][6])+
                         '\n    ' + str(data_security_katieBed.iloc[-1][1]) + '     Katie Bedroom=' + str(data_security_katieBed.iloc[-1][6])+
                         '\n    ' + str(data_security_kitchen.iloc[-1][1]) + '     Kitchen=' + str(data_security_kitchen.iloc[-1][6])+
                         '\n    ' + str(data_security_laundry.iloc[-1][1]) + '     Laundry=' + str(data_security_laundry.iloc[-1][6])+
                         '\n    ' + str(data_security_lPantry.iloc[-1][1]) + '     Left Pantry=' + str(data_security_lPantry.iloc[-1][6])+
                         '\n    ' + str(data_security_living.iloc[-1][1]) + '     Living Room=' + str(data_security_living.iloc[-1][6])+
                         '\n    ' + str(data_security_lowHall.iloc[-1][1]) + '     Lower Hall=' + str(data_security_lowHall.iloc[-1][6])+
                         '\n    ' + str(data_security_mainBed.iloc[-1][1]) + '     Main Bedroom=' + str(data_security_mainBed.iloc[-1][6])+
                         '\n    ' + str(data_security_net.iloc[-1][1]) + '     Network Room=' + str(data_security_net.iloc[-1][6])+
                         '\n    ' + str(data_security_powder.iloc[-1][1]) + '     Powder Room=' + str(data_security_powder.iloc[-1][6])+
                         '\n    ' + str(data_security_rain.iloc[-1][1]) + '     Rain Sensor=' + str(data_security_rain.iloc[-1][6])+
                         '\n    ' + str(data_security_rPantry.iloc[-1][1]) + '     Right Pantry=' + str(data_security_rPantry.iloc[-1][6])+
                         '\n    ' + str(data_security_rumpus.iloc[-1][1]) + '     Rumpus Room=' + str(data_security_rumpus.iloc[-1][6])+
                         '\n    ' + str(data_security_sam.iloc[-1][1]) + '     Sam Bedroom=' + str(data_security_sam.iloc[-1][6])+
                         '\n    ' + str(data_security_PathSE.iloc[-1][1]) + '     Path (SE)=' + str(data_security_PathSE.iloc[-1][6])+
                         '\n    ' + str(data_security_porchS.iloc[-1][1]) + '     Porch (S)=' + str(data_security_porchS.iloc[-1][6])+
                         '\n    ' + str(data_security_study.iloc[-1][1]) + '     Study=' + str(data_security_study.iloc[-1][6])+
                         '\n    ' + str(data_security_upperHall.iloc[-1][1]) + '     Upper Hallway=' + str(data_security_upperHall.iloc[-1][6])+
                         '\n    ' + str(data_security_wine.iloc[-1][1]) + '     Wine Cellar=' + str(data_security_wine.iloc[-1][6])+
                         '\n    ' + str(data_security_pool.iloc[-1][1]) + '     Pool=' + str(data_security_pool.iloc[-1][6]),
                style={'white-space': 'pre'}),
        ],className="column-3"),
        # Column 3 (3/3)
        html.Div([
            html.H4(children='Lights',
                    style={'textAlign': 'left'}),
            html.P(children='    Time'),
            html.P(id='Lighting_latest_readings',
                   children='    ' + str(data_lighting_BalconyBlind.iloc[-1][1]) + '      Balcony_Blind=' + str(data_lighting_BalconyBlind.iloc[-1][4])+
                            '\n    ' + str(data_lighting_Balcony.iloc[-1][1]) + '      Balcony_Lights=' + str(data_lighting_Balcony.iloc[-1][4])+
                            '\n    ' + str(data_lighting_BalconyUp.iloc[-1][1]) + '      Balcony_Uplights=' + str(data_lighting_BalconyUp.iloc[-1][4])+
                            '\n    ' + str(data_lighting_BathroomDown.iloc[-1][1]) + '      Bathroom_Downlights=' + str(data_lighting_BathroomDown.iloc[-1][4])+
                            '\n    ' + str(data_lighting_BathroomFan.iloc[-1][1]) + '      Bathroom_Fan=' + str(data_lighting_BathroomFan.iloc[-1][4])+
                            '\n    ' + str(data_lighting_BathroomHeat.iloc[-1][1]) + '      Bathroom_Heat_lights=' + str(data_lighting_BathroomHeat.iloc[-1][4])+
                            '\n    ' + str(data_lighting_BathroomTowel.iloc[-1][1]) + '      Bathroom_Towel_Rail=' + str(data_lighting_BathroomTowel.iloc[-1][4])+
                            '\n    ' + str(data_lighting_Christmas.iloc[-1][1]) + '      Christmas_Lights=' + str(data_lighting_Christmas.iloc[-1][4])+
                            '\n    ' + str(data_lighting_ConservatoryDown.iloc[-1][1]) + '      Conservatory_Downlights=' + str(data_lighting_ConservatoryDown.iloc[-1][4])+
                            '\n    ' + str(data_lighting_DeckBlind.iloc[-1][1]) + '      Deck_Blind=' + str(data_lighting_DeckBlind.iloc[-1][4])+
                            '\n    ' + str(data_lighting_Deck.iloc[-1][1]) + '      Deck_Lights=' + str(data_lighting_Deck.iloc[-1][4])+
                            '\n    ' + str(data_lighting_DiningTable.iloc[-1][1]) + '      Dining_Table_Downlights=' + str(data_lighting_DiningTable.iloc[-1][4])+
                            '\n    ' + str(data_lighting_EastSpot.iloc[-1][1]) + '      East_Spotlights=' + str(data_lighting_EastSpot.iloc[-1][4])+
                            '\n    ' + str(data_lighting_EastUp.iloc[-1][1]) + '      East_Up_Lights=' + str(data_lighting_EastUp.iloc[-1][4])+
                            '\n    ' + str(data_lighting_EnsuiteDown.iloc[-1][1]) + '      Ensuite_Downlights=' + str(data_lighting_EnsuiteDown.iloc[-1][4])+
                            '\n    ' + str(data_lighting_EnsuiteFan.iloc[-1][1]) + '      Ensuite_Fan=' + str(data_lighting_EnsuiteFan.iloc[-1][4])+
                            '\n    ' + str(data_lighting_EnsuiteTowel.iloc[-1][1]) + '      Ensuite_Towel_Rail=' + str(data_lighting_EnsuiteTowel.iloc[-1][4])+
                            '\n    ' + str(data_lighting_FloorSpace.iloc[-1][1]) + '      Floor_Space_Lights=' + str(data_lighting_FloorSpace.iloc[-1][4])+
                            '\n    ' + str(data_lighting_FrontDoor.iloc[-1][1]) + '      Front_Door_Light=' + str(data_lighting_FrontDoor.iloc[-1][4])+
                            '\n    ' + str(data_lighting_GarageExternal.iloc[-1][1]) + '      Garage_External_Lights=' + str(data_lighting_GarageExternal.iloc[-1][4])+
                            '\n    ' + str(data_lighting_Garage.iloc[-1][1]) + '      Garage_Light=' + str(data_lighting_Garage.iloc[-1][4])+
                            '\n    ' + str(data_lighting_Garden1.iloc[-1][1]) + '      Garden_Lights_1=' + str(data_lighting_Garden1.iloc[-1][4])+
                            '\n    ' + str(data_lighting_Garden2.iloc[-1][1]) + '      Garden_Lights_2=' + str(data_lighting_Garden2.iloc[-1][4])+
                            '\n    ' + str(data_lighting_GuestBathroomDown.iloc[-1][1]) + '      Guest_Bathroom_Downlight=' + str(data_lighting_GuestBathroomDown.iloc[-1][4])+
                            '\n    ' + str(data_lighting_GuestBathroomFan.iloc[-1][1]) + '      Guest_Bathroom_Fan=' + str(data_lighting_GuestBathroomFan.iloc[-1][4])+
                            '\n    ' + str(data_lighting_GuestBathroom.iloc[-1][1]) + '      Guest_Bathroom_Light=' + str(data_lighting_GuestBathroom.iloc[-1][4])+
                            '\n    ' + str(data_lighting_IslandBenchStrip.iloc[-1][1]) + '      Island_Bench_Strip_Light=' + str(data_lighting_IslandBenchStrip.iloc[-1][4])+
                            '\n    ' + str(data_lighting_KateBedroomFan.iloc[-1][1]) + '      Kate_Bedroom_Fan=' + str(data_lighting_KateBedroomFan.iloc[-1][4])+
                            '\n    ' + str(data_lighting_KateBedroom.iloc[-1][1]) + '      Kate_Bedroom_Light=' + str(data_lighting_KateBedroom.iloc[-1][4])+
                            '\n    ' + str(data_lighting_KitchenDown.iloc[-1][1]) + '      Kitchen_Downlights=' + str(data_lighting_KitchenDown.iloc[-1][4])+
                            '\n    ' + str(data_lighting_KitchenPendant.iloc[-1][1]) + '      Kitchen_Pendant_Lights=' + str(data_lighting_KitchenPendant.iloc[-1][4])+
                            '\n    ' + str(data_lighting_KitchenStrip.iloc[-1][1]) + '      Kitchen_Strip_Light=' + str(data_lighting_KitchenStrip.iloc[-1][4])+
                            '\n    ' + str(data_lighting_LaundryDown.iloc[-1][1]) + '      Laundry_Downlights=' + str(data_lighting_LaundryDown.iloc[-1][4])+
                            '\n    ' + str(data_lighting_LeftPantry.iloc[-1][1]) + '      Left_Pantry_Light=' + str(data_lighting_LeftPantry.iloc[-1][4])+
                            '\n    ' + str(data_lighting_Subfloor.iloc[-1][1]) + '      MF_Subfloor_Fan=' + str(data_lighting_Subfloor.iloc[-1][4])+
                            '\n    ' + str(data_lighting_NetworkRoom.iloc[-1][1]) + '      Network_Room_Downlight=' + str(data_lighting_NetworkRoom.iloc[-1][4])+
                            '\n    ' + str(data_lighting_NorthWest.iloc[-1][1]) + '      North_West_Downlights=' + str(data_lighting_NorthWest.iloc[-1][4])+
                            '\n    ' + str(data_lighting_PlantRoom.iloc[-1][1]) + '      Plant_Room_Lights=' + str(data_lighting_PlantRoom.iloc[-1][4])+
                            '\n    ' + str(data_lighting_PlantRoomFan.iloc[-1][1]) + '      Plant_Room_Subfloor_Fan=' + str(data_lighting_PlantRoomFan.iloc[-1][4])+
                            '\n    ' + str(data_lighting_PlantRoomVoid.iloc[-1][1]) + '      Plant_Room_Void_Lights=' + str(data_lighting_PlantRoomVoid.iloc[-1][4])+
                            #'\n   =' + str(data_lighting_powerRoomDown.iloc[-1][1]) + '      Powder_Room_Downlight=' + str(data_lighting_powerRoomDown.iloc[-1][4])+
                            '\n    ' + str(data_lighting_powerFan.iloc[-1][1]) + '      Powder_Room_Fan=' + str(data_lighting_powerFan.iloc[-1][4])+
                            '\n    ' + str(data_lighting_rightPantry.iloc[-1][1]) + '      Right_Pantry_Light=' + str(data_lighting_rightPantry.iloc[-1][4])+
                            '\n    ' + str(data_lighting_RumpusWest.iloc[-1][1]) + '      Rumpus_West_Downlights=' + str(data_lighting_RumpusWest.iloc[-1][4])+
                            '\n    ' + str(data_lighting_SamBedroomFan.iloc[-1][1]) + '      Sam_Bedroom_Fan=' + str(data_lighting_SamBedroomFan.iloc[-1][4])+
                            '\n    ' + str(data_lighting_SamBedroom.iloc[-1][1]) + '      Sam_Bedroom_Light=' + str(data_lighting_SamBedroom.iloc[-1][4])+
                            '\n    ' + str(data_lighting_SouthEast.iloc[-1][1]) + '      South_East_Spotlight=' + str(data_lighting_SouthEast.iloc[-1][4])+
                            '\n    ' + str(data_lighting_StudyDown.iloc[-1][1]) + '      Study_Downlights=' + str(data_lighting_StudyDown.iloc[-1][4])+
                            '\n    ' + str(data_lighting_TomBedroomFan.iloc[-1][1]) + '      Tom_Bedroom_Fan=' + str(data_lighting_TomBedroomFan.iloc[-1][4])+
                            '\n    ' + str(data_lighting_TomeBedroom.iloc[-1][1]) + '      Tom_Bedroom_Light=' + str(data_lighting_TomeBedroom.iloc[-1][4])+
                            '\n    ' + str(data_lighting_UpperHallwayDown.iloc[-1][1]) + '      Upper_Hallway_Downlights=' + str(data_lighting_UpperHallwayDown.iloc[-1][4])+
                            '\n    ' + str(data_lighting_UpperHallwayFloor.iloc[-1][1]) + '      Upper_Hallway_Floor_Lights=' + str(data_lighting_UpperHallwayFloor.iloc[-1][4])+
                            '\n    ' + str(data_lighting_UpperStair.iloc[-1][1]) + '      Upper_Stair_Lights=' + str(data_lighting_UpperStair.iloc[-1][4])+
                            '\n    ' + str(data_lighting_UpperStairPendant.iloc[-1][1]) + '      Upper_Stair_Pendant_Lights=' + str(data_lighting_UpperStairPendant.iloc[-1][4])+
                            '\n    ' + str(data_lighting_WalkInRobe.iloc[-1][1]) + '      Walk_In_Robe_Light=' + str(data_lighting_WalkInRobe.iloc[-1][4])+
                            '\n    ' + str(data_lighting_WestSpot.iloc[-1][1]) + '      West_Spotlights=' + str(data_lighting_WestSpot.iloc[-1][4])+
                            '\n    ' + str(data_lighting_WineCellar.iloc[-1][1]) + '      Wine_Cellar_Downlights=' + str(data_lighting_WineCellar.iloc[-1][4]),
                   style={'white-space': 'pre'}),
        ],className="column-3")
    ],className="row")
])

@app.callback(Output('data_graph','figure'),
              Input('graph_selector', 'value'))

def update_graph(selected_dropdown_value):
    if selected_dropdown_value == 'Elec_Pow':
        dataGraph = px.line(
            x=data_power["time"],
            y=data_power["power"],
            title="Electricity",
            labels = {
                "x":"Date/Time",
                "y":"Power"
                      }
        )
    elif selected_dropdown_value == 'Temp_Air':
        dataGraph = px.line(
            x=data_weather_tempest1["time"],
            y=data_weather_tempest1["air_temperature"],
            title="Air Temperature(Tempest)",
            labels = {
                "x": "Date/Time",
                "y": "Air Temperature"
            }
        )
    elif selected_dropdown_value == 'Temp_Hum':
        dataGraph = px.line(
            x=data_weather_tempest3["time"],
            y=data_weather_tempest3["relative_humidity"],
            title="Relative Humidity(Tempest)",
            labels={
                "x": "Date/Time",
                "y": "Relative Humidity"
            }
        )
    elif selected_dropdown_value == 'Gar_Hum':
        dataGraph = px.line(
            x=data_weather_garage1["time"],
            y=data_weather_garage1["relative_humidity"],
            title="Relative Humidity(Garage)",
            labels={
                "x": "Date/Time",
                "y": "Relative Humidity"
            }
        )
    elif selected_dropdown_value == 'Gar_Air':
        dataGraph = px.line(
            x=data_weather_garage["time"],
            y=data_weather_garage["air_temperature"],
            title="Air Temperature(Garage)",
            labels={
                "x": "Date/Time",
                "y": "Air Temperature"
            }
        )
    elif selected_dropdown_value == 'MB_Air':
        dataGraph = px.line(
            x=data_weather_meterBox["time"],
            y=data_weather_meterBox["air_temperature"],
            title="Air Temperature(Meter Box)",
            labels={
                "x": "Date/Time",
                "y": "Air Temperature"
            }
        )
    elif selected_dropdown_value == 'Solar_Rad':
        dataGraph = px.line(
            x=data_weather_Solar["time"],
            y=data_weather_Solar["solar_radiation"],
            title="Solar Radiation",
            labels={
                "x": "Date/Time",
                "y": "Solar Radiation"
            }
        )
    elif selected_dropdown_value == 'Wind_Dir':
        dataGraph = px.line(
            x=data_weather["time"],
            y=data_weather["direction"],
            title="Wind Direction (Degrees)",
            labels={
                "x": "Date/Time",
                "y": "Degrees"
            }
        )
    elif selected_dropdown_value == 'Wind_Avg':
        dataGraph = px.line(
            x=data_weather_windAvg["time"],
            y=data_weather_windAvg["wind_avg"],
            title="Wind Average (km/h)",
            labels={
                "x": "Date/Time",
                "y": "km/h"
            }
        )
    elif selected_dropdown_value == 'Wind_Gust':
        dataGraph = px.line(
            x=data_weather_windGust["time"],
            y=data_weather_windGust["wind_gust"],
            title="Wind Gust (km/h)",
            labels={
                "x": "Date/Time",
                "y": "km/h"
            }
        )
    elif selected_dropdown_value == 'Temp_Vol':
        dataGraph = px.line(
            x=data_station_temp["time"],
            y=data_station_temp["voltage"],
            title="Voltage(Tempest)",
            labels={
                "x": "Date/Time",
                "y": "Voltage"
            }
        )
    elif selected_dropdown_value == 'Water_Tank':
        dataGraph = px.line(
            x=data_tank["time"],
            y=data_tank["litres"],
            title="Water tank",
            labels={
                "x": "Date/Time",
                "y": "Litres/ml"
            }
        )
    elif selected_dropdown_value == 'Water_Meter':
        dataGraph = px.line(
            x=data_water_meter["time"],
            y=data_water_meter["total_accumulated_volume"],
            title="Water Meter",
            labels={
                "x": "Date/Time",
                "y": "total_accumulated_volume/L"
            }
        )
    elif selected_dropdown_value == 'Pool_ORP':
        dataGraph = px.line(
            x=data_pool_ORP["time"],
            y=data_pool_ORP["ORPmV"],
            title="ORP (pool)",
            labels={
                "x": "Date/Time",
                "y": "ORP/mv"
            }
        )
    else:
        dataGraph = px.line(
            x=data_pool_temp["time"],
            y=data_pool_temp["water_temperature"],
            title="Water Temperature(pool)",
            labels = {
                "x": "Date/Time",
                "y": "Water Temperature"
            }
        )
    return(dataGraph)

@app.callback(Output('mean','children'),
              Output('sum','children'),
              Output('max','children'),
              Output('min','children'),
              Output('median','children'),
              Output('count','children'),
              Output('std','children'),
              Output('var','children'),
              Input('graph_selector', 'value'))
def update_statistics(selected_dropdown_value):
    if selected_dropdown_value == 'Elec_Pow':
        mean1 = data_power["power"].mean()
        sum1 = data_power["power"].sum()
        max1 = data_power["power"].max()
        min1 = data_power["power"].min()
        median1 = data_power["power"].median()
        count1 = data_power["power"].count()
        std1 = data_power["power"].std()
        var1 = data_power["power"].var()

    elif selected_dropdown_value == 'Temp_Air':
        mean1 = data_weather_tempest1["air_temperature"].mean()
        sum1 = data_weather_tempest1["air_temperature"].sum()
        max1 = data_weather_tempest1["air_temperature"].max()
        min1 = data_weather_tempest1["air_temperature"].min()
        median1 = data_weather_tempest1["air_temperature"].median()
        count1 = data_weather_tempest1["air_temperature"].count()
        std1 = data_weather_tempest1["air_temperature"].std()
        var1 = data_weather_tempest1["air_temperature"].var()

    elif selected_dropdown_value == 'Temp_Hum':
        mean1 = data_weather_tempest3["relative_humidity"].mean()
        sum1 = data_weather_tempest3["relative_humidity"].sum()
        max1 = data_weather_tempest3["relative_humidity"].max()
        min1 = data_weather_tempest3["relative_humidity"].min()
        median1 = data_weather_tempest3["relative_humidity"].median()
        count1 = data_weather_tempest3["relative_humidity"].count()
        std1 = data_weather_tempest3["relative_humidity"].std()
        var1 = data_weather_tempest3["relative_humidity"].var()

    elif selected_dropdown_value == 'Gar_Hum':
        mean1 = data_weather_garage1["relative_humidity"].mean()
        sum1 = data_weather_garage1["relative_humidity"].sum()
        max1 = data_weather_garage1["relative_humidity"].max()
        min1 = data_weather_garage1["relative_humidity"].min()
        median1 = data_weather_garage1["relative_humidity"].median()
        count1 = data_weather_garage1["relative_humidity"].count()
        std1 = data_weather_garage1["relative_humidity"].std()
        var1 = data_weather_garage1["relative_humidity"].var()


    elif selected_dropdown_value == 'Gar_Air':
        mean1 = data_weather_garage["air_temperature"].mean()
        sum1 = data_weather_garage["air_temperature"].sum()
        max1 = data_weather_garage["air_temperature"].max()
        min1 = data_weather_garage["air_temperature"].min()
        median1 = data_weather_garage["air_temperature"].median()
        count1 = data_weather_garage["air_temperature"].count()
        std1 = data_weather_garage["air_temperature"].std()
        var1 = data_weather_garage["air_temperature"].var()

    elif selected_dropdown_value == 'MB_Air':
        mean1 = data_weather_meterBox["air_temperature"].mean()
        sum1 = data_weather_meterBox["air_temperature"].sum()
        max1 = data_weather_meterBox["air_temperature"].max()
        min1 = data_weather_meterBox["air_temperature"].min()
        median1 = data_weather_meterBox["air_temperature"].median()
        count1 = data_weather_meterBox["air_temperature"].count()
        std1 = data_weather_meterBox["air_temperature"].std()
        var1 = data_weather_meterBox["air_temperature"].var()

    elif selected_dropdown_value == 'Solar_Rad':
        mean1 = data_weather_Solar["solar_radiation"].mean()
        sum1 = data_weather_Solar["solar_radiation"].sum()
        max1 = data_weather_Solar["solar_radiation"].max()
        min1 = data_weather_Solar["solar_radiation"].min()
        median1 = data_weather_Solar["solar_radiation"].median()
        count1 = data_weather_Solar["solar_radiation"].count()
        std1 = data_weather_Solar["solar_radiation"].std()
        var1 = data_weather_Solar["solar_radiation"].var()

    elif selected_dropdown_value == 'Wind_Dir':
        mean1 = data_weather["direction"].mean()
        sum1 = data_weather["direction"].sum()
        max1 = data_weather["direction"].max()
        min1 = data_weather["direction"].min()
        median1 = data_weather["direction"].median()
        count1 = data_weather["direction"].count()
        std1 = data_weather["direction"].std()
        var1 = data_weather["direction"].var()

    elif selected_dropdown_value == 'Wind_Avg':
        mean1 = data_weather_windAvg["wind_avg"].mean()
        sum1 = data_weather_windAvg["wind_avg"].sum()
        max1 = data_weather_windAvg["wind_avg"].max()
        min1 = data_weather_windAvg["wind_avg"].min()
        median1 = data_weather_windAvg["wind_avg"].median()
        count1 = data_weather_windAvg["wind_avg"].count()
        std1 = data_weather_windAvg["wind_avg"].std()
        var1 = data_weather_windAvg["wind_avg"].var()

    elif selected_dropdown_value == 'Wind_Gust':
        mean1 = data_weather_windGust["wind_gust"].mean()
        sum1 = data_weather_windGust["wind_gust"].sum()
        max1 = data_weather_windGust["wind_gust"].max()
        min1 = data_weather_windGust["wind_gust"].min()
        median1 = data_weather_windGust["wind_gust"].median()
        count1 = data_weather_windGust["wind_gust"].count()
        std1 = data_weather_windGust["wind_gust"].std()
        var1 = data_weather_windGust["wind_gust"].var()

    elif selected_dropdown_value == 'Temp_Vol':
        mean1 = data_station_temp["voltage"].mean()
        sum1 = data_station_temp["voltage"].sum()
        max1 = data_station_temp["voltage"].max()
        min1 = data_station_temp["voltage"].min()
        median1 = data_station_temp["voltage"].median()
        count1 = data_station_temp["voltage"].count()
        std1 = data_station_temp["voltage"].std()
        var1 = data_station_temp["voltage"].var()

    elif selected_dropdown_value == 'Water_Tank':
        mean1 = data_tank["litres"].mean()
        sum1 = data_tank["litres"].sum()
        max1 = data_tank["litres"].max()
        min1 = data_tank["litres"].min()
        median1 = data_tank["litres"].median()
        count1 = data_tank["litres"].count()
        std1 = data_tank["litres"].std()
        var1 = data_tank["litres"].var()

    elif selected_dropdown_value == 'Water_Meter':
        mean1 = data_water_meter["total_accumulated_volume"].mean()
        sum1 = data_water_meter["total_accumulated_volume"].sum()
        max1 = data_water_meter["total_accumulated_volume"].max()
        min1 = data_water_meter["total_accumulated_volume"].min()
        median1 = data_water_meter["total_accumulated_volume"].median()
        count1 = data_water_meter["total_accumulated_volume"].count()
        std1 = data_water_meter["total_accumulated_volume"].std()
        var1 = data_water_meter["total_accumulated_volume"].var()

    elif selected_dropdown_value == 'Pool_ORP':
        mean1 = data_pool_ORP["ORPmV"].mean()
        sum1 = data_pool_ORP["ORPmV"].sum()
        max1 = data_pool_ORP["ORPmV"].max()
        min1 = data_pool_ORP["ORPmV"].min()
        median1 = data_pool_ORP["ORPmV"].median()
        count1 = data_pool_ORP["ORPmV"].count()
        std1 = data_pool_ORP["ORPmV"].std()
        var1 = data_pool_ORP["ORPmV"].var()
    else:
        mean1 = data_pool_temp["water_temperature"].mean()
        sum1 = data_pool_temp["water_temperature"].sum()
        max1 = data_pool_temp["water_temperature"].max()
        min1 = data_pool_temp["water_temperature"].min()
        median1 = data_pool_temp["water_temperature"].median()
        count1 = data_pool_temp["water_temperature"].count()
        std1 = data_pool_temp["water_temperature"].std()
        var1 = data_pool_temp["water_temperature"].var()

    return mean1,sum1,max1,min1,median1,count1,std1,var1


if __name__ == '__main__':
    app.run_server(debug=True)

