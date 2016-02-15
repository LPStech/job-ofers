# encoding:utf-8


class BackendDeveloper(object):
    company = "LPS Ingenieria"
    team = "LPStech"
    job_url = "http://lpsingenieria.com/buscamos-desarrolladores-web/"

    def __init__(self, first_name, last_name, github, linkedin, knowledges):
        self.first_name = first_name
        self.last_name = last_name
        self.github = github
        self.linkedin = linkedin
        self.knowledges = knowledges

        self.key_requirements = ('python', 'django', 'motivation', 'software')
        self.other_requirements = ('djangorestframework', 'git', 'teamwork', 'linux', 'REST', 'star wars')

    @property
    def score(self):
        """
            Write the code to match the perfect candidate with the requirements above!
                Output should be 10 or more for perfect matches
                Output should be 0 for candidates that do not fulfill any requirements
        """
        # scores va sobre 100 (40 de key_requirements 60 de other_requirements) para que la salida sea mas de 10
        # (Output should be 10 or more for perfect matches)
        scores = 0
        for item in self.knowledges:
            if self.key_requirements.count(item) or self.other_requirements.count(item):
                scores += 10  # output should be 10 or more for perfect matches
        return scores

    def i_am_ready(self):
        if self.score > 7:
            print ("Make a pull request with this code, we want you!")
        else:
            print ("Wait, you have created successfully the score method? Then make a pull request, we want you!")


if __name__ == "__main__":
    """
        Write the code to create yourself, a BackendDeveloper, and let us know you are ready!
    """
    first_name = "Itziar"
    last_name = "Polo Martinez"
    email = "itziar276@gmail.com"
    github = "https://github.com/itziar"
    linkedin = "https://es.linkedin.com/in/itziar-polo-martinez-6219a354"
    knowledges = ["python", "django", "motivation", "software", "git", "teamwork", "linux"]
    me = BackendDeveloper(first_name, last_name, github, linkedin, knowledges)
    me.i_am_ready()
