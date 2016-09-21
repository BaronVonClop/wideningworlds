"""
Command sets

All commands in the game must be grouped in a cmdset.  A given command
can be part of any number of cmdsets and cmdsets can be added/removed
and merged onto entities at runtime.

To create new commands to populate the cmdset, see
`commands/command.py`.

This module wraps the default command sets of Evennia; overloads them
to add/remove commands from the default lineup. You can create your
own cmdsets by inheriting from them or directly from `evennia.CmdSet`.

"""

from evennia import default_cmds
from evennia import CmdSet
from commands import command
from commands import profile
from commands import fetlist
from commands import request
from commands import morph
from commands import approve
from commands import summon
from commands import plusOOC
from commands import buildingapp
from commands import goaside
from commands import sooc
from commands import namecolor
from commands import recdict
from commands import (
    override_look,
)

class CharacterCmdSet(default_cmds.CharacterCmdSet):
    """
    The `CharacterCmdSet` contains general in-game commands like `look`,
    `get`, etc available on in-game Character objects. It is merged with
    the `PlayerCmdSet` when a Player puppets a Character.
    """
    key = "DefaultCharacter"

    def at_cmdset_creation(self):
        """
        Populates the cmdset
        """
        super(CharacterCmdSet, self).at_cmdset_creation()
        self.add(profile.CmdViewProfile())
        self.add(request.cmdRequest)
        self.add(request.cmdRespond)
        self.add(profile.cmdEditplayer)
        self.add(fetlist.cmdFetlist)
        self.add(morph.cmdMorph)
        self.add(approve.cmdApprove)
        self.add(summon.cmdSummon)
        self.add(summon.cmdJoin)
        self.add(plusOOC.cmdPlusOoc)
        self.add(plusOOC.cmdPlusIC)
        self.add(buildingapp.cmdBuildingApplication)
        self.add(buildingapp.cmdBuildingReview)
        self.add(goaside.cmdGoAside)
        self.add(sooc.cmdSayOOC)
        self.add(namecolor.cmdNamecolor)
        self.add(override_look.CmdLook)
	self.add(recdict.CmdRecdict)
        #
        # any commands you add below will overload the default ones.
        #


class PlayerCmdSet(default_cmds.PlayerCmdSet):
    """
    This is the cmdset available to the Player at all times. It is
    combined with the `CharacterCmdSet` when the Player puppets a
    Character. It holds game-account-specific commands, channel
    commands, etc.
    """
    key = "DefaultPlayer"

    def at_cmdset_creation(self):
        """
        Populates the cmdset
        """
        super(PlayerCmdSet, self).at_cmdset_creation()
        #
        # any commands you add below will overload the default ones.
        #


class UnloggedinCmdSet(default_cmds.UnloggedinCmdSet):
    """
    Command set available to the Session before being logged in.  This
    holds commands like creating a new account, logging in, etc.
    """
    key = "DefaultUnloggedin"

    def at_cmdset_creation(self):
        """
        Populates the cmdset
        """
        super(UnloggedinCmdSet, self).at_cmdset_creation()
        #
        # any commands you add below will overload the default ones.
        #


class SessionCmdSet(default_cmds.SessionCmdSet):
    """
    This cmdset is made available on Session level once logged in. It
    is empty by default.
    """
    key = "DefaultSession"

    def at_cmdset_creation(self):
        """
        This is the only method defined in a cmdset, called during
        its creation. It should populate the set with command instances.

        As and example we just add the empty base `Command` object.
        It prints some info.
        """
        super(SessionCmdSet, self).at_cmdset_creation()
        #
        # any commands you add below will overload the default ones.
        #
