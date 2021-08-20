import psutil
import platform
import inspect
import cpuinfo
print (f"Processor brand  : {cpuinfo.get_cpu_info()['brand_raw']}")
source_code = inspect.getsource(platform)
uname = platform.uname()
print (f"processor: {uname.processor}")
#print (source_code)
#print (f"what : {platform.uname()}")
print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))