# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from tests.integration import IntegrationTestCase
from tests.integration.holodeck import Request
from twilio.http.response import Response


class StatisticsTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "cumulative": {
                    "avg_task_acceptance_time": 0.0,
                    "end_time": "2014-08-06T22:39:00Z",
                    "reservations_accepted": 0,
                    "reservations_rejected": 0,
                    "reservations_timed_out": 0,
                    "start_time": "2014-08-06T22:24:00Z",
                    "tasks_canceled": 0,
                    "tasks_entered": 0,
                    "tasks_moved": 0,
                    "tasks_timed_out_in_workflow": 0
                },
                "realtime": {
                    "longest_task_waiting_age": 0,
                    "longest_task_waiting_sid": null,
                    "tasks_by_status": {
                        "assigned": 1,
                        "pending": 0,
                        "reserved": 0
                    },
                    "total_tasks": 1
                },
                "workflow_sid": "WWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))
        
        self.twilio.taskrouter.v1.workspaces.get(sid="WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .workflows.get(sid="WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .statistics.fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows/WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Statistics'
        ))