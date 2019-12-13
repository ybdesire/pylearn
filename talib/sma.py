import numpy
import talib



# Simple Moving Average
# default 30 day sma
close = numpy.random.random(30)
output = talib.SMA(close)
print(close)
print(output)

'''
[ 0.06089536  0.97342085  0.36221949  0.79925895  0.51810701  0.79420899
  0.43860557  0.53023293  0.50458963  0.19422644  0.69454565  0.14783919
  0.65423097  0.82766262  0.07208659  0.62104965  0.23842752  0.85081636
  0.91023414  0.36004765  0.45649184  0.30652258  0.76235688  0.67097743
  0.80317168  0.77994786  0.23355331  0.45142714  0.88243131  0.85009511]
[        nan         nan         nan         nan         nan         nan
         nan         nan         nan         nan         nan         nan
         nan         nan         nan         nan         nan         nan
         nan         nan         nan         nan         nan         nan
         nan         nan         nan         nan         nan  0.55832269]

'''




# Simple Moving Average
close = numpy.random.random(10)
output = talib.SMA(close, timeperiod=5)# 5 day sma
print(close)
print(output)

'''
[ 0.62841305  0.84872348  0.07729728  0.06175836  0.52374135  0.70158612   0.74331391  0.71948381  0.09842918  0.3126808 ]

[        nan         nan         nan         nan  0.42798671  0.44262132   0.4215394   0.54997671  0.55731087  0.51509876]
'''




