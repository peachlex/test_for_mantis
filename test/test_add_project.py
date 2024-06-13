from model.project import Project


def test_add_project(app, db):
    old_projects = db.get_projects_list()
    project = Project(name=app.project.random_name(6), status='development', view_status='public', description="TestProjectDescription")
    app.project.add_project(project)
    new_projects = db.get_projects_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
