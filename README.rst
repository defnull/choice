Multiple-Choice Game Engine
===========================

This is a very simple text-based multiple-choice game which
parses an easy-to-read plot-file syntax. An embedded language to support more
complex game logic (variables, conditional text or choices, functions)
is planned, but not supported jet.

Plot-File Syntax
----------------

You can add any number of scenes to a plot-file. Each new scene is preceded by
a label (e.g. ``[scene_name]``) followed by a description text. The first
scene does not need to have a label. It is labeled 'start' automatically.

::

  You open the door and see nothing but black darkness.
  You have a strange feeling about this.

  [room] You are dead now. No one will ever know why.

  [exit] You got out alive, lucky one.

Scenes alone don't make a good story. You need a way to proceed from scene to
scene, best by giving the player a choice. This is why labels are so
important. You can link to them::

  You open the door and see nothing but black darkness.
  You have a strange feeling about this.
  <room> Close your eyes and enter the room.
  <torch> Light a torch.
  
  [room] You are dead now. No one will ever know why.
  
  [torch] In the flickering light of the torch you can see that the room has
  no floor, but a deep pit with spears in it. Thank god you didn't step
  inside.
  <exit> Go home.
  
  [exit] You got out alive, lucky one.


Now the player has a choice. As soon as he reaches a scene that has no further
choices, the game ends.

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
    In the flickering light of the torch you can see that the room has
    no floor, but a deep pit with spears in it. Thank god you didn't step
    inside.
  
    ? Adventures are dangerous? I don't want to do this anymore.
      [end] This was a small dungon and a borng adventure.
  
    ? Search for another door.
      There is one, hidden behind a book shelve.
  
      <dungeon> Step inside cautiously.
  
      ? Go away.
        <end>
  
  <end> Be a coward and go home.
  
  [dungen] The adventure begins...

As you can see, in-place choices can be nested and mixed with normal links.
The blank lines are optional.

This syntax is quite intuitive. Just make sure you get the indention right.
The last ``<end>`` link for example should match the indention of the scene it
belongs to. If a nested block gets to big to fit your screen, consider
outsourcing parts of it into separate root-level scenes.

Lets now have a look at the "Go away" choice in the last example. It is
followed by an in-place scene with no description text and only a single link.
It makes no sense to present an empty scene to the player, so it is stepped
over by the game engine. The "Go away" choice jumps right to the 'end' scene,
just like an ``<end>`` link would do. The following two examples are
equivalent (to the player)::

  Are you male or female?
  ? I was male last time I checked.
    <male>

  ? Female, thats for sure.
    <female>

::

  Are you male or female?
  <male> I was male last time I checked.
  <female> Female, thats for sure.

Usage
-----

The library is in a very early state. You can parse a plot-file into a
scene-graph and play the game in the command line with the following syntax::

  from choice import parse, play
  with open('./test.plot') as fp:
      source = fp.read()
      game = parse(source)
      play(game)

Alternatively you can just run ``choice.py`` with the plot-file as first command-line argument.

  $ python choice.py ./test.plot

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

