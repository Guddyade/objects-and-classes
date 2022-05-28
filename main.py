class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, track, score):
        self.name= str(name)
        self.age = int(age)
        self.tracks = list(track)
        self.score = float(score)


#Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
def change_name (self, name):
    self.name = name

def change_age(self, age):
    self.age = age

def add_tracks(self, strong):
    self.track.append(strong)

def get_score(self):
    return self.score

Bob = Student("Bob", 26, ["FE", "BE"], 20.9)


# Expected methods
# Bob.change_name("Peter")
# Bob.change_age(34)
# Bob.add_track("UI/UX")
# Bob.get_score()

