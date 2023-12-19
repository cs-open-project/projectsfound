from unittest import TestCase

from content import read_project, read_md


class Test(TestCase):
    def test_read_project(self):
        project = read_project("Yetus (Dormant)[软件库集合]", "Description: sss", "介绍: 这是...")

        if project["name"] != "Yetus (Dormant)":
            self.fail("name is wrong {}".format(project["name"]))

    def test_read_md(self):
        read_md()

    def test_split(self):
        name = "介绍: Apache CloudStack is open source software designed to deploy and manage large " \
               "networks of virtual machines, as a highly available, highly scalable Infrastructure as  " \
               "a Service (IaaS) cloud computing platform. CloudStack is used by a number of service  " \
               "providers to offer public cloud services, and by many companies to provide an  " \
               "on-premises (private) cloud offering, or as part of a hybrid cloud solution.  " \
               "CloudStack is a turnkey solution that includes the entire \"stack\" of features most  " \
               "organizations want with an IaaS cloud: compute orchestration, Network-as-a-Service,  " \
               "user and account management, a full and open native API, resource accounting, and a  " \
               "first-class User Interface (UI).  CloudStack currently supports the most popular hypervisors: " \
               "VMware, KVM, XenServer and  Xen Cloud Platform (XCP).  Users can manage their cloud with an easy " \
               "to use Web interface, command line tools, and  / or a full-featured RESTful API. In addition, " \
               "CloudStack provides an API that's  compatible with AWS EC2 and S3 for organizations that wish " \
               "to deploy hybrid clouds.".split(":", 2)[1].strip()
        print(name)
