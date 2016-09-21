"""
Command for adding stuff to the recursive dict. wip

"""

from evennia import Command as BaseCommand
from evennia import default_cmds

class cmdRecdict(default_cmds.MuxCommand):
    """
    help file goes here when done
    
    Usage:
    
    To add a desc:
    recdict <flag>=<desc>
    
    Reading descs:
    recdict read=<flag>
    
    To list descs:
    recdict list
    """
    key = "recdict"
    help_category= "building"
    
    def func(self):
        #target the recursivedesc storage item, error if it can't be
        target = self.caller.search("recursivedesc", global_search=True)
        if not target:
            self.caller.msg("The recursivedesc item was not found. You have either not created it, or it has been deleted.")
        
        #initialize the item if it isn't already
        if not target.db.descs:
            target.db.descs = {}
            
        #List the already created things if args are "list"
        if self.args == "list":
            #this can definitely be made prettier/user readable with some effort later on
            self.caller.msg(target.db.descs.keys())
        
        #If the lhs is 'read', show the desc on the otherside
        #TODO: error handling
        if self.lhs == "read":
            self.caller.msg("%s" % target.db.descs["%s" % self.rhs])
            
            
        #if none of the above, we assume it's a new desc name
        if self.lhs != "list" and self.lhs != "read":
            target.db.descs["%s" % self.lhs] = self.rhs
            self.caller.msg("Description added as flag '%s'." % self.lhs)
            
        #if no args supplied
        if not self.args:
            self.caller.msg("No args given. Type 'help recdict' for help.")