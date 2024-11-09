from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print("test",content)
        toml_content = toml.loads(content)
        #print("test_toml",toml_content)
        toml_name = toml_content['tool']['poetry']['name']
        toml_description = toml_content['tool']['poetry']['description']
        toml_licence = toml_content['tool']['poetry']['license']
        toml_authors = toml_content['tool']['poetry']['authors']
        toml_dependencies = toml_content['tool']['poetry']['dependencies']
        toml_dependencies_dev = toml_content['tool']['poetry']['group']['dev']['dependencies']
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(toml_name, toml_description, toml_licence, toml_authors, toml_dependencies, toml_dependencies_dev)
