Multiple-Choice Game Engine
===========================

This is a very simple text-based multiple-choice game which
parses an easy-to-read plot-file syntax. An embedded language to support more
complex game logic (variables, conditional text or choices, functions)
is planned, but not supported jet.

Plot-File Syntax
----------------

You can add any number of scenes to a plot-file. Each new scene is preceded by
a label (e.g. `[scene_name]`) followed by a description text. The first scene
does not need a label. It is labeled 'start' automatically. Example::

  You open the door and see nothing but black darkness.
  You have a strange feeling about this.

  [room] You are dead now. No one will ever know why.

Scenes alone don't make a good story. You need a way to proceed from scene to
scene, best by giving the player a choice. This is why labels are so
important. You can link to them::

  You open the door and see nothing but black darkness.
  You have a strange feeling about this.
  
  <room> Close your eyes and enter the room.
  <torch> Light a torch.
  
  [room] You are dead now. No one will ever know why.
  
  [torch] The room has no floor, but a deep pit with spears in it.
  Thank god you didn't step inside.

Now the player has a choice. By the way: As soon as the player reaches a scene
that has no further choices, the game ends.

Writing deeply nested plots and especially conversations can get confusing
quickly. There is an alternative syntax which allows you to define the
target-scene of a choice in-place. You just have to begin the link with '?'
instead of a link-target and add the target scene indented with space
characters. You don't have to assign a label to the nested scene, but you can,
if you want to jump to it from another scene, too. Here is an example::

  You open the door and see nothing but black darkness.
  You have a strange feeling about this.

  ? Close your eyes and enter the room.
    You are dead now. No one will ever know why.
  ? Light a torch.
    The room has no floor, but a deep pit wth spears in it.
    Thank god you didn't step inside.
    ? Go away.
      [flee] This was a small dungon and a borng adventure.
    ? Search for another door.
      There is one, hidden behind a book shelve.
      <dungeon> Step inside.
      ? Go away
        <flee>

As you can see, in-place choices can be nested and mixed with normal links.
The syntax is quite intuitive. Just make sure you get the indention right.

Lets now have a look at the last two lines of the last example. There is an
in-place choice with no description text and only a single link. It makes no
sense to present this to the player, so it is stepped over by the game engine.
The following two examples are equivalent (to the player)::

  Are you male or female?
  ? I was male last time I checked.
    <male>
  ? Female, thats for sure.
    <female>

  Are you male or female?
  <male> I was male last time I checked.
  <male> Female, thats for sure.

Usage
-----

The library is in a very early state. You can parse a plot-file into a
scene-graph and play the game in the command line with the following syntax::

  from choice import parse, play
  game = parse(open(sys.argv[1]))
  play(game)

Licence (MIT)
-------------

  Copyright (c) 2010, Marcel Hellkamp.

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to
  deal in the Software without restriction, including without limitation the
  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
  sell copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
  IN THE SOFTWARE.

