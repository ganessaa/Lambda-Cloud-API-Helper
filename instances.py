'''List running instances
https://cloud.lambdalabs.com/api/v1/docs#operation/listInstances
https://cloud.lambdalabs.com/api/v1/docs#operation/getInstance
'''

import argparse
import libs.api as api
import libs.helper as helper

parser = argparse.ArgumentParser(
    add_help=True,
)
parser.add_argument(
    '--id',
    help='The unique identifier (ID) of the instance',
    type=str,
)
args = parser.parse_args()

path = 'instances'

if args.id:
    path = '/'.join([path, args.id])

obj = api.get(path)
helper.show(obj['data'])


def show(datum):
    vals = [
        datum['id'],
        datum['instance_type']['name'],
        datum['region']['name'],
        datum['status'],
    ]
    if 'ip' in datum:
        vals.append(datum['ip'])
    print(' '.join(vals))


print('####################')
print('# Active instances #')
print('####################')
if args.id:
    show(obj['data'])
else:
    for datum in obj['data']:
        show(datum)
