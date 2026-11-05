
class Model:
  def __init__(self):
        

    self.directory = [
       { "firstname" : "rayane", "familyname": "rahmani", "tel": "0656191027"},
        {"firstname" : "ahmed","familyname": "mahdi", "tel": "0656191027"},
        {"firstname"  : "hamid","familyname": "katibi", "tel": "0656191027"},
        {"firstname": "mahmoud","familyname": "brahimi", "tel": "0656191027"}
        ]

  def search (self, name):

        nb_found = 0
        persons = [] 
        for person in self.directory:
            if person["familyname"] == name:
                persons.append(person)
                nb_found = nb_found + 1
        if nb_found == 0:
            print(f"there is no information about {name} in this annuaire")
        return persons



class View:
   def __init__(self):
      pass
   def input (self):
      print ("finding a telephone")
      print ("give a name")
      name = input()
      return name

   def output (self, person):
      print ("list of found names")

      print (f"we found {len(person)} person")
      for p in person:
          print (f"{p['firstname']} {p['familyname']} {p['tel']}")



def controller():
   data_model = Model()
   my_viewer = View()

   name = my_viewer.input()
   persons = data_model.search(name)
   my_viewer.output(persons)


if __name__ == "__main__":
    controller()