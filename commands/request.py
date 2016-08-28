"""
"""
from evennia import Command as BaseCommand
from evennia import default_cmds
from evennia.utils import evtable
from evennia.utils.evmenu import EvMenu

class cmdRequest(default_cmds.MuxCommand):
	"""
	Request system. This is for players to submit support tickets,
	which wizards can access and respond to.
	"""
	
	key = "request"
	help_category = "general"
	
	def func(self):
		#All we do here is open the EvMenu world.request, everything else is handled there.
		EvMenu(self.caller, "world.request", startnode="start", cmdset_mergetype="Replace", cmdset_priority=1, auto_quit=True, cmd_on_exit="look", persistent=False)
class cmdRespond(default_cmds.MuxCommand):
	"""
	Respond to a request.
	
	Wizards only.
	"""
	
	key = "respond"
	locks = "cmd:perm(Wizards)"
	help_category = "general"
	
	def func(self):
		#All we do here is open the EvMenu world.respond, everything else is handled there.
		EvMenu(self.caller, "world.respond", startnode="start", cmdset_mergetype="Replace", cmdset_priority=1, auto_quit=True, cmd_on_exit="look", persistent=False)