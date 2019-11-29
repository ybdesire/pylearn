from reloadr import autoreload

@autoreload
def fun(x):
    return x+66