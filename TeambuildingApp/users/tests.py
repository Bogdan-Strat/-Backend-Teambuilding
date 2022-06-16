from rest_framework.test import APITestCase

from TeambuildingApp.users.models import *

class TeamCreateTestCase(APITestCase):
    def test_create_product(self):
        initial_team_count = Team.objects.count()
        team_attrs = {
            'name' : 'New Team'
        }

        response = self.client.post('/api/v1/teams/new', team_attrs)
        if response.status_code != 201:
            print(response.data)
        self.assertEqual(
            Team.objects.count(),
            initial_team_count + 1,
        )

        for attr, expected_value in team_attrs.items():
            self.assertEqual(response.data[attr], expected_value)
