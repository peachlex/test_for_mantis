import random

from model.project import Project


def test_delete_project(app, db):
    if len(db.get_projects_list()) == 0:
        app.project.add_project(Project(name=app.project.random_name(6), status='release', view_status='public', description="TestProjectDescription"))
    old_projects = db.get_projects_list()
    project = random.choice(old_projects)
    app.project.delete_project(project)
    new_projects = db.get_projects_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert old_projects == new_projects
