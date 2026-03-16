from S1_SDK import Arm_Search
import sys
if sys.platform.startswith('linux'):
    import glob
    ports = glob.glob('/dev/ttyUSB*')
    for port in ports:
        if(Arm_Search(port)):
            print(port,"(机械臂)")
        else:
            print(port,"(非机械臂)")
else:
    print("暂不支持")