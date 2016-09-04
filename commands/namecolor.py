from evennia import Command as BaseCommand
from evennia import default_cmds
from evennia.utils.ansi import strip_ansi
from utils.message import syntax_error

class cmdNamecolor(default_cmds.MuxCommand):
    """
    Set your name color. This will make your name appear in whatever color you select when you use say or emote.
    
    usage:
    
    namecolor <name with ANSI color codes>
    
    This can be a bit complicated, so check the wiki for more info:
    
    Colors can be deleted with 'namecolor delete'. This will erase your name colors and return you to the default gray.
    """
    
    key = "namecolor"
    help_category = "general"
    
    def func (self):
        
        caller = self.caller
        
        #if they use an =, we know something is wrong
        if self.rhs:
            syntax_error(caller, self.key)
            return
            
        #if the arg is "delete", we just delete their name colors and ignore everything else
        if self.args == "delete":
            del caller.db.colorname
            return
            
        #strip the ANSI from the submitted name and make sure they aren't trying to impostor someone else    
        stripped = strip_ansi(self.args)
        #if the stripped name doesn't equal their name, error
        if stripped != caller.name:
            caller.msg("That name doesn't match yours! Your name must not change, only add color codes.")
            return
        
        if stripped == caller.name:
            caller.db.colorname = self.args
            caller.msg("Your name colors have been set to %s" % caller.db.colorname)
