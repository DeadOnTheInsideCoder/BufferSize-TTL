# BufferSize-TTL

<h1>Usage:</h2><br />

This program can find MaxBufferSize AND MaxTTL of a host or an ip address(Ipv4 OR Ipv6).<br />

TCP Tuning: https://en.wikipedia.org/wiki/TCP_tuning<br />
TTL(Time To Live): https://en.wikipedia.org/wiki/Time_to_live


<h1>HOW TO INSTALL:</h1><br />
          1)Download zip file or clone it(https://github.com/DeadOnTheInsideCoder/BufferSize-TTL.git).<br />
          2)Unzip it and move it to desktop(If you want to place it in another directory you must change step 3 command.)<br />
          2)Open up run with windows Key + r , type cmd and hit ENTER.<br />
          3)Type this command >> cd /Desktop/BufferSize_TTL<br />
          4)And then type this command >> BufferSize_TTL<br />
          OR >> python BufferSize_TTL.py<br /> 
          OR >> BufferSize_TTL.py<br />


<h1>HOW TO USE:</h1><br />
         You can specify 2 arguments:<br />
                 First Argument is the host or ip<br />
                 Second Argument is the output file<br />                
         You can specify them before or after.<br />


<h1>Example:</h1><br />
           
           >> BufferSize_TTL www.google.com c://Users/MyUser/Desktop/out.txt
           >> BufferSize_TTL www.google.com
           MaxBufferSize: 1465
           MaxTTL:15
           >>BufferSize_TTL
           Host >>
           Path >>

<h1>HOW IT WORKS:</h1><br />
             At Ping program you can specify the bufferSize and the TTL<br />
             So if i type a command like:<br />
             >> ping www.google.com -l 1465    //-l is for bufferSize<br />
             If the buffer size is too much for the host it returns Request timed out.<br /> 
             And if i type a command like:<br />
             >> ping www.google.com -i 4       //-i is for ttl<br />
             If the ttl time exceeded it will throw an TTL expired in transit(Time Exceeded Error(Error 11))<br />
             We use the os python library so we can execute cmd commands and get their output<br />
             So we run a while loop and we execute every posible MaxBufferSize And MaxTTL<br />
             We filter the output and we are done.<br />
