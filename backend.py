# encoding:utf-8


class BackendDeveloper(object):
    company = "LPS Ingenieria"
    team = "LPStech"

    def __init__(self, first_name, last_name, knowledges):
        self.first_name = first_name
        self.last_name = last_name
        self.knowledges = knowledges

        self.key_requirements = ('python', 'django', 'motivation', 'software')
        self.other_requirements = ('djangorestframework', 'git', 'teamwork', 'linux', 'REST', 'star wars')

    @property
    def score(self):
    	result = 0
    	#if my knowledges are contained in key_req, then each skill will be 3 points
    	#if my knowledges are contained in other_req, then each skill will be 1 point
    	#otherwise there will not be any puntuation
    	for x in self.knowledges:
    		if x in self.key_requirements:
    			result = result + 3
    		elif x in self.other_requirements:
    			result = result + 1

        return result
        
    def i_am_ready(self):
        if self.score > 7:
            print ("Make a pull request with this code, we want you!")
        else:
            print ("Wait, you have created successfully the score method? Then make a pull request, we want you!")

if __name__ == "__main__":
    #defining my skills
    knowledges = ('python','django','motivation','djangorestframework','software','REST','stars wars', 'linux','teamwork') 
    #creating object
    Me = BackendDeveloper('Javier', 'Fernandez', knowledges)
    # calling that function in order to check whether or not I fulfill the requierments. 
    Me.i_am_ready()
    
