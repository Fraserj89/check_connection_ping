# A quick tool to ping a destination to see whether it gets a response or not

# import the modules needed
import os
import time

# Enter the IP Address of the device to test connection with
hostname = "192.168.11.118"
# Set the failcount to 0, this will allow us to select how many fails we want before
# we state that the network is down.
failCount = 0;

while True:
# Set up ping command:
# -c flag is how many ping packets to send
# -t is the timeout to wait in seconds
# then add the hostname as set above, then don't write the ping results to terminal
    response = os.system("ping -c 1 -t 8 " + hostname + " > /dev/null")
# If the response = 0 this shows no packets were lost, so the network is up.
    if response == 0:
        pingstatus = "Network Active"
        print pingstatus
# Make sure to reset the fail counter back to 0
        failCount = 0;
# Make the application wait for 3 seconds before running again.
        time.sleep(3)
    else:
# If the response is anythin else, it will print as a network error
# This in turn will add 1 to the fail count
        failCount += 1
# Now we set the fail count so that if it = 3 or more then it will print a network error.
        if failCount >= 3:
            pingstatus = "Network Error"
            print pingstatus
            time.sleep(3)
