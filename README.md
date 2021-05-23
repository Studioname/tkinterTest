# tkinterTest
Miles to km converter in tkinter

Main contains the unguided exercise, the other files are tutorial related. I say unguided, because there was no input from the instructor when it came to making
the app, we had to do it with what we had learned in the tutorial. And it went rather smoothly! I was happy to finally be working with GUI's. Turtle was fun but
very simple, and quite restrictive in places. Tkinter on the other hand seems like a big step up. Making things happen on screen is one of my favourite things
to do. In GML I loved working with the main surface - not that i'd edit it or anything, was a bit above my expertise at the time, although i did [with the help
of a couple of folks] manage to get a decent sprite baking operation going. So the rundown is I was making cards, and someone pointed out to me that baking card
data to a sprite using surfaces was the way to go. So I gave it a shot and it worked rather well. The operation went:

Create surface
Assign surface
Draw card background
Draw icons
Draw title/text
Bake to sprite
Assign sprite to skeleton [spine skeleton in this case]
Apply animation

There was no real 'baking' involved, because Spine does not bake animations... But still. The only reason I stopped working on the project was because as soon as I had
completed the game engine, I realised that while there was a game in there somewhere, I would have to rewrite a major part of it because there was a particular
part which stood out as being unfun. And I did not [and have since not had] the inspiration to replace or rework the particular part that I did not like. But I did complete a
fully functional, working game engine. There might be a name for that kind of phenomenon somewhere, but still. It's like raising a calf in a barn, which then gets too big for
the barn door, so to get the cow out you need to deconstruct the barn or part of it. My calf is still in that barn, along with the somehow functioning code I wrote... I mean,
I'm half amazed at the stuff I was doing in that project. At the best of it, I wrote a single button which did the work of 15 separate ones. [I was at the time under the illusion 
that less code = elegance]. I'm a big fan of dynamic programming, although I should probably invest into modular programming since that seems to be the way to write good code. 
