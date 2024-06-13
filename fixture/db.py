import pymysql
from model.project import Project

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, db=name, user=user, password=password, autocommit=True)

    def get_projects_list(self):
        list_of_projects = []
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT id, name FROM mantis_project_table")
            for row in cursor:
                (id_project, project_name) = row
                list_of_projects.append(Project(project_id=str(id_project), name=project_name))
        return list_of_projects

    def destroy(self):
        self.connection.close()