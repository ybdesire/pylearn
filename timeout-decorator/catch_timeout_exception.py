import timeout_decorator,time

@timeout_decorator.timeout(2,use_signals=True)# 2s time out
def test():
    try:
        time.sleep(3)# sleep 3s
        return 1
    except Exception as e:
        if isinstance(e, timeout_decorator.timeout_decorator.TimeoutError):
            return 2
        else:
            return 3
    
test()#2
