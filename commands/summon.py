from evennia import Command as BaseCommand
from evennia import default_cmds

class cmdSummon(default_cmds.MuxCommand):
    """
    summon
    
    Summon another player to your location with their permission.
    
    usage:
    summon <player>
    
    When summoned:
    
    join
    """
    
    key = "summon"
    aliases = ["msummon"]
    help_category = "wizards"
    
    def func (self):
        caller = self.caller
        args = self.args
        summonloc = caller.location

        if not args:
            caller.msg("Error: no character. Usage: summon <character>.")
            return

        target = caller.search(args, global_search=True, typeclass="typeclasses.characters.Character")

        if not target:
            caller.msg("Error: character not found.")
            return
        if target:    
            target.msg("%s" % caller + " wants to summon you to %s" % summonloc + ". To accept, type 'join'.")
            target.db.joinloc = summonloc
            caller.msg("You offer to summon %s" % target + " to your location.")

class cmdJoin(default_cmds.MuxCommand):
    """
    join
    
    Accept a summon that has been offered to you by another player.
    
    usage:
    join
    """
    
    key = "join"
    aliases = ["mjoin"]
    help_category = "wizards"
    
    def func (self):
        caller = self.caller
        args = self.args

        if not caller.db.joinloc:
            caller.msg("Nobody has summoned you, or your last summon expired.")
            return
            
        caller.move_to(caller.db.joinloc)
        del caller.db.joinloc