from my_devices import net_things
import my_functions


if __name__ == '__main__':
    for i in net_things:
        conn = my_functions.connection(i)
        if 'arista' in i['hostname']:
            conn.load_merge_candidate(filename='arista1.lasthop.io-loopbacks')
        elif 'cisco' in i['hostname']:
            conn.load_merge_candidate(filename='cisco3.lasthop.io-loopbacks')
        else:
            print('No hostname provided')
        print(conn.compare_config())
        result = input('Continue?')
        if result == 'y':
            conn.commit_config()
            print(conn.compare_config())
            input('Press any key...')
        else:
            conn.discard_config()
        


