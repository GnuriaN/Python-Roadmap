from graphviz import Digraph

u = Digraph('Roadmap Python', filename='RoadmapPython.gv')
u.body.append('size="12,12"')
u.attr('node', shape='box')
u.node_attr.update(color='lightblue', style='filled')

u.edge('Linux', 'nginx')
u.edge('Linux', 'Базы данных')

u.edge('nginx', 'Web')

u.edge('Базовый курс Python', 'Базы данных')
u.edge('Базовый курс Python', 'Web')
u.edge('Базовый курс Python', 'Передача данных')

u.edge('Базы данных', 'SQLAlchemy')
u.edge('Базы данных', 'SQLite')
u.edge('Базы данных', 'PostgreSQL')
u.edge('Базы данных', 'Redis')
u.edge('Базы данных', 'MongoDB')

u.edge('SQLAlchemy', 'SQLite')
u.edge('SQLAlchemy', 'PostgreSQL')

u.edge('Web', 'Django')
u.edge('Web', 'Flask')
u.edge('Web', 'Pyramid')

u.edge('Передача данных', 'WebRTC')
u.edge('Передача данных', 'websockets')
u.edge('Передача данных', 'Twisted')
u.edge('Передача данных', 'asyncio')

u.edge('Форматы данных', 'pickle')
u.edge('Форматы данных', 'JSON')
u.edge('Форматы данных', 'YAML')

u.view()
