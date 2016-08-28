from evennia import Command as BaseCommand
from evennia import default_cmds
from evennia.utils.evmenu import EvMenu

class cmdBuildingApplication(default_cmds.MuxCommand):

	key = "buildingapp"
	aliases = ["buildingapplication", "builderapp", "builderapps"]
	help_category = "building"
	
	def func(self):
		EvMenu(self.caller, "world.builderapp", startnode="start", cmdset_mergetype="Replace", cmdset_priority=1, auto_quit=True, cmd_on_exit="look", persistent=False)
		
class cmdBuildingReview(default_cmds.MuxCommand):

	key = "buildingreview"
	help_category = "building"
	locks = "cmd:perm(Wizards)"
	
	def func(self):
		EvMenu(self.caller, "world.builderreview", startnode="start", cmdset_mergetype="Replace", cmdset_priority=1, auto_quit=True, cmd_on_exit="look", persistent=False)