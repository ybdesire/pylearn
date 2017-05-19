ids_list_all = [ 'id01','id02','id03','id04','id05','id06','id07','id08', 'id11','id12','id13','id14','id15','id16','id17','id18', 'id21','id22','id23','id24','id25','id26','id27','id28', 'id31','id32','id33']


# cut long list into sub-list, since es terms search list len cannot large than 8
ids_chunks = [ids_list_all[x:x+8] for x in range(0, len(ids_list_all), 8)]

print(ids_chunks)