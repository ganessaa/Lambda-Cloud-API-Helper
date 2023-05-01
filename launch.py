'''Launch instances
https://cloud.lambdalabs.com/api/v1/docs#operation/launchInstance
'''

import argparse
import libs.api as api
import libs.env as env
import libs.helper as helper

parser = argparse.ArgumentParser(
    add_help=True,
)
parser.add_argument(
    '--region_name',
    help='Short name of a region',
    type=str,
    required=True,
)
parser.add_argument(
    '--instance_type_name',
    help='Name of an instance type',
    type=str,
    required=True,
)
args = parser.parse_args()

data = {
    'region_name': args.region_name,
    'instance_type_name': args.instance_type_name,
    'ssh_key_names': [
        env.SSH_KEY_NAME
    ],
    'file_system_names': [],
    'quantity': 1
}

obj = api.post('instance-operations/launch', data)
if 'data' in obj:
    helper.show(obj['data'])
else:
    print("*************************************************************************************")
    print("*** Failed to launch the instance. Please check your configuration and try again. ***")
    print("*************************************************************************************")
