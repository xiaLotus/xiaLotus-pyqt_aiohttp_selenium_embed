import sys
# 更換
package_path = r".\python-3.11.3\Lib\site-packages"
if package_path not in sys.path:
    sys.path.append(package_path)
import os

current_path = os.path.dirname(os.path.abspath(__file__))
if current_path not in sys.path:
    sys.path.append(current_path)

from func import Class1, Class2, Class3

obj1 = Class1()
obj2 = Class2()
obj3 = Class3()

print(obj1, '\n', obj2, '\n', obj3, '\n')