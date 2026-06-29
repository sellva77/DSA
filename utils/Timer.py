import time

def timer_dec(baseFun):
    def enhanced_func(*args, **kwargs):
        start= time.time()
        result=baseFun(*args, **kwargs)
        end=time.time()
        print(f"Task time: {end-start} seconds")
        return result
    return enhanced_func