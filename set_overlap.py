COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

print(COURSES.keys())

def covers(topic):
  result = []
  keys = COURSES.keys()
  for i,course in enumerate(keys,start=0):
    new_set = topic & COURSES[course]
    if (len(new_set)):
      topic & COURSES[course]
    
    result.append(course)
      
    return result

def covers2(topic):
  result = []
  for course in COURSES.keys():
    topic & COURSES[course]
    result.append(course)
    return result
    
    

print(covers2({'Python'})) 
