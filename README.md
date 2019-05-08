# lambda-issue-recache
A quick way to issue redis or other recache urls via lambda (python3.6); includes properly compiled resources to import into lambda

REQUIRED ENVIRONMENT VARIABLES:

    [STRING]: TARGET_URL      # Example: http://theguybehindme.com:8080
    [STRING]: TARGET_URI      # Example: /is/going/insane?key=
    [STRING]: HOST            # theguybehindme  (I'm here for logging messages, you can leave this null.)
    [STRING]: KEY             # iD0ntF33ls0g0od (Could be worse; you could be Tony Stark.)

The zip file contains everything you need to put this into service; like now on python3.6 for lambda. (Uses pycurl compiled with GCC from libcurl-devel, with nss backend (Amazon required this). You are responsible only for populating the Environment variables. 

Easiest way is to create a lambda job for python3.6 and then issue this via the cli

    aws lambda update-function-code --function-name YOURFUNCTIONNAMEHERE --zip-file fileb://function.zip --profile YOURPROFILENAME --region YOUR-REGION-HERE
    
  
Happy trails.
