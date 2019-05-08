import json
import pycurl
import os
'''
Environment Variables:
TARGET_URL = https://youserver.yourdomain.suffix:portifrequired
TARGET_URI = '/place/on/serverwhere?key=placeyourkeyinthekey' 
KEY = 's0mekeyh3r3'
The Parameterization allows us to reuse for other recache requests, and allows
easy encapsulation.
'''
try:
    TARGET_URL = os.environ['TARGET_URL']
    TARGET_URI = os.environ['TARGET_URI']
    HOST = os.environ['HOST']
    KEY = os.environ['KEY']
except KeyError as MissingEnvironmentVariables:
    print('Missing one or more environment variables! Please supply '
    'TARGET_URL, TARGET_URI, HOST, KEY')
    raise MissingEnvironmentVariables
body_mesg = ' recache request for adserver via Tomcat/JBOSS listener on '
ret_body_succ = '[SUCCESS]: Performed' + body_mesg + HOST + '!'
ret_body_fail = '[FAILED]: Could NOT perform' + body_mesg + HOST + '!'
fqurl = TARGET_URL + TARGET_URI + KEY
def lambda_handler(event, context):
    try:
        c = pycurl.Curl()
        c.setopt(c.URL, fqurl )
        c.perform()
        c_resp_code = c.getinfo(pycurl.HTTP_CODE)
        c.close()
        if c_resp_code != 200:
            raise Exception
    except Exception as FailedConnectivityorBadResponseCheckServer:
        return {
        'statusCode': c_resp_code,
        'body': json.dumps(ret_body_fail)
    }
        raise FailedConnectivityorBadResponseCheckServer

    return {
        'statusCode': c_resp_code,
        'body': json.dumps(ret_body_succ)
    }
