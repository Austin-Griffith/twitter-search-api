import urllib2
import base64
import json
UN = 'austin.griffith@colorado.edu' # YOUR GNIP ACCOUNT EMAIL ID
PWD = 'Vicki1957!'
#account = '' # YOUR GNIP ACCOUNT USER NAME
def get_json(data):
    return json.loads(data.strip())
def post():
    url = 'https://gnip-api.twitter.com/search/fullarchive/accounts/greg-students/prod.json'
    publisher = "twitter"
    streamType = "track"
    dataFormat = "activity-streams"
    fromDate = "2018-0416-0000"
    toDate = "2018-0415-0000"
    jobTitle = "job30"

    rules = '[{"query":"raining","maxResults":"10"}]'

    jobString = '{"publisher":"' + publisher + '","streamType":"' + streamType + '","dataFormat":"' + dataFormat + '","fromDate":"' + fromDate + '","toDate":"' + toDate + '","title":"' + jobTitle + '","rules":' + rules + '}'
    base64string = base64.encodestring('%s:%s' % (UN, PWD)).replace('\n', '')
    req = urllib2.Request(url=url, data=jobString)
    req.add_header('Content-type', 'application/json')
    req.add_header("Authorization", "Basic %s" % base64string)

    proxy = urllib2.ProxyHandler({'http': 'http://proxy:8080', 'https': 'https://proxy:8080'})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)
    try:
        response = urllib2.urlopen(req)
        the_page = response.read()
        the_page = get_json(the_page)
        print 'Job has been created.'
        print 'Job UUID : ' + the_page['jobURL'].split("/")[-1].split(".")[0]
    except urllib2.HTTPError as e:
        print e.read()

if __name__=='__main__':
    post()
