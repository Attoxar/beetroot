import sys


print("Original sys.path:")
print(sys.path)

custom_directory = "/path/to/custom_directory"
sys.path.append(custom_directory)

print("\nUpdated sys.path:")
print(sys.path)

try:
    import custom_module
    print("\nCustom module imported successfully!")
except ImportError:
    print("\nFailed to import custom module.")
