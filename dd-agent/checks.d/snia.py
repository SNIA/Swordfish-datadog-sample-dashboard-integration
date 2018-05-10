import json, checks
import simplejson
import requests
from checks import AgentCheck
import urllib2

class Volumesdata(AgentCheck):
    def check(self, instance):

        host = instance['url']         
        ttag = instance['url_storage']
        vtag = instance['volumes_dump']
        ftag = instance['url_fs_storage']
        


        sservices = urllib2.urlopen("http://" + host + "StorageServices")
        sdata1 = simplejson.load(sservices)
        pdata = urllib2.urlopen("http://" + host + ttag + "/vol3")
        data = simplejson.load(pdata)
        qdata = urllib2.urlopen("http://" + host + ftag + "/FS2")
        data1 = simplejson.load(qdata)
        rdata = urllib2.urlopen("http://" + host + vtag)
        data2 = simplejson.load(rdata)
       

        self.count('storageservices.count', data["Members@odata.count"])
        self.gauge('ConsumedBytes of capacity in 3/volumes/vol3', data['Capacity'][0]['Data']["ConsumedBytes"])
        self.gauge('AllocatedBytes of capacity in 3/volumes/vol3', data['Capacity'][0]['Data']["AllocatedBytes"])        
        self.gauge('ConsumedBytes in 1/volumes/4', data2['1_Volumes']['4']['CapacitySources']["ConsumedBytes"])
        self.gauge('AllocatedBytes in 1/volumes/4', data2['1_Volumes']['4']['CapacitySources']["AllocatedBytes"])
        self.gauge('ConsumedBytes in 3/FileSystems/FS2', data1['Capacity']['Data']["ConsumedBytes"])
        self.gauge('AllocatedBytes in 3/FileSystems/FS2', data1['Capacity']['Data']["AllocatedBytes"])
        self.gauge('Threshold values low', data1['LowSpaceWarningThresholdPercents'][0])
        self.gauge('Threshold values medium', data1['LowSpaceWarningThresholdPercents'][1])
        

        
        
        

