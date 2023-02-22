'''Retrieve list of offered instance types
https://cloud.lambdalabs.com/api/v1/docs#operation/instanceTypes
'''

import libs.api as api
import libs.helper as helper

obj = api.get('instance-types')
helper.show(obj['data'])

print('###################################')
print('# Available Instances and Regions #')
print('###################################')
for datum in obj['data'].values():
    for regions in datum['regions_with_capacity_available']:
        print(datum['instance_type']['name'], ':', regions['name'])
