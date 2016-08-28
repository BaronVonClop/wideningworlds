"""
Fetlist. Serves as replacement for wixxx from ProtoMUCK.

Much more flexible and includes categories, avoiding the dreaded "wixxxlump"
where people just throw virtually everything on their list in no real order.

"""

from evennia import Command as BaseCommand
from evennia import default_cmds

class cmdFetlist(default_cmds.MuxCommand):
	"""
	Read another player's fetlist.
	
	Usage:
	+fetlist <player>
	
	To edit your own:
	
	+fetlist <list>=<fetish>
	
	Accepted "lists" are "f" (Fave), "y" (Yes), and "m" (Maybe).
	
	Example:
	+fetlist f=bondage
	
	would add "bondage" to your "faves" list.
	
	To delete a tag:
	
	+fetlist delete=<tag>
	
	This will search your three lists for <tag> and remove it.
	
	To completely clear your fetlist:
	+fetlist clear
	
	This will **irreversibly** delete your whole fetlist, so be be certain
	you want to do that!
	
	By Applejack/Baron Von Clop.
	"""

	key = "+fetlist"
	aliases = ["fetlist", "wixxx", "+wixxx"]
	help_category= "fetlist"
	
	
	def func(self):
		#if an equals sign is not found and it isn't "clear", we assume it's a player name and search for it
		if "=" not in self.args and not self.args == "clear" and not self.lhs == "delete":
			#Target the player
			target = self.caller.search(self.args, global_search=True, typeclass="typeclasses.characters.Character")
			#if name is invalid, throw error message
			if not target:
				self.caller.msg("Sorry, I can't find a player named %s. Type 'help +fetlist' if you need help with syntax." % self.args)
			#If name is valid, display their fetlist
			else:
				#Find the longest list:
				# if (len(target.db.fetlistf) >= len(target.db.fetlisty)):
					# maxlength = len(target.db.fetlistf)
				# if (len(target.db.fetlisty) >= len(target.db.fetlistf)):
					# maxlength = len(target.db.fetlisty)
				# if (maxlength < target.db.fetlistm):
					# maxlength = len(target.db.fetlistm)
				
				#print beginning
				self.caller.msg("======= |015FAVE|n =======$======= |040YES|n ========$======= |550MAYBE|n ======$")
				#now let's print the rest
				maxlength = 50
				x=1
				while (x < maxlength):
					#if all three have an entry at fetlistn[x]
					if len(target.db.fetlistf) >= x and len(target.db.fetlisty) >= x and len(target.db.fetlistm) >= x:
						self.caller.msg('{:^20}'.format("%s" % (target.db.fetlistf[x-1])) + "$" + '{:^20}'.format("%s" % (target.db.fetlisty[x-1])) + "$" + '{:^20}'.format("%s" % (target.db.fetlistm[x-1])) + "$")
						x += 1
					#if only f and y have an entry at fetlistn[x]
					elif len(target.db.fetlistf) >= x and len(target.db.fetlisty) >= x:
						self.caller.msg('{:^20}'.format("%s" % (target.db.fetlistf[x-1])) + "$" + '{:^20}'.format("%s" % (target.db.fetlisty[x-1])) + "$" + '{:^20}'.format("") + "$")
						x += 1
					#if only y and m have an entry at fetlistn[x]
					elif len(target.db.fetlisty) >= x and len(target.db.fetlistm) >= x:
						self.caller.msg('{:^20}'.format("") + "$" + '{:^20}'.format("%s" % (target.db.fetlisty[x-1])) + "$" + '{:^20}'.format("%s" % (target.db.fetlistm[x-1])) + "$")
						x += 1
					#if only f and m have an entry at fetlistn[x]
					elif len(target.db.fetlistf) >= x and len(target.db.fetlistm) >= x:
						self.caller.msg('{:^20}'.format("%s" % (target.db.fetlistf[x-1])) + "$" + '{:^20}'.format("") + "$" + '{:^20}'.format("%s" % (target.db.fetlistm[x-1])) + "$")
						x += 1
					#if only m has an entry at fetlistn[x]
					elif len(target.db.fetlistm) >= x:
						self.caller.msg('{:^20}'.format("") + "$" + '{:^20}'.format("") + "$" + '{:^20}'.format("%s" % (target.db.fetlistm[x-1])) + "$")
						x += 1
					#if only y has an entry at fetlistn[x]
					elif len(target.db.fetlisty) >= x:
						self.caller.msg('{:^20}'.format("") + "$" + '{:^20}'.format("%s" % (target.db.fetlisty[x-1])) + "$" + '{:^20}'.format("") + "$")
						x += 1
					#if only f has an entry at fetlistn[x]
					elif len(target.db.fetlistf) >= x:
						self.caller.msg('{:^20}'.format("%s" % (target.db.fetlistf[x-1])) + "$" + '{:^20}'.format("") + "$" + '{:^20}'.format("") + "$")
						x += 1
					#catch to prevent infinite loop
					else:
						x +=1
						
					
					
				#print ending
				self.caller.msg("====================$====================$====================$")
				return
				
		#if +fetlist clear, clear all entries.
		if self.args == "clear":
			caller = self.caller
			del caller.db.fetlistf[:]
			del caller.db.fetlisty[:]
			del caller.db.fetlistm[:]
			caller.msg("Your kinks have been cleared.")
			return
		#if arg is "delete"
		if self.lhs == "delete":
			tag = self.rhs
			caller = self.caller
			found = None
			
			#check favorites
			if tag in caller.db.fetlistf:
				#if found, delete it
				caller.db.fetlistf.remove(tag)
				found = 1
			
			#check yes
			if tag in caller.db.fetlisty:
				#if found, delete it
				caller.db.fetlisty.remove(tag)
				found = 1
				
			#check maybe
			if tag in caller.db.fetlistm:
				#if found, delete it
				caller.db.fetlistm.remove(tag)
				found = 1
				
			#if anything matching was found
			if found == 1:
				#announce it was deleted
				caller.msg("%s has been deleted from your kinks!" % tag)
			#otherwise alert that nothing happened
			else:
				caller.msg("%s wasn't found in any of your lists. Did you spell it correctly? Case sensitive!" % tag)
				return
			return
		
		#add to favorites list
		if self.lhs == "f":
			caller = self.caller
		
			#Check length
			if not (len(self.rhs) <=20):
				self.caller.msg("That is too long! Additions must be <=20 characters.")
				return
			
			#Length passed, add to kink list
			caller.db.fetlistf.append(self.rhs)
			caller.msg("Added %s to your Favorites on fetlist." % self.rhs)
			
		#add to yes list
		if self.lhs == "y":
			caller = self.caller
			
			#Check length
			if not (len(self.rhs) <=20):
				self.caller.msg("That is too long! Additions must be <=20 characters.")
				return
			
			#Length passed, add to kink list
			caller.db.fetlisty.append(self.rhs)
			caller.msg("Added %s to your Yes on fetlist." % self.rhs)
			
		#add to maybe list
		if self.lhs == "m":
			caller = self.caller
			
			#Check length
			if not (len(self.rhs) <=20):
				self.caller.msg("That is too long! Additions must be <=20 characters.")
				return
			
			#Length passed, add to kink list
			caller.db.fetlistm.append(self.rhs)
			caller.msg("Added %s to your Maybe on fetlist." % self.rhs)
			
		#if not one of those three
		if not self.lhs == "f" and not self.lhs == "y" and not self.lhs == "m":
			self.caller.msg("That's not a supported category. Use 'f', 'y', or 'm'. Type 'help +fetlist' for help.")
			
		
		
		

#Everything below depreciated as of 8/6/2016. Kept just in case for now. Will be deleted soon.
		
# class cmdFetlistaddf(default_cmds.MuxCommand):
	# """
	# Add something to your favorites on fetlist.
	# """
	
	# key = "+fetlistaddf"
	# aliases = ["fetlistaddf", "wixxxaddf", "+wixxxaddf"]
	# help_category = "fetlist"
	
	# def func(self):
		
		# caller = self.caller
		
		# #Check length
		# if not (len(self.args) <=20):
			# self.caller.msg("That is too long! Additions must be <=20 characters.")
			# return
			
		# #Length passed, add to kink list
		# caller.db.fetlistf.append(self.args)
		# caller.msg("Added %s to your Favorites on fetlist." % self.args)
		
# class cmdFetlistaddy(default_cmds.MuxCommand):
	# """
	# Add something to your "yes" list on fetlist.
	
	# Usage:
	# +fetlistaddf <kink>
	# """
	
	# key = "+fetlistaddy"
	# aliases = ["fetlistaddy", "wixxxaddy", "+wixxxaddy"]
	# help_category = "fetlist"
	
	# def func(self):
		
		# caller = self.caller
		
		# #Check length
		# if not (len(self.args) <=20):
			# self.caller.msg("That is too long! Additions must be <=20 characters.")
			# return
			
		# #Length passed, add to kink list
		# caller.db.fetlisty.append(self.args)
		# caller.msg("Added %s to your Yes list on fetlist." % self.args)
		
# class cmdFetlistaddm(default_cmds.MuxCommand):
	# """
	# Add something to your "maybe" list on fetlist.
	
	# Usage:
	# +fetlistaddm <kink>
	# """
	
	# key = "+fetlistaddm"
	# aliases = ["fetlistaddm", "wixxxaddm", "+wixxxaddm"]
	# help_category = "fetlist"
	
	# def func(self):
		
		# caller = self.caller
		
		# #Check length
		# if not (len(self.args) <=20):
			# self.caller.msg("That is too long! Additions must be <=20 characters.")
			# return
			
		# #Length passed, add to kink list
		# caller.db.fetlistm.append(self.args)
		# caller.msg("Added %s to your Maybe list on fetlist." % self.args)
		
# class cmdFetlistclear(default_cmds.MuxCommand):
	# """
	# Clear all your kinks.
	
	# This will IRREVERSIBLY wipe out ALL of your kink list; be sure you want to do this!
	
	# Usage:
	# +Fetlistclear
	# """
	
	# key = "+fetlistclear"
	# aliases = ["fetlistclear", "wixxxclear", "+wixxxclear"]
	# help_category = "fetlist"
	
	# def func(self):
		
		# caller = self.caller
		# del caller.db.fetlistf[:]
		# del caller.db.fetlisty[:]
		# del caller.db.fetlistm[:]
		# caller.msg("Your kinks have been cleared.")
		
		
#DEPRECIATED CODE BELOW
#Used for the old system of tags and a main tag DB. No longer needed.
#Replaced in favor of the more flexible and far less frustrating "custom" tag system.
		
		
#class cmdFetlistnewtag(default_cmds.MuxCommand):
	# """
	# Add a tag to the Fetlist db.
	
	# Wizards only.
	
	# Usage:
	# +fetlistnewtag <tag>=<definition>
	# """
	
	# key = "+fetlistnewtag"
	# help_category = "fetlist"
	
	# def parse(self):
		# #split args into two things; tag and desc
		# tag, desc = None, None
		# if "=" in self.args:
			# tag, desc = [part.strip() 
							# for part in self.args.rsplit("=", 1)]
			# self.tag, self.desc = tag, desc
	
	# def func(self):
		
		# #target the fetlist master item
		# target = self.caller.search("fetlist")
		# #check length for stuff
		# if (len(self.tag) > 3):
			# self.caller.msg("Tag length too long. Must be <=3 characters.")
			# return
		# if (len(self.desc) > 20):
			# self.caller.msg("Description too long. Must be <=20 characters.")
			# return
		# #arg passed, let's commit it to the DB
		# target.db.fetlisttagdict["%s" % self.tag] = self.desc
		# target.db.fetlisttaglist.append(self.tag)
		# self.caller.msg("Tag %(1)s added with definition %(2)s" % {"1" : self.tag, "2" : self.desc})

# class cmdFetlisttags(default_cmds.MuxCommand):
	# """
	# View all tags.
	
	# Usage:
	# +fetlisttags
	# """
	# key = "+fetlisttags"
	# help_category = "fetlist"
	
	# def func(self):
		# #target fetlist master
		# target = self.caller.search("fetlist")

		# #if no args, display whole list
		# if not self.args:
			# #header
			# self.caller.msg("The following tags are in the database and available for use:")
			# #while loop for tags
			# x=0
			# tagnumber = len(target.db.fetlisttaglist)
			# while (x < tagnumber):
				# self.caller.msg("%s" % target.db.fetlisttaglist[x])
				# x += 1
		