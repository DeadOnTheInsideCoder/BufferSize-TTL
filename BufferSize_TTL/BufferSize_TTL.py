#/usr/bin/python3

import subprocess
import sys
import os
from datetime import datetime


def GetArguments():

   global host
   global path
   global Write
   
   try:
       host = sys.argv[1]   
   except IndexError:
     
      try:
       host = str(input("[?]Host >>")) 
      except KeyboardInterrupt:
        print("[!]You pressed ctr+x")
        print("[*]Exiting...")
        sys.exit()
      except EOFError:
        sys.exit()
      except Exception as e:
       print("[!]Error :",str(e))    
   except Exception as e:
     print("[!]Error :",str(e))
     
   try:
     path = sys.argv[2]
     Write = True
   except IndexError:  
     try:  
      path = str(input("[?]Path >>"))
      if path == "":      
         Write = False
      else:
        Write = True     
     except KeyboardInterrupt: 
        print("[!]You pressed ctr+x")
        print("[*]Exiting...")
        sys.exit()   
     except EOFError:   
        sys.exit()     
     except Exception as e:    
       print("[!]Error :",str(e))
       sys.exit()     
   except Exception as e:   
     print("[!]Error :",str(e))
     sys.exit()

   

def FindMaxBufferSize():

  global host
  global BufferSize
  global Start_Time
  global startupinfo
  global count
  
  try:
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    count = 1460
    Start_Time = datetime.now()
    while True:

     print("\n[!]Started at: ",Start_Time)
     print("[!]Finding MaxBufferSize...")
     print("[!]Testing MaxBufferSize: ",str(count))
     result = subprocess.Popen(['ping','-n','2','-l',str(count),host]
                          ,stdout=subprocess.PIPE
                          ,stderr=subprocess.PIPE
                          ,startupinfo=startupinfo)
     out,err= result.communicate()
     out = out.decode("utf-8")
     if '(100% loss)' in out:
         BufferSize = count - 1
         print("[*]Found!")
         break
     else:
         os.system('cls')
         count = count +1
  except KeyboardInterrupt:
     sys.exit()
  except Exception as e:
     print("[!]Error: ",str(e))
     sys.exit()


def TimeToLive():

    global host
    global BufferSize
    global Start_Time
    global startupinfo
    global info
    global count
    
    threshold = 20
    try:
      while True:
        print("\n[!]Started at: ",Start_Time)
        print("[!]Finding MaxBufferSize...")
        print("[!]Testing MaxBufferSize: ",str(count))
        print("[*]Found!")
        print("[!]Finding maximum TTL...")
        print("[!]Testing MaximumTTL: ",str(threshold))
        result = subprocess.Popen(['ping','-n','2','-i',str(threshold),host]
                          ,stdout=subprocess.PIPE
                          ,stderr=subprocess.PIPE
                          ,startupinfo=startupinfo)
        out,err= result.communicate()
        out = out.decode("utf-8")
        if 'TTL expired in transit' in out:
            print("[*]Found!")
            End_Time = datetime.now()
            Total_Time = End_Time - Start_Time
            TTL = threshold +1
            info = {'host':host,'BufferSize':BufferSize,'TTL':TTL,'Start_Time':Start_Time,'End_Time':End_Time,'Total_Time':Total_Time}
            break
        else:
            threshold = threshold-1
            os.system('cls')

    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        print("[!]Error: ",str(e))
        sys.exit()



def PrintAndWriteResults():

    global info
    global path
    output = "Results:\n\tHost: "+str(info['host'])+'\n\tMaxBufferSize: '+str(info['BufferSize'])+'\n\tMax TTL: '+str(info['TTL'])+'\n\tStart Time: '+str(info['Start_Time'])+'\n\tEnd Time: '+str(info['End_Time'])+'\n\tTotal Time: '+str(info['End_Time']-info['Start_Time'])
    print(output)
    try:
      if path == '':
         sys.exit()
      else:
         file = open(path,'a')
         file.write(str(output))
         file.close()

    except Exception as e:
       print('Error: ',str(e))
       sys.exit()

   
def PingInfo():

    GetArguments()
    FindMaxBufferSize()
    TimeToLive()
    PrintAndWriteResults()
   
    
PingInfo()
