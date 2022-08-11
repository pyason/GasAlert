import sys
sys.path.insert(1, '../src')

from GasAlert import lambda_handler

firstSchedulerEvent = {'id': '2e546d39-1259-fcc8-774e-424ec5179b35', 'detail-type': 'Scheduled Event', 'source': 'aws.events', 'time': '2022-08-11T16:30:00Z', 'region': 'ca-central-1', 'detail': {}}
secondSchedulerEvent = {'id': '2e546d39-1259-fcc8-774e-424ec5179b35', 'detail-type': 'Scheduled Event', 'source': 'aws.events', 'time': '2022-08-11T22:30:00Z', 'region': 'ca-central-1', 'detail': {}}

# lambda_handler(firstSchedulerEvent,  {})
lambda_handler(firstSchedulerEvent, {})