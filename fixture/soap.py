from suds.client import Client
from suds import WebFault

from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        url = self.app.config["web"]["baseUrl"]
        client = Client(url + 'api/soap/mantisconnect.php?wsdl')
        try:
            client.service.mc_login(username,password)
            return True
        except WebFault:
            return False

    def get_projects_list(self, username, password):
        url = self.app.config["web"]["baseUrl"]
        client = Client(url + 'api/soap/mantisconnect.php?wsdl')

        def convert(project):
            return Project(project_id=str(project.id), name=project.name)
        try:
            list_projects = client.service.mc_projects_get_user_accessible(username, password)
            return list(map(convert, list_projects))
        except WebFault:
            return False
