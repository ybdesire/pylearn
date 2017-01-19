import os
import sys


androguard_module_path = os.path.join( os.path.dirname(os.path.abspath(__file__)), 'common/Androguard-2.0/androguard' )

if not androguard_module_path in sys.path:
    sys.path.append(androguard_module_path)


from androguard.core.bytecodes import apk
from androguard.core.bytecodes import dvm
from androguard.core.analysis import analysis
from sklearn.feature_extraction import FeatureHasher

__author__ = 'Bin Yin (ybdesire@gmail.com)'
__date__ = '2017-01-19'
__version_info__ = (0, 0, 0)
__version__ = '.'.join(str(i) for i in __version_info__)


print('run at python2.7')


apk_file = 'test.apk'
a = apk.APK(apk_file)
d = dvm.DalvikVMFormat(a.get_dex())
x = analysis.VMAnalysis(d)

strs = x.tainted_variables.get_strings()

for s in strs:
    # s[0] is path info, s[1] is string. such as (<androguard.core.analysis.analysis.TaintedVariable object at 0xd655b50>, 'bitmap decoded size=')
    for path in s[0].get_paths(): # get path info by s[0]
        cm_method = d.get_cm_method(path[1]) # get method by path[1]
        cm_method_name = cm_method[0] # get method name by cm_method[0]
        print('method_name: {0},    string: {1}'.format(cm_method_name, s[1]))


'''
result example:

(1) one strings at one class (mult-methods)
method_name: Landroid/support/v4/app/ShareCompat$IntentBuilder;,    string: android.intent.extra.CC
method_name: Landroid/support/v4/app/ShareCompat$IntentBuilder;,    string: android.intent.extra.CC
method_name: Landroid/support/v4/app/ShareCompat$IntentReader;,    string: android.intent.extra.CC
method_name: Landroid/support/v4/app/ShareCompat$IntentBuilder;,    string: android.intent.extra.CC

(2) multi-strings at one methods
method_name: Lcom/alipay/sdk/util/g;,    string: NETWORK_TYPE_13
method_name: Lcom/alipay/sdk/util/g;,    string: NETWORK_TYPE_15


'''
