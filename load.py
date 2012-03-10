import sqlite3

# for dash expander
conn = sqlite3.connect('~/Library/Application Support/DashExpander/library.dash')

c = conn.cursor()

c.execute('INSERT INTO "snippets" VALUES(NULL, "shruggalt", "¯\_(シ)_/¯", NULL, NULL);')
