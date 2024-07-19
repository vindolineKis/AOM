import sys
from labjack import ljm

# Open first found LabJack
handle = ljm.openS("ANY", "ANY", "ANY")  # Any device, Any connection, Any identifier

# Setup configuration based on device type
info = ljm.getHandleInfo(handle)
deviceType = info[0]

if deviceType == ljm.constants.dtT4:
    aNames = ["AIN0", "AIN1"]
    aValues = [0, 0]  # Dummy values as T4 doesn't need configuration
else:
    aNames = ["AIN0", "AIN1"]
    aValues = [10.0, 10.0]  # Range for T7 and T8

# Write configuration to the LabJack
numFrames = len(aNames)
ljm.eWriteNames(handle, numFrames, aNames, aValues)

# Read AIN0 and AIN1 from the LabJack with eReadNames in a loop.
numFrames = 2
loopAmount = sys.argv[1] if len(sys.argv) > 1 else "infinite"
i = 0

with open("result.txt", "w") as f:
    while True:
        try:
            results = ljm.eReadNames(handle, numFrames, aNames)
            print(f"AIN0: {results[0]} V, AIN1: {results[1]} V")
            f.write(f"AIN0 : {results[0]} V, AIN1 : {results[1]} V\n")
            i += 1
            if loopAmount != "infinite" and i >= int(loopAmount):
                break
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(e)
            break

# Close handles
ljm.close(handle)