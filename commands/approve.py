from evennia import Command as BaseCommand
from evennia import default_cmds

class cmdApprove(default_cmds.MuxCommand):
	"""
	For wizards only. Used to approve a character for access to a zone.
	
	Usage:
	
	appove <name>=<zone>
	
	Applicable zones:
	
	Azeroth
	Earth
	Orbit
	"""
	
	key = "approve"
	aliases = ["+approve"]
	help_category = "wizards"
	lock = "cmd: perm(Wizards)"
	def func (self):
		if "=" not in self.args:
			self.caller.msg("Syntax error. Check 'help approve' for help.")
			return
		else:
			target = self.caller.search(self.lhs, global_search=True, typeclass="typeclasses.characters.Character")
			if not self.rhs == "Azeroth" and not self.rhs == "Earth" and not self.rhs == "Orbit":
				self.caller.msg("I don't recognize that zone.")
				return
			if not target:
				self.caller.msg("I don't recognize that player.")
				return
			
			
			if self.rhs == "Azeroth":
				target.db.azeroth = "yes"
				self.caller.msg("Player " + self.lhs + " approved for zone " + self.rhs + ".")
				target.msg("You have been approved to play in the Azeroth zone.")
			if self.rhs == "Earth":
				target.db.earth = "yes"
				self.caller.msg("Player " + self.lhs + " approved for zone " + self.rhs + ".")
				target.msg("You have been approved to play in the Earth zone.")
			if self.rhs == "Orbit":
				target.db.orbit = "yes"
				self.caller.msg("Player " + self.lhs + " approved for zone " + self.rhs + ".")
				target.msg("You have been approved to play in the Orbit zone.")