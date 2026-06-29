import time

def timer_dec(baseFun):
    def enhanced_func(*args, **kwargs):
        start= time.time()
        result=baseFun(*args, **kwargs)
        end=time.time()
        elapsed = (end - start) * 1000
        print(f"Task time: {elapsed} seconds")
        return result
    return enhanced_func