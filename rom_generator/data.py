from datalog import easy

db = easy.read('''
 edge(a, b).
 edge(b, c).
 edge(c, d).
 edge(d, e).
 ''')

print(easy.select(db, ('edge', 'a', 'b')))

# db = easy.read('''
# entityType(my_scene_1, scene).
# hasConnectionPoint(my_scene_1, conn_1_1).
# connectionEntrance(conn_1_1, (15, 27)).
# connectionLocalExit(conn_1_1, (15, 26)).
# connectionLocalExitDirection(conn_1_1, direction_up).
#     ''')



breakpoint()
