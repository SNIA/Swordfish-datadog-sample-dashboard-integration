import json, checks, dogstatsd
import simplejson
import requests
from checks import AgentCheck
import urllib2

class Volumesdata(AgentCheck):
    def check(self, instance):

        host = instance['url']         
        sptag = instance['sp_dump']
        vtag = instance['volumes_dump']
        
        


        
        pdata = urllib2.urlopen("http://" + host + sptag)
        data = simplejson.load(pdata)
        

        self.gauge('SPCapacitySources Consumed', data['3_StoragePools']['BasePool']['CapacitySources']["ConsumedBytes"])
        self.gauge('SPCapacitySources Allocated', data['3_StoragePools']['BasePool']['CapacitySources']["AllocatedBytes"])
        self.gauge('SP Threshold Low', data['3_StoragePools']['BasePool']['LowSpaceWarningThresholdPercents'][0])
        self.gauge('SP Threshold Medium', data['3_StoragePools']['BasePool']['LowSpaceWarningThresholdPercents'][1])   
        self.gauge('SP Threshold High', data['3_StoragePools']['BasePool']['LowSpaceWarningThresholdPercents'][2])           
        
        
        

