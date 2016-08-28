from evennia import Command as BaseCommand
from evennia import default_cmds


class cmdSayOOC(default_cmds.MuxCommand):
	"""
	Say something out of character at your current location.
	
	usage:
	sooc <text>
	"""
	
	key = "sooc"
	aliases = ['"ooc', "'ooc", "."]
	help_category = "general"
	
	def func (self):
		
		caller = self.caller

		if not self.args:
			caller.msg("Say what?")
			return

		speech = self.args
		

		# calling the speech hook on the location
		speech = caller.location.at_say(caller, speech)
		if caller.db.colorname:
			# Feedback for the object doing the talking.
			caller.msg('{R(OOC){n %s {gsays, {y"{w%s{y"' % (caller.db.colorname,
                                               speech))

			# Build the string to emit to neighbors.
			emit_string = '{R(OOC){n %s {gsays, {y"{w%s{y"' % (caller.db.colorname,
											   speech)
											   
		else:
			# Feedback for the object doing the talking.
			caller.msg('{R(OOC){n %s {gsays, {y"{w%s{y"' % (caller.name,
                                               speech))

			# Build the string to emit to neighbors.
			emit_string = '{R(OOC){n %s {gsays, {y"{w%s{y"' % (caller.name,
											   speech)

		
		caller.location.msg_contents(emit_string,
									 exclude=caller)