import subprocess

def gridlabd_geodata_merge(location1, location2):
    cmd = f"gridlabd geodata merge -D distance location {location1} {location2}"
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    
    if process.returncode == 0:
        return output.decode().strip()
    else:
        return ""

# Example usage:
location1 = "37.4150,-122.2056"
location2 = "37.3880,-122.2884"
result = gridlabd_geodata_merge(location1, location2)
print(result)
