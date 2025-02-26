from rest_framework.throttling import UserRateThrottle

# this class sets the new throttling policy for the user as the default throttling rate 

class TenCallsPerMinute(UserRateThrottle):
    # rate = '10/m'
    scope = 'ten'

# add in the settings.py 
# 'ten': '10/minute' 