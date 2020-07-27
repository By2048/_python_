import sys
import platform

print(1, sys.platform)
print(2, platform.system())
print()

print(3, 'example'.ljust(50, '_'))
print(4, 'example'.rjust(50, '_'))
