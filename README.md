# lambda-issue-recache
A quick way to issue redis or other recache urls via lambda (python3.6); includes properly compiled resources to import into lambda

REQUIRED ENVIRONMENT VARIABLES:

    [STRING]: TARGET_URL      # Example: http://theguybehindme.com:8080 I need to be full qualified.
    [STRING]: TARGET_URI      # Example: /is/going/insane?key=
    [STRING]: HOST            # Example: theguybehindme  (I'm here for logging messages, I didn't feel like extracting it from string.)
    [STRING]: KEY             # Example:iD0ntF33ls0g0od (Could be worse; you could be Tony Stark. Oh Snap!)

The zip file contains everything you need to put this into service; like now on python3.6 for lambda. (Uses pycurl compiled with GCC from libcurl-devel, with nss backend (Amazon required this). You are responsible only for populating the Environment variables. If you don't trust me (why should you); you need to at least do yourself a favor, and make sure to build your own shared object for pycurl on an amazon linux instance. You'll need to do the following for that:

    yum install -y libcurl-devel libnss
    mkdir build
    cd build
    pip3.6 install pycurl --target .
    # You may get errors about a curl backend not being set, if you do this:
    export PYCURL_SSL_LIBRARY=nss
    # lambda supports nss backend for the pycurl.so that you are building in this directory, not openssl.
    zip ../function.zip .
    zip -g ..function.zip /path/to/lambda_function.py

Go create a lambda job for python3.6 by cli or console and then issue this via the cli, or upload via the console.

    aws lambda update-function-code --function-name YOURFUNCTIONNAMEHERE --zip-file fileb://function.zip --profile YOURPROFILENAME --region YOUR-REGION-HERE
    
Lambda requires the following execution permissions:
    
    ec2:CreateNetworkInterface
    ec2:DescribeNetworkInterfaces
    ec2:DeleteNetworkInterface
  
Happy trails.
