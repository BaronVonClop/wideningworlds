"""
Profile system for brief looks at someone's character, without a long description. 'At a glance' profile.

Meant to replicate the +finger/+hoof system from ProtoMUCK/MUF.
"""


from evennia import Command as BaseCommand
from evennia import default_cmds
from evennia.utils.evmenu import EvMenu

class CmdViewProfile(default_cmds.MuxCommand):
    """
    View the profiles of others, as well as configure your own.
    
    usage:
    +profile <character>
    
    To edit yours:
    
    +profile <field>=<text>
    
    Acceptable fields:
    
    gender
    race
    age
    height
    weight
    coat
    mane
    cutiemark
    
    Example:
    
    +profile gender=Female
    
    Written by Applejack/Baron Von Clop
    """
    
    key = "+profile"
    help_category = "mush"
    aliases = ["hoof", "+hoof", "profile"]
    
    
    def func(self):
        errmsg = "That isn't a player name I recognize."
        caller = self.caller
        
        #if no equals sign, we assume it's a player, attempt to target it, and display profile for it.
        if "=" not in self.args:
            target = caller.search(self.args, global_search=True, typeclass="typeclasses.characters.Character")
            #If no result, give this
            if not target:
                return
            #If target found, then we display their profile.
            if target:
                self.caller.msg("  |303/=============================\\")
                self.caller.msg(" |303/===========|550 PROFILE |303===========\\")
                self.caller.msg("|303/=================================\\")
                self.caller.msg("%(1)s the %(2)s %(3)s" % {"1" : target.name, "2" : target.db.gender, "3" : target.db.race})
                self.caller.msg("       AGE: %s" % target.db.age)
                self.caller.msg("    HEIGHT: %s" % target.db.height)
                self.caller.msg("    WEIGHT: %s" % target.db.weight)
                self.caller.msg("      HAIR: %s" % target.db.hair)
                self.caller.msg(" COAT/SKIN: %s" % target.db.coat)
                self.caller.msg("PROFESSION: %s" % target.db.occupation)
                self.caller.msg("|303.=================================.")
        
        #If there is an = sign and the left hand side is == "race"
        if self.lhs == "race":
            errmsg = "You must supply a race under 20 characters."
            
            #If no right hand side, then error.
            if not self.rhs:
                self.caller.msg(errmsg)
                return
            #If >20 char, error.
            if not len(self.rhs) <= 20:
                caller.msg(errmsg)
                return
            #Otherwise, we apply the right hand side as their race.
            caller.db.race = self.rhs
            self.caller.msg("Your race was set to %s." % self.rhs)
            return
            
        if self.lhs == "gender":
            errmsg = "You must supply a gender under 20 characters."
            
            if not self.rhs:
                self.caller.msg(errmsg)
                return

            if not len(self.rhs) <= 20:
                caller.msg(errmsg)
                return

            caller.db.gender = self.rhs
            self.caller.msg("Your gender was set to %s." % self.rhs)
            return
            
        if self.lhs == "age":
            errmsg = "You must supply an age under 4 characters."
            
            if not self.rhs:
                self.caller.msg(errmsg)
                return

            if not len(self.rhs) <=4:
                caller.msg(errmsg)
                return

            caller.db.age = self.rhs
            self.caller.msg("Your age was set to %s." % self.rhs)
            return
            
        if self.lhs == "height":
            errmsg = "You must supply a height under 20 characters."
            
            if not self.rhs:
                self.caller.msg(errmsg)
                return

            if not len(self.rhs) <= 20:
                caller.msg(errmsg)
                return

            caller.db.height = self.rhs
            self.caller.msg("Your height was set to %s." % self.rhs)
            return
            
        if self.lhs == "weight":
            errmsg = "You must supply a weight under 20 characters."
            
            if not self.rhs:
                self.caller.msg(errmsg)
                return

            if not len(self.rhs) <= 20:
                caller.msg(errmsg)
                return

            caller.db.weight = self.rhs
            self.caller.msg("Your weight was set to %s." % self.rhs)
            return
        
        if self.lhs == "coat":
            errmsg = "You must supply a coat color under 20 characters."
            
            if not self.rhs:
                self.caller.msg(errmsg)
                return

            if not len(self.rhs) <= 20:
                caller.msg(errmsg)
                return

            caller.db.coat = self.rhs
            self.caller.msg("Your coat was set to %s." % self.rhs)
            return
            
        if self.lhs == "mane":
            errmsg = "You must supply a mane color under 20 characters."
            
            if not self.rhs:
                self.caller.msg(errmsg)
                return

            if not len(self.rhs) <= 20:
                caller.msg(errmsg)
                return

            caller.db.mane = self.rhs
            self.caller.msg("Your mane color was set to %s." % self.rhs)
            return
            
        if self.lhs == "cutiemark":
            errmsg = "You must supply a cutie mark under 20 characters."
            
            if not self.rhs:
                self.caller.msg(errmsg)
                return

            if not len(self.rhs) <= 20:
                caller.msg(errmsg)
                return

            caller.db.cutiemark = self.rhs
            self.caller.msg("Your cutie mark was set to %s." % self.rhs)
            return
class cmdEditplayer(default_cmds.MuxCommand):

    key = "editplayer"
    help_category = "profile"
    
    def func(self):
        EvMenu(self.caller, "world.editplayer", startnode="start", cmdset_mergetype="Replace", cmdset_priority=1, auto_quit=True, cmd_on_exit="look", persistent=False)