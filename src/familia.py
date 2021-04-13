from random import randint

class Losperez:
    
    def __init__(self, last_name):
        self.last_name = last_name
        #example list of members
        self._members = [
            {
                "id" :  self._getRandomId(),
                "first_name" : "Gilberto",
                "last_name" : last_name,
                "age"   : 50,
                "children" : []
            }
        ]
    # read-only: Use this method to generate random members ID's when adding members into the list
    
    def _getRandomId(self):
        return randint(0, 99999999)
    def getAllMembers(self):
        return self._members
    def getSingleMember(self, id):
        #write a loop that will loop through self._members
        for member in self._members:
            #write a conditional to check that member['id'] matches id passed
            if member['id'] == id:
                return member
        return None

    def createFamilyMember(self, firstname, age, parent_id):
        family_member = {
            "id"    :   self._getRandomId(),
            "first_name"    :   firstname,
            "last_name"     :   self.last_name,
            "age"           :   age,
            "children"     :   []
        }
        current_family_members = self._members
        for idx, member in enumerate(current_family_members):
            if member['id'] == int(parent_id):
                self._members[idx]['children'].append(family_member['first_name'])
        self._members.append(family_member)
        return family_member