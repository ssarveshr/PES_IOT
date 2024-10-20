import glob
# Find all .proto files in the current directory
proto_files = glob.glob('*.proto')
import subprocess, os
my_env = os.environ.copy()
my_env["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
# Compile each .proto file
for proto_file in proto_files:
    # Execute the protoc compiler command
    subprocess.run(['protoc','--python_out=.', proto_file], env=my_env)