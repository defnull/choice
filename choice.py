''' This is a very simple text-based multiple-choice game which
parses an easy plot-file syntax. An embedded language to support more
complex game logic (variables, conditional text or choices, functions)
is planned.

'''

import re, sys, textwrap

t_NAME   = re.compile(r'\[([^\]]+)\]\s*(.*)')
t_JUMP   = re.compile(r'<([^>]+)>(.*)')
t_CHOICE = re.compile(r'\?\s*(.+)')

def getind(line):
    sline = line.lstrip()
    ind = line[:-len(sline)]
    ind = ind.count('\t')*4 + ind.count(' ')
    return ind, sline

def lexer(lines):
    ind = 0
    out = []
    for line in lines:
        if not line.strip():
            if out and out[-1][0] == 'text':
                out.append(['text', ind, ''])
            continue
        ind, line = getind(line)
        m = t_NAME.match(line)
        if m:
            name, text = m.groups()
            out.append(['name', ind, name])
            if text:
                out.append(['text', ind, text])
            continue
        m = t_JUMP.match(line)
        if m:
            target, text  = m.groups()
            out.append(['jump', ind, target, text.strip() or 'Continue'])
            continue
        m = t_CHOICE.match(line)
        if m:
            question  = m.groups()[0]
            out.append(['choice', ind, question.strip()])
            continue
        out.append(['text', ind, line.strip()])
    return out

class Scene(object):
    def __init__(self, name=''):
        self.name = name
        self.text = ''
        self.choices = []
        self.parent = None

    def add_choice(self, target, description):
        self.choices.append([target, description])
        if not target.parent:
            target.parent = self

    def export(self, noloop=None):
        if not noloop:
            noloop = []
        if self.name:
            yield '[%s]' % self.name
        if self in noloop:
            yield '--recursion--'
            return
        noloop.append(self)
        for line in self.text.splitlines():
            yield '%s' % line
        for target, text in self.choices:
            yield '? %s:' % text
            for line in target.parse(noloop):
                yield '  ' + line

    def get_all(self, pool=None):
        if not pool: pool = set()
        pool.add(self)
        for target, desc in self.choice:
            if target not in pool:
                 target.get_all(pool)
        return pool

    def __str__(self):
        return '\n'.join(self.export()) + '\n'

    def __repr__(self):
        return '<' + self.name + '>'

def parser(tokens):
    start = Scene()
    named = {}
    start.parent = start
    stack = [[start, 0]]
    for token in tokens:
        token, ind, data = token[0], token[1], token[2:]
        if stack[-1][1] == -1: # We expect indention
            if ind > stack[-2][1]: # Intendion is good
                stack[-1][1] = ind
            else: # Dedention where indention is expected
                raise ValueError('Expected indention.')
        while ind < stack[-1][1]: # Dedention
            stack.pop()
        scene = stack[-1][0]
        if token == 'name':
            if scene.name or scene.choices:
                stack.pop()
                scene = named.setdefault(data[0], Scene(data[0]))
                stack.append([scene, ind])
            else:
                scene.name = data[0]
                named[data[0]] = scene
        elif token == 'text' and not scene.choices:
            scene.text += data[0] + '\n'
        elif token == 'jump':
            target = named.setdefault(data[0], Scene(data[0]))
            scene.add_choice(target, data[1])
        elif token == 'choice':
            nscene = Scene()
            stack.append([nscene, -1])
            scene.add_choice(nscene, data[0])
    return start

def play(scene):
    ''' Play a game in the text console '''
    while 1:
        if not scene.text and len(scene.choices) == 1:
            scene = scene.choices[0][0]
            continue
        print '\n'*20
        print '-'*78
        print '\n'.join(textwrap.wrap(scene.text.rstrip(), 78))
        print
        if not scene.choices: break
        for i, choice in enumerate(scene.choices):
            print "%d) %s" % (i+1, choice[1])
        choice = int(raw_input('? ') or 1)-1
        scene = scene.choices[choice][0]

play(parser(lexer(open(sys.argv[1]))))
