# Seconds in hour = 3,600
def convert(hours, minutes):
    """convert_hours = hours * 60 * 60
    convert_minutes = minutes * 60"""
    convert_to_seconds = hours * 60 * 60 + minutes * 60 #cleaner
    print (convert_to_seconds)
    return convert_to_seconds
    
    



convert	(1,3) #3780
convert (2,0) #7200
convert (0,0) #0
