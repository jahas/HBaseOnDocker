import happybase as hbase

zk = "quickstart.cloudera"


def run():
    table = hbase.Connection(host=zk).table("adam:table")
    
    print(f'Count of column families is {len(table.families())}')
    print(f'Count of regions is {len(table.regions())}')
    scan = table.scan(columns=["a:the_column"])
    for row in scan:
        print(row)


if __name__ == "__main__":
    run()
