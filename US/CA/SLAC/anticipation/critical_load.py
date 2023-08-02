import gridlabd
gridlabd.command('123.glm')

def extract_meters(output_file_path):
    critical_meters = gridlabd.get_class('meter')
    critical_meters.to_csv='output_file_path.csv'
   

if __name__ == "__main__":
    output_file_path = "critical_meters.glm"
    extract_meters(output_file_path)
