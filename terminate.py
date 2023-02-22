'''Terminate an instance
https://cloud.lambdalabs.com/api/v1/docs#operation/terminateInstance
'''

import argparse
import libs.api as api
import libs.helper as helper

parser = argparse.ArgumentParser(
    add_help=True,
)
parser.add_argument(
    '--ids',
    help='The unique identifiers (IDs) of the instances to terminate',
    nargs='*',
    type=str,
    required=True,
)
args = parser.parse_args()

data = {
    'instance_ids': args.ids
}

obj = api.post('instance-operations/terminate', data)
helper.show(obj['data'])
