from django.test import TestCase
from Job_Tech import models
from Job_Tech.models import StudentJobs
# Create your tests here.

class URLTests(TestCase):
    #check urls of a local server pages
    def test_homepage(self):
        response=self.cilent.get('/')
        self.assertEqual(response.status_code, 200)
    def test_loginpage(self):
        response=self.cilent.get('login/')
        self.assertEqual(response.status_code, 200)
    def test_registerpage(self):
        response=self.cilent.get('register/')
        self.assertEqual(response.status_code, 200)
    def test_profilepage(self):
        response=self.cilent.get('profile/')
        self.assertEqual(response.status_code, 200)
    def test_deletepage(self):
        response=self.cilent.get('delete/<int:id>')
        self.assertEqual(response.status_code, 200)
    def test_editpage(self):
        response=self.cilent.get('edit/<int:id>')
        self.assertEqual(response.status_code, 200)
    def test_page(self):
        response=self.cilent.get('/')
        self.assertEqual(response.status_code, 200)
    def test_studentjobpage(self):
        response=self.cilent.get('studentjob/')
        self.assertEqual(response.status_code, 200)
    def test_addpage(self):
        response=self.cilent.get('add/')
        self.assertEqual(response.status_code, 200)
    def test_viewjobspage(self):
        response=self.cilent.get('<int:id>')
        self.assertEqual(response.status_code, 200)
    def test_logoutpage(self):
        response=self.cilent.get('logout/')
        self.assertEqual(response.status_code, 200)
    def test_jobseekerpage(self):
        response=self.cilent.get('jobseeker/')
        self.assertEqual(response.status_code, 200)
    def test_profileseekerpage(self):
        response=self.cilent.get('profileseeker/')
        self.assertEqual(response.status_code, 200)
    def test_deletepage(self):
        response=self.cilent.get('delete/')
        self.assertEqual(response.status_code, 200)
    def test_searchjobpage(self):
        response=self.cilent.get('searchjob/')
        self.assertEqual(response.status_code, 200)
    def test_job_submissionpage(self):
        response=self.cilent.get('job_submission/')
        self.assertEqual(response.status_code, 200)
    def test_allhrpage(self):
        response=self.cilent.get('allhr/')
        self.assertEqual(response.status_code, 200)
    def test_portfolio_hrpage(self):
        response=self.cilent.get('portfolio_hr/')
        self.assertEqual(response.status_code, 200)

class TestAppModels(TestCase):
    def test_model_studentjobs(self):
        title=StudentJobs.objects.create(title="Django Testing")
        desc=StudentJobs.objects.create(title="some desc")
        company=StudentJobs.objects.create(title="some company")
        location=StudentJobs.objects.create(title="some location")
        self.assertEqual(str(title),"Django Testing")
        self.assertEqual(str(desc),"some desc")
        self.assertEqual(str(company),"some company")
        self.assertEqual(str(location),"some location")


