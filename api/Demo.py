# import jenkinsapi.jenkins  as jenkins

# server = jenkins.Jenkins('http://localhost:8080', username='admin', password='admin')
# # user = server.get_whoami()
# version = server.get_create_url()
# # print('Hello %s from Jenkins %s' % (user['fullName'], version))
# print(version)


import jenkinsapi
from jenkinsapi.jenkins import Jenkins
jenkins = Jenkins('http://localhost:8080', username='admin', password='admin')
# print(J.version)
# print(J.get_jobs)

# print(jenkins.items())
# print(type(jenkins.items()))

jenkins_job_list = jenkins.items()
print(len(jenkins_job_list))


for job_details in jenkins_job_list:
    # print(type(job_details))
    for job in job_details:
        print(job)


# for job in J.keys:
#     print(job)

# J.keys() # Jenkins objects appear to be dict-like, mapping keys (job-names) to
# J['test_jenkinsapi']
# J['test_jenkinsapi'].get_last_good_build()
