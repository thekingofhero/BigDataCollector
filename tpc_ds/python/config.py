def local_config():
    tpcds_tool_root = ""
    #SF 3000 means ~1TB
    tpcds_scale_factor = 300
    #flat file's path on hdfs
    flatfile_path_HDFS = "/user/root/tpcds-data-%s"%(tpcds_scale_factor)
    nodes = ['tracing024',\
             'tracing025',\
             'tracing026',\
             'tracing027']
    threads_per_node = 12
    db_name = 'tpcds_parquet_300'
    tpcds_tbls = {
        'date_dim':'',
        'time_dim':'',
        'customer':'',
        'customer_address':'',
        'customer_demographics':'',
        'household_demographics':'',
        'item':'',
        'promotion':'',
        'store':'',
        'store_sales':'',
        'inventory':''
    }
    return locals()
