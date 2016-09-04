"""
Morph system. Allows players to store descriptions and call them at will.
"""


from evennia import Command as BaseCommand
from evennia import default_cmds

class cmdMorph(default_cmds.MuxCommand):
    """
    MORPH
    
    Morph is used to quickly change between descriptions.
    
    As examples, it can be used to rapidly change your description to different sets of clothing, or different weights. Many people have both a "skinny" and a "fat" description.
    
    USAGE:
    
    morph <name>
    
    Morph your description to a saved morph.
    
    morph add=<name>
    
    Save your current description and profile as a morph that you can change to later.
    Naming your new morph the same as an existing morph will overwrite it.
    
    morph delete=<name>
    
    Delete a saved morph.
    
    morph list
    
    Show a list of your morphs.
    """

    key = "morph"
    aliases = ["morphs"]
    help_category = "profile"
    
    def func(self):
        #if there isn't an equals sign in the command and the command isn't "list", we assume they want to switch morphs.
        if "=" not in self.args and not self.args == "list":
            if self.args not in self.caller.db.morphs:
                self.caller.msg("That isn't one of your morphs. Type 'help morph' for help.")
            if self.args in self.caller.db.morphs:
                self.caller.db.desc = self.caller.db.morphsdict["%sdesc" % self.args]
                self.caller.db.race = self.caller.db.morphsdict["%srace" % self.args]
                self.caller.db.gender = self.caller.db.morphsdict["%sgender" % self.args]
                self.caller.db.age = self.caller.db.morphsdict["%sage" % self.args]
                self.caller.db.height = self.caller.db.morphsdict["%sheight" % self.args]
                self.caller.db.weight = self.caller.db.morphsdict["%sweight" % self.args]
                self.caller.db.hair = self.caller.db.morphsdict["%shair" % self.args]
                self.caller.db.coat = self.caller.db.morphsdict["%scoat" % self.args]
                self.caller.db.occupation = self.caller.db.morphsdict["%soccupation" % self.args]
                self.caller.msg("Your morph into your '%s' form." % self.args)
            return
            
        if self.args == "list":
            self.caller.msg("You currently have these morphs:|/")
            self.msg(", ".join(self.caller.db.morphs))
        
        if self.lhs == "add":
            self.caller.msg("Adding your current description as a morph named '%s'..." % self.rhs)
            self.caller.db.morphs.append(self.rhs)
            self.caller.db.morphsdict["%sdesc" % self.rhs] = self.caller.db.desc
            self.caller.db.morphsdict["%srace" % self.rhs] = self.caller.db.race
            self.caller.db.morphsdict["%sgender" % self.rhs] = self.caller.db.gender
            self.caller.db.morphsdict["%sage" % self.rhs] = self.caller.db.age
            self.caller.db.morphsdict["%sheight" % self.rhs] = self.caller.db.height
            self.caller.db.morphsdict["%sweight" % self.rhs] = self.caller.db.weight
            self.caller.db.morphsdict["%shair" % self.rhs] = self.caller.db.hair
            self.caller.db.morphsdict["%scoat" % self.rhs] = self.caller.db.coat
            self.caller.db.morphsdict["%soccupation" % self.rhs] = self.caller.db.occupation
            self.caller.msg("Morph added under the name '%s'." % self.rhs)
        
        if self.lhs == "delete":
            if self.rhs not in self.caller.db.morphs:
                self.caller.msg("No morph by that name.")
            if self.rhs in self.caller.db.morphs:
                self.caller.msg("Deleting the morph named '%s'..." % self.rhs)
                self.caller.db.morphs.remove(self.rhs)
                del self.caller.db.morphsdict["%sdesc" % self.rhs]
                del self.caller.db.morphsdict["%srace" % self.rhs]
                del self.caller.db.morphsdict["%sgender" % self.rhs]
                del self.caller.db.morphsdict["%sage" % self.rhs]
                del self.caller.db.morphsdict["%sheight" % self.rhs]
                del self.caller.db.morphsdict["%sweight" % self.rhs]
                del self.caller.db.morphsdict["%shair" % self.rhs]
                del self.caller.db.morphsdict["%scoat" % self.rhs]
                del self.caller.db.morphsdict["%soccupation" % self.rhs]
                self.caller.msg("Morph named '%s' sucessfully deleted." % self.rhs)