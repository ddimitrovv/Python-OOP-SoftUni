from unittest import TestCase, main

from project.team import Team


class TestTeam(TestCase):
    TEAM = 'Team'

    def setUp(self) -> None:
        self.team = Team(self.TEAM)

    def test_team_init__expected_correct_obj(self):
        result = self.team.name
        expected_result = self.TEAM
        self.assertEqual(result, expected_result)
        self.assertEqual(dict(), self.team.members)

    def test_team_incorrect_name__expected_exception(self):
        with self.assertRaises(ValueError) as error:
            self.team.name = 'Abc1'
        self.assertEqual("Team Name can contain only letters!", str(error.exception))

    def test_add_member__expected_correct_string_and_members(self):
        members = {'member 1': 15, 'member 2': 20, 'member 3': 25}
        actual = self.team.add_member(**members)
        expected = f"Successfully added: member 1, member 2, member 3"
        self.assertEqual(expected, actual)
        self.assertEqual(self.team.members, members)
        self.assertDictEqual(members, dict(self.team.members))

    def test_remove_member__member_exists__expected_member_to_be_removed(self):
        members = {'member 1': 15, 'member 2': 20, 'member 3': 25}
        self.team.add_member(**members)
        actual = self.team.remove_member('member 1')
        expected = f"Member member 1 removed"
        self.assertEqual(expected, actual)
        self.assertDictEqual({'member 2': 20, 'member 3': 25}, dict(self.team.members))

    def test_remove_member__member_does_not_exists__expected_member_to_be_removed(self):
        members = {'member 1': 15, 'member 2': 20, 'member 3': 25}
        self.team.add_member(**members)
        actual = self.team.remove_member('member 10')
        expected = f"Member with name member 10 does not exist"
        self.assertEqual(expected, actual)
        self.assertDictEqual(members, dict(self.team.members))

    def test_gt_expected_true(self):
        self.team.members = {'member 1': 15, 'member 2': 20, 'member 3': 25}
        team2 = Team('team')
        members = {'member 1': 15, 'member 2': 20}
        team2.add_member(**members)
        expected = True
        actual = self.team > team2
        self.assertEqual(expected, actual)

    def test_gt_expected_false(self):
        self.team.members = {'member 1': 15, 'member 2': 20, 'member 3': 25}
        team2 = Team('team')
        members = {'member 1': 15, 'member 2': 20, 'member3': 25, 'member4': 30}
        team2.add_member(**members)
        expected = False
        actual = self.team > team2
        self.assertEqual(expected, actual)

    def test_len__expected_len_of_team_members(self):
        members = {'member 1': 15, 'member 2': 20, 'member 3': 25}
        self.team.members = members
        expected = len(members)
        actual = self.team.__len__()
        self.assertEqual(expected, actual)

    def test_len__expected_zero_as_len_of_team_members(self):
        actual = self.team.__len__()
        self.assertEqual(0, actual)

    def test_add__expected_correct_obj(self):
        self.team.members = {'member1': 10, 'member2': 15}
        other_team = Team('other')
        other_team.members = {'member3': 20}
        new_team = self.team.__add__(other_team)
        self.assertEqual(f'Teamother', new_team.name)
        self.assertDictEqual({'member1': 10, 'member2': 15, 'member3': 20}, new_team.members)

    def test_team_str__expected_correct_str(self):
        self.team.members = {'member1': 10, 'member2': 15}
        expected = """Team name: Team
Member: member2 - 15-years old
Member: member1 - 10-years old"""
        actual = self.team.__str__()
        self.assertEqual(expected, actual)

    def test_team_str__without_members__expected_correct_str(self):
        expected = "Team name: Team"
        actual = self.team.__str__()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()
