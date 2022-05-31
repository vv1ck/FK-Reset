import Reset_Fake
import suspicious_login
Modes = input("""
  _____ _  __  ____                _    
 |  ___| |/ / |  _ \ ___  ___  ___| |_  
 | |_  | ' /  | |_) / _ \/ __|/ _ \ __| 
 |  _| | . \  |  _ <  __/\__ \  __/ |_  
 |_|   |_|\_\ |_| \_\___||___/\___|\__| 
           By Mr.JØKER @221298
                                        
 -1) Reset password Fake
 -2) Suspicious login
[$] Enter : """)
if Modes=='1':Reset_Fake.Settings()
elif Modes=='2':suspicious_login.Settings()
