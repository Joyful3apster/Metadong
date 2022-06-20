import ppdeep

h2 = 'The equivalence of mass and energy translates into the well-known E = mc²'
h1 = 'The equivalence of mass and energy translates into the well-known E = MC2'


print(ppdeep.compare(ppdeep.hash(h2), ppdeep.hash(h1)))