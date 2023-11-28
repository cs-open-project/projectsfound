from unittest import TestCase

from content import read_project


class Test(TestCase):
    def test_read_project(self):
        project = read_project("Yetus (Dormant)[软件库集合]", "Description: sss", "介绍: 这是...")

        if project["name"] != "Yetus (Dormant)":
            self.fail("name is wrong {}".format(project["name"]))
