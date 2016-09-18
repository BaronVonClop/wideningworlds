"""
Override for the look command
"""

from evennia.commands.default.general import CmdLook as DefaultCmdLook

class CmdLook(DefaultCmdLook):

    def func(self):
        target = self._get_target()
        if not target:
            self.caller.msg("You have no location to look at!")
            return
        
        


    def _get_target(self):
        """Gets the target of the look command from the args"""
        return (
            self.caller.search(self.args) 
            if self.args
            else self.caller.location
        )
        
