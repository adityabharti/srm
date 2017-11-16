rom srm_client.client import SrmClient, InternalSrmClient

#with SrmClient('10.4.232.217:9086/srm.wsdl', '10.4.232.217\Administrator', 'nutanix/4u').open() as client:
#with SrmClient('10.5.216.143:9086/vcdr/extapi/sdk', 'Administrator', 'nutanix/4u').open() as client:
'''
with SrmClient('10.4.232.33:9086/vcdr/extapi/sdk', 'administrator@nutanix.local', 'Apple4u2$').open() as client:
  print "--->Printing recovery plans"
  print client.get_recovery_plans()
  print "XXX>Recovery plans printed"'''

i_client = InternalSrmClient('10.4.232.33:9086/vcdr/extapi/sdk', 'administrator@nutanix.local', 'Apple4u2$')

print "0+0+" * 4
print i_client.get_protection_groups()
print "0-0-" * 8

