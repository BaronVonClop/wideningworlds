"""
Creation of a request/ticket system. Theoretically, this should only need to be called once ever with:

@create/drop request:requests.request

Theoretically this can be made with a create_object "setup" command, but that's way too elegant for me.

GUARD THE CREATED ITEM WITH YOUR LIFE, it hosts all the bboard posts. Deletion or modification means all your bboard posts are deleted.

You must also have NOTHING else named exactly "request" in the game.
"""

from typeclasses.objects import Object
    
class request(Object):
    def at_object_creation(self):
        self.db.requestnum = 1
        self.db.requestdict = {'reqtext0': None, 'reqtitle0': None, 'reqauthor0': None, 'isclosed0': 1, 'reqtime0': None}