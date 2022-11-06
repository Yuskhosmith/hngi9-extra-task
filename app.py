import csv, json, os, hashlib

filepath = input("Paste the file path/name (filename.csv) here: \n")
# filepath = 'NFT Naming csv - Team Bevel.csv'

data = {}
jsonHash = []
with open(filepath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    BASE_DIR = os.getcwd()
    try:
        path = os.path.join(BASE_DIR, 'output')
        os.mkdir(path)
    except FileExistsError:
        pass

    for row in csvReader:
        data["format"] = "CHIP-007"
        data["seriesNumber"] = row["Series Number"]
        name = data["filename"] = row["Filename"]
        data["description"] = row["Description"]
        data["gender"] = row["Gender"]
        data["UUID"] = row["UUID"]
        
        jsonfilepath = os.path.join(path, data["filename"]+'.json')
        with open(jsonfilepath, 'w') as jsonFile:
            jsonFile.write(json.dumps(data, indent=4))
    
        k = hashlib.sha256(open(jsonfilepath, 'rb').read()).hexdigest()
        data['hash'] = k
        jsonHash.append(data.copy())
        data = {}
        print(f"{name} completed")
csvFile.close()
# print(data)

with open(filepath, 'w') as newCsvFile:
    headers = ['Series Number','Filename','Name','Description','Gender','UUID','Hash']
    writer = csv.DictWriter(newCsvFile, fieldnames=headers)
    writer.writeheader()
    # Series Number
    for oneJsonHash in jsonHash:
        writer.writerow({'Series Number': oneJsonHash['seriesNumber'], 'Filename': oneJsonHash['filename'], 'Description': oneJsonHash['description'],'Gender': oneJsonHash['gender'], 'UUID': oneJsonHash['UUID'], 'Hash': oneJsonHash['hash']})

newCsvFile.close()
