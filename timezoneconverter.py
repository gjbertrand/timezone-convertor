from datetime import datetime
import pytz
import time

 






timezone_reference = {
    "EST": "America/New_York",
    "EDT": "America/New_York",
    "CST": "America/Chicago",
    "CDT": "America/Chicago",
    "MST": "America/Denver",       
    "MDT": "America/Denver",
    "PST": "America/Los_Angeles",
    "PDT": "America/Los_Angeles",
    "AKST": "America/Anchorage",
    "AKDT": "America/Anchorage",
    "HST": "Pacific/Honolulu",
    "HDT": "Pacific/Honolulu",    
    "AST": "America/Puerto_Rico",  
    "ADT": "America/Puerto_Rico",
    "NST": "America/St_Johns",
    "NDT": "America/St_Johns",
    "MST_CA": "America/Edmonton",   
    "MDT_CA": "America/Edmonton",
    "GMT": "Europe/London",
    "UTC": "UTC",
    "BST": "Europe/London",         
    "CET": "Europe/Paris",
    "CEST": "Europe/Paris",
    "EET": "Europe/Athens",
    "EEST": "Europe/Athens",
    "IST": "Asia/Kolkata",       
    "PKT": "Asia/Karachi",
    "WIB": "Asia/Jakarta",          
    "WITA": "Asia/Makassar",
    "WIT": "Asia/Jayapura",
    "CHINA": "Asia/Shanghai",   
    "JST": "Asia/Tokyo",
    "KST": "Asia/Seoul",
    "HKT": "Asia/Hong_Kong",
    "SGT": "Asia/Singapore",
    "GST": "Asia/Dubai",
    "MSK": "Europe/Moscow",
    "AEST": "Australia/Sydney",
    "AEDT": "Australia/Sydney",
    "ACST": "Australia/Adelaide",
    "ACDT": "Australia/Adelaide",
    "AWST": "Australia/Perth",
    "NZST": "Pacific/Auckland",
    "NZDT": "Pacific/Auckland",
    "WAT": "Africa/Lagos",
    "CAT": "Africa/Harare",
    "EAT": "Africa/Nairobi",
    "ART": "America/Argentina/Buenos_Aires",
    "BRT": "America/Sao_Paulo",
    "BRST": "America/Sao_Paulo",
    "CLT": "America/Santiago",
    "CLST": "America/Santiago",
    "PET": "America/Lima",
    "SAST": "Africa/Johannesburg",
    "CHST": "Pacific/Guam",
}



def get_current_timezone_time(timezone):
    timezone = timezone.upper()

    if timezone not in timezone_reference:
        return "Timezone not found"
    
    else:
        tz = pytz.timezone(timezone_reference[timezone])
        now = datetime.now(tz)
        return now.strftime(f"%H:%M")
    
def convert_timezone(timezone1, timezone2,time):
    """Takes a time and a timezone and converts it to another one"""
    given_time = time.split(':')
    given_time[0] = int(given_time[0])
    given_time[1] = int(given_time[1])
    given_hour = given_time[0]
    given_minute = given_time[1]

    current = datetime.now()

    given_with_date =  datetime(current.year,current.month, current.day, given_hour, given_minute)

    if timezone1 not in timezone_reference or timezone2 not in timezone_reference:
        return "Timezone not found"
    
    else:
        tz = pytz.timezone(timezone_reference[timezone1])
        start_tz = tz.localize(given_with_date)

        tz2 = pytz.timezone(timezone_reference[timezone2])
        end_tz = start_tz.astimezone(tz2)

        return end_tz.strftime(f"%H:%M")




def main():
    while True:
        time.sleep(1)
        file_path = r"timezone-convertor/request-file/timezone_request.txt"
        f = open(file_path, 'r')
        data = f.read().strip()
        f.close()
        if  len(data) == 0:
            continue
        
        inputs = data.split()

        if inputs[0].lower() == "current": 
            print("Received current comanded with timezone " + inputs[1])
            f = open(file_path, 'w')
            content = get_current_timezone_time(inputs[1])
            f.write(content)
            f.close()
            print("Sent " + content)

        
        elif inputs[0].lower() == "convert":
            f = open(file_path, 'w')
            f.write(convert_timezone(inputs[1], inputs[2], inputs[3]))
            f.close()

        


main()
print(get_current_timezone_time('PST'))

