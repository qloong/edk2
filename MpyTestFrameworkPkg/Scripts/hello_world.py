import mptf

def run(log_path):
    print ("Hello world!")
    obj = mptf.mptf(log_path)
    obj.Input('cls' + mptf.ENTER)
    obj.Close()