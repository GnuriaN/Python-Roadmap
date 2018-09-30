from graphviz import Digraph

u = Digraph('Roadmap Python', filename='RoadmapPython.gv')
u.attr('node', shape='doublebox')
u.node_attr.update(color='lightblue', style='filled')

u.body.append('size="12,12"')
u.body.append(r'label = "\n\nRoadmap Python\ndrawn by GnuriaN"')
u.body.append('fontsize=20')

# u.edge('Linux', 'nginx', label='1')
u.edge('JavaScript','Web')

u.edge('Linux', 'nginx')
u.edge('Linux', 'Базы данных')
u.edge('nginx', 'Web')

u.edge('Базовый курс Python', 'Базы данных')
u.edge('Базовый курс Python', 'Web')
u.edge('Базовый курс Python', 'Передача данных')

u.edge('Базы данных', 'SQLAlchemy')
u.edge('Базы данных', 'SQLite')
u.edge('Базы данных', 'PostgreSQL')
u.edge('Базы данных', 'MySQL')
u.edge('Базы данных', 'Redis')
u.edge('Базы данных', 'MongoDB')

u.edge('SQLAlchemy', 'SQLite')
u.edge('SQLAlchemy', 'PostgreSQL')
u.edge('SQLAlchemy', 'MySQL')

u.edge('Web', 'Django')
u.edge('Web', 'Flask')
u.edge('Web', 'Pyramid')
u.edge('Web', 'HTML')

u.edge('HTML', 'CSS')
u.edge('HTML', 'Django')
u.edge('HTML', 'Flask')
u.edge('HTML', 'Pyramid')

u.edge('Передача данных', 'WebRTC')
u.edge('Передача данных', 'websockets')
u.edge('Передача данных', 'Twisted')
u.edge('Передача данных', 'asyncio')

u.edge('Форматы данных', 'pickle')
u.edge('Форматы данных', 'JSON')
u.edge('Форматы данных', 'YAML')

u.view()
