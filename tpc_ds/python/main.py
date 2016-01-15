import os
from config import local_config
from multiprocessing import Process

def hdfs_mdir():
    cmd = "hdfs dfs -mkdir -p %s"
    root_dir = local_config()['flatfile_path_HDFS']
    dirs = list(map(lambda x :os.path.join(root_dir,x) ,local_config()['tpcds_tbls'].keys()))
    for hdfs_dir in dirs:
        print("Making directory:%s"%(hdfs_dir))
        os.system(cmd%(hdfs_dir))

def gen_dims():
    dirs = list(map(lambda x :os.path.join(root_dir,x) ,local_config()['tpcds_tbls'].keys()))
    proc_list = []
    for tbl in local_config()['tpcds_tbls'].keys():
        cmd = "
                 %s \
                -TABLE %s \
                -SCALE %s \
                -DISTRIBUTIONS %s \
                -TERMINATE N \
                -FILTER Y \
                -QUIET Y |hdfs dfs -put - %s.dat 
            "%(os.path.join(local_config()['tpcds_tool_root'],'tools','dsdgen'),
                tbl,
                local_config()['tpcds_scale_factor'],
                os.path.join(local_config()['tpcds_tool_root'],'tools','tpcds.idx'))
        proc = Process(target=os.system,args=[cmd])
        proc_list.append(proc)
        proc.start()
    for proc in proc_list:
        if proc.is_alive():
            proc.join()

def gen_facts():
    print()

def main():

if __name__ == '__main__':
    
