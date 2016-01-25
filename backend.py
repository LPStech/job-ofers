# encoding:utf-8


class BackendDeveloper(object):
    company = "LPS Ingenieria"
    team = "LPStech"

    __author__ = "David Vicente Ranz"
    __email__ = "dvicente74@gmail.com"
    __phone__ = "+34 653 687 187"
    __github__ = "https://github.com/davidvicenteranz"
    __linkedin__ = "https://www.linkedin.com/in/david-vicente-8a9841b4"
    __twitter__ = "https://twitter.com/DVicenteR"
    __website__ = "http://davidvicenteranz.appspot.com/"

    def __init__(self, first_name, last_name, knowledges):
        self.first_name = first_name
        self.last_name = last_name
        self.knowledges = knowledges

        self.key_requirements = ('python', 'django', 'motivation', 'software')
        self.other_requirements = (
            'djangorestframework', 'git', 'teamwork', 'linux', 'REST', 'star wars')

    @property
    def score(self):
        """
            Write the code to match the perfect candidate with the requirements above!
                Output should be 10 or more for perfect matches
                Output should be 0 for candidates that do not fulfill any requirements
        """
        return len([req for req in list(set(self.knowledges)) if req in 
            self.key_requirements or req in self.other_requirements])

    def i_am_ready(self):
        if self.score > 7:
            print ("Make a pull request with this code, we want you!")
        else:
            print (
                "Wait, you have created successfully the score method? Then make a pull request, we want you!")

if __name__ == "__main__":
    """
        Write the code to create yourself, a BackendDeveloper, and let us know you are ready!
    """
    me = BackendDeveloper(
        'David',
        'Vicente Ranz',
        ['python',
         'django',
         'django', # just to test duplicates
         'motivation',
         'software',
         'djangorestframework',
         'git',
         'teamwork',
         'linux',
         'REST',
         'node.js',
         'GAE',
         'json',
         'mobile dev',
         'cloud',
         'mac os',
         'vps',
         'java',
         'c#',
         'javascript',
         'angular',
         'css',
         'coffeescript',
         'html5',
         'freelance',
         'remote worker',
         'much more',
         'star wars'])

    me.i_am_ready()

    # show contact information
    print """
Contact information for %s who has reached a score of %i
------------------------------------------------------------------------
email:  %s
phone:  %s
web:    %s
------------------------------------------------------------------------
IMPORTANT NOTE:
Only liked the first two and genuine Star Wars movies: 
A New Hope and The Empire Strikes Back
""" % (me.__author__, me.score, me.__email__, me.__phone__, me.__website__)
