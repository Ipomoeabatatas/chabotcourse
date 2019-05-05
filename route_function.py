
import datetime



def get_shuttleschedule(property, pickup_point, day_type):
## Route a dictionary containing tuples as the key.
## Each tuple refers a unique combination of property, pickup point, weekdaytype. 
## Based on the tuple combination, there will be a list containing the leaving time.
## This list is returned by the function
## The dictionary below represents the hypothetical bus schedule from 
    routes = {
                 ("Goodlife Club", "Clubhouse", "Weekday"): ["1:00PM", "3:00PM", "5:00PM", "7:00PM"], 
                 ("Goodlife Club", "Pasir Ris Mrt", "Weekday"): ["1:30PM", "3:30PM", "5:30PM", "7:30PM"], 
                 ("Goodlife Club", "Clubhouse", "Weekend"): ["1:00PM", "2:00PM","3:00PM", "4:00PM", "5:00PM", "6:00PM","7:00PM"], 
                 ("Goodlife Club", "Clubhouse", "Weekend"): ["1:30PM", "2:30PM","3:30PM", "4:30PM", "5:30PM", "6:30PM","7:30PM"], 
                 ("AI Hub Park", "Clementi MRT", "Weekday"): ["8:00AM", "8:30AM", "9:00AM"],
                 ("AI Hub Park", "Clementi MRT", "Weekend"): ["No services"],
                 ("AI Hub Park", "Block A", "Weekday"): ["5:00PM", "6:00PM", "7:00PM"],
                 ("AI Hub Park", "Block B", "Weekday"): ["5:15PM", "6:15PM", "7:15PM"],
                 ("AI Hub Park", "Block A", "Weekend"): ["No services"],
                 ("AI Hub Park", "Block B", "Weekend"): ["No services"],
                }        
    result = routes.get( (property  ,  pickup_point , day_type ), ["There is no route found"])                         
    return result



        
### Example 1: To request for weekday schedule for Goodlie Club at Pickup Point Clubhouse

property = "Goodlife Club"
pickUpPt = "Clubhouse"
timelist = get_shuttleschedule(property, pickUpPt, "Weekday" )
print ("\n")
print ("Weekday Schedule for %s at %s is :--> " %(property, pickUpPt) )
print (timelist)

### Example 2 : To request for weekday schedule for AI Hub Park at Pickup Point Block A
property = "AI Hub Park"
pickUpPt = "Block A"
timelist = get_shuttleschedule(property, pickUpPt, "Weekday" )
print ("\n")
print ("Weekday Schedule for %s at %s is :--> " %(property, pickUpPt) )
print (timelist)


### Example 3 : To request for weekend schedule for AI Hub Park at Pickup Point Block A
property = "AI Hub Park"
pickUpPt = "Block A"
timelist = get_shuttleschedule(property, pickUpPt, "Weekend" )
print ("\n")
print ("Weekend Schedule for %s at %s is :--> " %(property, pickUpPt) )
print (timelist)
print ("\n")


#####################################################################
### the codes below are to find of the day of week (e.g. weekend of weekday)

now = datetime.datetime.now()    ### gets the current time
dayofweek = now.weekday()   # 0 - 4 is weekday ; 5-6 is weekend

if (dayofweek > 4 )  :
      daytype = "Weekend"
else:
      daytype = "Weekday"