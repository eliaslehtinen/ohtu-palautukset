import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        projectToml = toml.loads(content)
        poetryData = projectToml["tool"]["poetry"]
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(poetryData["name"], poetryData["description"], poetryData["dependencies"], poetryData["group"]["dev"]["dependencies"])
