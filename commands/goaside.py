from evennia import Command as BaseCommand
from evennia import default_cmds
from evennia.utils import create, utils, search

class cmdGoAside(default_cmds.MuxCommand):
    """
    goaside
    
    Create an empty, private room that doesn't link anywhere else. Used for quick, private scenes that are location-agnostic.
    
    usage:
    goaside
    """
    
    key = "goaside"
    help_category = "general"
    
    def func (self):
        
        if not self.caller.db.hasgoaside:
            name = "%s's Private Room" % self.caller.name
            
            create.create_object("typeclasses.rooms.Room", name, report_to=self.caller)
            self.caller.db.hasgoaside = "YES"
        
        target = self.caller.search("%s's Private Room" % self.caller.name, global_search=True)
        self.caller.move_to(target)