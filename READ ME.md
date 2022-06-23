# Mullvad-Brute-forcer
Proof of concept of a tool that is made to try brute force Mullvad VPN accounts 


-Idea 
You would think that a service who's primary purpose is to provide privacy would make an account system which is pretty strong right? Well on the surface you would see Mullvad's 16 digit account number login system as a potential issue, as you dont need a user and pass, so in theory couldnt you just sequentially generate 16 digit numbers and you would think after awhile you would get some hits right. 

Well turns out a 16 digit number has 10,000,000,000,000,000 different possible combinations. It is highly unlikey you would get a hit. Out of 555k registerd mullvad avvounts that gives you roughly a 0.00000000000052582% chance of getting a hit. Almost impossible, but not quite. This method is a proof of concept and is for educational purposes only.

-execution 
This simple script generates 16 digit numbers, then checks them against the mullvad login endpoint. Includes threading for better performance.

-issues
Mullvad's login endpoint is rate limited, if a thread tries to many times to check the number it will get a error that the max retries has been exceeded. Could be circumvented with the use of proxies, or using a mobile endpoint which could potentially not be rate limited