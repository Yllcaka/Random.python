import getopt, sys

def Thingy_thats_important_for_this_programm():
    start_date = None
    end_date = None

    argv = sys.argv[1:]


    try:
        opts,args = getopt.getopt(argv,"s:e:",["start_date=","end_date="])

    except getopt.GetoptError as err:
        print(err)
        opts = []
    for opt,arg in opts:
        if opt in ["-s","--start_date"]:
            start_date = arg
        elif opt in ["-e","--end_date"]:
            end_date = arg
    print(f"start date = {start_date}")
    print(f"end date = {end_date}")
Thingy_thats_important_for_this_programm()