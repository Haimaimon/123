from Job_Tech import models
from django.test import TestCase
from .forms import UserCreationForm, HrForm, JobSeekerForm, AllJobsForm, StudentJobForm, FileUploadForm
from Job_Tech.models import StudentJobs, Hr, JobSeeker, FileModel, AllJob


class UserCreationFormTestCase(TestCase):
    def test_form_validation(self):
        # Create a new form with valid data
        form = UserCreationForm({
            'username': 'nir',
            'email': 'nir@gmail.com',
            'password1': 'nir12345',
            'password2': 'nir12345',
            'status': 'Hr',
        })

        # Check that the form is valid
        self.assertTrue(form.is_valid())

        # Create a new form with invalid data
        form = UserCreationForm({
            'username': '...',
            'email': 'nir@gmail.com',
            'password1': 'nir12345',
            'password2': 'nir12345',
            'status': 'hr',
        })

        # Check that the form is invalid
        self.assertFalse(form.is_valid())


class TestAppModels(TestCase):
    def test_model_studentjobs(self):
        title = StudentJobs.objects.create(title="Django Testing")
        desc = StudentJobs.objects.create(title="some desc")
        company = StudentJobs.objects.create(title="some company")
        location = StudentJobs.objects.create(title="some location")
        self.assertEqual(str(title), "Django Testing")
        self.assertEqual(str(desc), "some desc")
        self.assertEqual(str(company), "some company")
        self.assertEqual(str(location), "some location")


class TestAppModels(TestCase):
    def test_model_hr(self):
        name = Hr.objects.create(title="nir")
        phone = Hr.objects.create(title="0555555555")
        email = Hr.objects.create(title="nir@gmail.com")
        placejob = Hr.objects.create(title="apple")
        usertype = Hr.objects.create(title="Hr")
        self.assertEqual(str(name), "nir")
        self.assertEqual(str(phone), "0555555555")
        self.assertEqual(str(email), "nir@gmail.com")
        self.assertEqual(str(placejob), "apple")
        self.assertEqual(str(usertype), "Hr")


class TestAppModels(TestCase):
    def test_model_jobseeker(self):
        name = JobSeeker.objects.create(title="mak")
        phone = JobSeeker.objects.create(title="0555555533")
        email = JobSeeker.objects.create(title="mak@gmail.com")
        education = JobSeeker.objects.create(title="Software Engineering")
        wordwithinitiator = JobSeeker.objects.create(title="No")
        user_type = JobSeeker.objects.create(title="JobSeeker")
        self.assertEqual(str(name), "mak")
        self.assertEqual(str(phone), "0555555533")
        self.assertEqual(str(email), "mak@gmail.com")
        self.assertEqual(str(education), "Software Engineering")
        self.assertEqual(str(wordwithinitiator), "No")
        self.assertEqual(str(user_type), "JobSeeker")


class TestAppModels(TestCase):
    def test_model_file(self):
        desc_file = FileModel.objects.create(title="שלום לכולם")
        file = FileModel.objects.create(title="Graphs_1slidePerPage_6Kv1AAl.pdf")
        self.assertEqual(str(desc_file), "שלום לכולם")
        self.assertEqual(str(file), "Graphs_1slidePerPage_6Kv1AAl.pdf")


class TestAppModels(TestCase):
    def test_model_alljob(self):
        title = AllJob.objects.create(title="QA")
        desc = AllJob.objects.create(title="...")
        company = AllJob.objects.create(title="apple")
        location = AllJob.objects.create(title="USA")
        age = AllJob.objects.create(title=+35)
        self.assertEqual(str(title), "QA")
        self.assertEqual(str(desc), "...")
        self.assertEqual(str(company), "apple")
        self.assertEqual(str(location), "USA")
        self.assertEqual(str(age), "+35")


class FormsTestCase(TestCase):
    def test_hr_form(self):
        form_data = {'name': 'nir', 'phone': '0555555555', 'email': 'nir@gmail.com',
                     'placejob': 'apple', 'usertype': 'hr'
                     }
        form = HrForm(data=form_data)
        self.assertTrue(form.is_valid())

        form_data = {'name': 'hai', 'phone': '0555555533', 'email': 'nir@gmail.com',
                     'placejob': 'dell', 'usertype': 'hr'}
        form = HrForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_jobseeker_form(self):
        form_data = {'name': 'mak', 'phone': '0555558888', 'email': 'mak@gmail.com',
                     'education': 'Software Engineering', 'wordwithinitiator': 'no', 'user_type': 'JobSeeker'}
        form = JobSeekerForm(data=form_data)
        self.assertTrue(form.is_valid())

        form_data = {'name': 'marko', 'phone': '0555558888', 'email': 'mak@gmail.com',
                     'education': 'Software Engineering', 'wordwithinitiator': 'yes', 'user_type': 'JobSeeker'}
        form = JobSeekerForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_alljob_form(self):
        form_data = {'title': 'QA', 'desc': '5 שנות ניסיון', 'company': 'Dell',
                     'location': 'תל אביב', 'age': +35}
        form = AllJobsForm(data=form_data)
        self.assertTrue(form.is_valid())

        form_data = {'title': 'developer', 'desc': '5 שנות ניסיון', 'company': 'apple',
                     'location': 'תל אביב', 'age': +35}
        form = AllJobsForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_studentjob_form(self):
        form_data = {'title': 'QA', 'desc': '10 שנות ניסיון', 'company': 'amdox', 'location': 'תל אביב'}
        form = StudentJobForm(data=form_data)
        self.assertTrue(form.is_valid())

        form_data = {'title': '...', 'desc': '10 שנות ניסיון', 'company': '...', 'location': 'תל אביב'}
        form = StudentJobForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_fileupload_form(self):
        form_data = {'desc_file': 'שלום לכולם', 'file': 'Graphs_1slidePerPage_6Kv1AAl.pdf'}
        form = FileUploadForm(data=form_data)
        self.assertTrue(form.is_valid())

        form_data = {'desc_file': '...', 'file': '...'}
        form = FileUploadForm(data=form_data)
        self.assertFalse(form.is_valid())


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


