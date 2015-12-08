import os
def local_config():
    step_size = 50
    consumer_num = 1
    #output_type:
    #        db: postgres' database
    #        csv:csv file
    output_type = 'csv'
    install_path = os.path.dirname(os.path.realpath(__file__))
    return locals()
