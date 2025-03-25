# time in Msecs
# current_milli_time() = https://stackoverflow.com/questions/5998245/how-do-i-get-the-current-time-in-milliseconds-in-python

import time
import Error_Handeling



def current_milli_time():                       #returns the current time in milliseconds
    return round(time.time() * 1000)



class Sensor_Single_parcel_mesurments ():          #opens the excel file and appends the chosen language colum to the list 
                                    #colums 1 None, 2 EN (English (US)), 3 DE (German), 4 PL (Polish), 5 RO (Romanian), 6 FR (French), 7 ES (Spanisch), 8 PT (Portugese)  
    
    def __init__(self,Dict_of_RelevantData,LogAll,Active,SensorIn):
        pass
        
        self.LogAll = LogAll 
        self.Active = Active
        self.Sensor = SensorIn
        self.Dict_of_RelevantData = Dict_of_RelevantData
    
    def ParcelLength (self, Active:bool, SensorIn :bool, Dict_of_RelevantData :dict ,LogAll :bool = False):

            self.start	= 0
            self.end    = 0

            self.TimeMax	= self.Dict_of_RelevantData.get("TimeMax")
            self.TimMin  	= self.Dict_of_RelevantData.get("TimeMin")
            self.TimeSingle = self.Dict_of_RelevantData.get("TimeSingle")
            self.Timedouble = self.Dict_of_RelevantData.get("TimeDouble")
            


            self.start = current_milli_time()

            if self.Sensor == True and self.Active == True:
                self.end = current_milli_time()

            self.timepassed = self.start / self.end 


            if self.Active == True and self.Sensor == True and self.timepassed is not 0: 
                
                if self.timepassed > self.TimeMax + 10:
                    ParcelLong(eventcode)

                if self.timepassed < self.TimeMin + 10:
                    ParcelShort(eventcode)		


                if LogAll == True:
            
                    if self.timepassed < self.TimeSingle: 	
                        ParcelSingle(eventcode)

                    if self.timepassed >= self.Timedouble and not self.timepassed > self.TimeMax + 10: 	
                        ParcelDouble(eventcode)


class Sensor_Health ():          #opens the excel file and appends the chosen language colum to the list 
                                    #colums 1 None, 2 EN (English (US)), 3 DE (German), 4 PL (Polish), 5 RO (Romanian), 6 FR (French), 7 ES (Spanisch), 8 PT (Portugese)  
    
    def __init__(self, Active:bool, SensorIn :bool, Dict_of_RelevantData :dict ,LogAll :bool = False , sensor_helth_check :bool= True):
        pass
        

        
        self.LogAll = LogAll 
        self.Active = Active
        self.sensor_helth_check = sensor_helth_check
        self.Sensor = SensorIn
        self.Dict_of_RelevantData = Dict_of_RelevantData


    def sensor_helth (self): # does not work phase 1 to initiate, but the rest is useles !!!
        """ log sensor input 5x if time is == witin 50ms of another start test (if time is == witin of time before 50ms apend to list else clear list)
            log the repeted times 200x = (if false == True and time /\ within 10 ms apend to list)
            if 200 entrys are reached, calculate average time and apend to new list and reppeat 200x 1x
            if average time is witin15ms of oneanother raise senor health
            
            
            if a brake of 10 revolution does not add another time event to the list clear both lists
                if time is grater than 15 ms clear both lists
        """


        self.time_tolerance_in_ms_init:   int = 20            # time in ms, to set the tolerance for initilasaition of the second phase  
        self.time_tolerance_in_ms_Long:   int = 10            # time in ms, to set the tolerance
        self.final_tolerance_time_ms:     int = 15            # time in ms, to set the tolerance
        self.firstCountingMax:  int = 5             # counts the first time 
        self.TimeCountListMax:  int = 200           # counts the second time (2x)
        self.timetotal:         int = 0
        self.timelotal_long_1:  int = 0
        self.timelotal_long_2:  int = 0
        self.timelist_short = []
        self.timelist_long_1 = []
        self.timelist_long_2 = []


        
        if self.Active == True and self.sensor_helth_check == True:
            # first chek if sensor is beeing falsy triggert (by a peace of tape on the belt or simelar)
            while len(self.timelist_short) <= self.firstCountingMax:                                       # apend the current time in ms to the list 
                    
                if self.Sensor == False:
                    self.time1 = current_milli_time()
                    self.timelist_short.append(self.time1)
                time.sleep(0.2)
            
            self.num_of_entrys_1 = len(self.timelist_short)

            for self.timeX in self.timelist_short:
                self.timetotal += self.timeX                                                                # calculates the total time 

            self.time_short_resault = self.timetotal/self.num_of_entrys_1
                



            if self.time_short_resault == self.timelist_short + self.time_tolerance_in_ms_init or self.time_short_resault == self.timelist_short - self.time_tolerance_in_ms_init:    # if this codition returns true then the sensor is beeing closly monotord for 400 revolutions of the belt (take the average of the last 5 revolutions and compers them to the first one in the list if itis witin +-20 ms the condition is true)
                # second chek if sensor is beeing falsy triggert            
                while  len(self.timelist_long_1) <= self.TimeCountListMax:                                   # apend the current time in ms to the list

                    self.time2 = current_milli_time()
                    self.timelist_long_1.append(self.time2)                        
                    time.sleep(0.2)
                    
                self.num_of_entrys_2 = len(self.timelist_long_1)

                for self.timeY in self.timelist_long_1:
                    self.timelotal_long_1 += self.timeY 

                self.timelotal_long_resault_1 = self.timelotal_long_1/self.num_of_entrys_2
                    
                    


                if self.timelotal_long_resault_1 == self.timelist_short + self.time_tolerance_in_ms_Long or self.timelotal_long_resault_1 == self.timelist_short - self.time_tolerance_in_ms_Long:    # if this codition returns true then the sensor is beeing closly monotord for 400 revolutions of the belt (take the average of the last 5 revolutions and compers them to the first one in the list if itis witin +-20 ms the condition is true)
                    # third chek if sensor is beeing falsy triggert (nessecery ?)
                    while  len(self.timelist_long_2) <= self.TimeCountListMax:                                   # apend the current time in ms to the list

                        self.time2 = current_milli_time()
                        self.timelist_long_2.append(self.time2)                        
                        time.sleep(0.2)
                            
                    self.num_of_entrys_3 = len(self.timelist_long_2)

                    for self.timeZ in self.timelist_long_2:
                        self.timelotal_long_2 += self.timeZ 

                    self.timelotal_long_resault_2 = self.timelotal_long_2/self.num_of_entrys_3



                    if self.timelotal_long_resault_1 == self.timelotal_long_resault_2 + self.final_tolerance_time_ms or self.timelotal_long_resault_1 == self.timelotal_long_resault_2 - self.final_tolerance_time_ms:               # if long list 1 and 2 average are within 15 ms of oneanother 
                        #call object on belt
                        #write to log
                        pass
                        
                    else:                       
                        self.time_short_resault = 0
                        self.timetotal = 0
                        self.timelist_short.clear()
                        self.timelist_long_1.clear()
                        self.timelist_long_2.clear()


            else:
                self.time_short_resault = 0
                self.timetotal = 0
                self.timelist_short.clear()









