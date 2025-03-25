import datetime
import MasterSettings as MasSet

class logger:
    def __init__(self,event):

        "simply logs the time, date and the passed in event"

        self.event      = event
        self.file_path  = MasSet.Log_Files
        self.time       = datetime.datetime.now().strftime("%H:%M:%S")
        self.date       = datetime.date.today()



        try:
            with open (self.file_path,"a")as file:
                file.write (f"\n{self.time} : {self.date}, {self.event}" )
        except Exception as err:
            print ("Log event Failure !")
            print ("Exception details:", err)



if __name__ == "__main__":

    logger("test log")