import subprocess
import csv

def gridlabd_geodata_merge(location1, location2, output_file):
    cmd = f"gridlabd geodata merge -D distance location {location1} {location2}"
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()

    if process.returncode == 0:
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Location 1", "Location 2", "Result"])
            writer.writerow([location1, location2, output.decode().strip()])
        print(f"Results written to '{output_file}' successfully.")
    else:
        print("Error executing gridlabd geodata merge.")

# Example usage:
location1 = "37.4150,-122.2056"
location2 = "37.3880,-122.2884"
output_file = "results.csv"
gridlabd_geodata_merge(location1, location2, output_file)
