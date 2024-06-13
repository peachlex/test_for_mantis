from selenium.webdriver.support.ui import Select

from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def fill_project_info(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        wd.find_element_by_name("status").click()
        Select(wd.find_element_by_name("status")).select_by_visible_text(project.status)
        n = self.get_status(project.status)
        wd.find_element_by_xpath("//option[@value='{}']".format(n)).click()
        wd.find_element_by_name("view_state").click()
        n = self.get_view_status(project.view_status)
        wd.find_element_by_xpath("//tr[5]/td[2]/select/option[{}]".format(n)).click()
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    @staticmethod
    def get_view_status(view_status):
        return 1 if view_status == "public" else 2

    def add_project(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_css_selector("input[value='Create New Project'").click()
        self.fill_project_info(project)
        wd.find_element_by_css_selector("input[value='Add Project'").click()

    @staticmethod
    def get_status(status):
        n = 10
        if status == "release":
            n = 30
        elif status == "stable":
            n = 50
        elif status == "obsolete":
            n = 70
        return n
