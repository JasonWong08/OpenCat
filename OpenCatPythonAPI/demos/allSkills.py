#!/usr/bin/python3
# -*- coding: utf-8 -*-

# PetoiRobot is a wrapper for ardSerial.
# Test all skills of Bittle.
# 依赖：在 OpenCatPythonAPI 目录执行 pip install -r requirements.txt（见上级目录）。
from PetoiRobot import *

model = 'Bittle'
postureTable = postureDict[model]

skillList = ['kbalance','kbuttUp','kcalib','kdropped','klifted','klnd','krest','ksit','kstr','kup','kzero','kang','kbx','kchr','kck','kcmh','kdg','kfiv','kgdb','khds','khg','khi','khsk','khu','kjmp','kkc','kmw','knd','kpd','kpee','kpu','kpu1','krc','kscrh','ksnf','ktbl','kts','kwh','kzz']
if __name__ == '__main__':
    try:
        '''
        testSchedule is used to test various serial port commands
        '''
        testSchedule = [
                        
            # turn off the gyroscope
            ['g',0.1],
            
            # turn on/off the random behavior, retun 'Z' to turn on, 'z' to turn off
            # ['z',0.1],

        ]
        # goodPorts = {}
        # connectPort(goodPorts)
        autoConnect()
        t=threading.Thread(target = keepCheckingPort, args = (goodPorts,))
        t.start()
        print(skillFullName)
        parallel = False
#        if len(goodPorts)>0:
#        time.sleep(2);
        send(goodPorts, ['G',0.1])
        for task in skillList:  # execute the tasks in the testSchedule
            print(f'{skillFullName[task[1:]]:>15}',end=': ')
            print(task)
            send(goodPorts, [task,0.1])
        
        # closeAllSerial(goodPorts)
        closePort()
        logger.info("finish!")
        os._exit(0)

    except Exception as e:
        logger.info("Exception")
        # closeAllSerial(goodPorts)
        closePort()
        os._exit(0)
        print(e)
        raise e
