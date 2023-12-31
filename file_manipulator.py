import sys

METHODS = ["reverse", "copy", "duplicate-contents", "replace-string"]
NUM_ARGS = {
    "reverse": 4,
    "copy": 4,
    "duplicate-contents": 4,
    "replace-string": 5
}

def is_method_valid(list):
    #check method name
    if len(list) < 2 or list[1] not in METHODS:
        return False
    return True

def reverse_string(string):
    newString = ""
    for i in range(len(string)):
        newString += string[- i - 1]
    return newString

def validate_argument_number(list):
    method = list[1]
    if not len(list) == NUM_ARGS.get(method, 0):
        raise ValueError(f"Invalid number of arguments for method '{method}'.")

def is_txt_file(text):
    if ".txt" not in text: return False
    return True

def is_natural_num(numString):
    n = int(numString)
    if n > 0: return True
    return False

def reverse(list):
    #[thisFileName, duplicate-contents, fileInput, fileOutPut]
    #validation
    validate_argument_number(list)
    fileInput = list[2]
    fileOutput = list[3]

    if not is_txt_file(fileInput) and not is_txt_file(fileOutput):
        raise ValueError("Chose text file for second and third arguments.")
    
    #reverse
    contents = ""
    with open(fileInput, 'r') as f:
        contents = f.read()
        contents = reverse_string(contents)
    with open(fileOutput, 'w') as f:
        f.write(contents)

    print(f"Contents of '{fileInput}' were reversed and saved in '{fileOutput}'.")

def copy(list):
    #[thisFileName, duplicate-contents, fileInput, fileOutPut]
    #validation
    validate_argument_number(list)
    fileInput = list[2]
    fileOutput = list[3]

    if not is_txt_file(fileInput) and not is_txt_file(fileOutput):
        raise ValueError("Chose text file for second and third arguments.")
    
    #copy
    contents = ""
    with open(fileInput, 'r') as f:
        contents = f.read()
    with open(fileOutput, 'x') as f:
        f.write(contents)
    
    print(f"'{fileInput}' is copied to '{fileOutput}'.")

def duplicate_contents(list):
    #[thisFileName, duplicate-contents, fileInput, duplicateTimes]
    #validation
    validate_argument_number(list)
    
    fileInput = list[2]
    if not is_txt_file(fileInput):
        raise ValueError("Chose text file for second argumnet.")

    duplicateTimes = 0
    if is_natural_num(list[3]):
        duplicateTimes = int(list[3])
    else:
        raise ValueError("Natural number is only accepted for duplicatetimes.")

    #duplicate
    newContents = ""
    with open(fileInput, 'r') as f:
        contents = f.read()
        newContents = contents
        for i in range(duplicateTimes):
            newContents += "\n" + contents
    with open(fileInput, 'w') as f:
        f.write(newContents)
    print("The file contents were duplicated.")

def replace_string(list):
    #[thisFileName, replace-string, fileInput, serchString, newString]
    validate_argument_number(list)

    fileInput = list[2]
    if not is_txt_file(fileInput):
        raise ValueError("Chose text file for second argumnet.")
    
    searchString = list[3]
    newString = list[4]

    contents = ""
    newContents = ""
    with open(fileInput, 'r') as f:
        contents = f.read()
    newContents = contents.replace(searchString, newString)
    with open(fileInput, 'w') as f:
        f.write(newContents)
    print(f"'{searchString}' are replaced by '{newString}'.")



argvList = sys.argv #[thisFileName, method, inputFilePath, outputFilePath]

if is_method_valid(argvList) is False:
    raise ValueError("Invalid method typed.")

method = argvList[1]

if method == "reverse":
    reverse(argvList)
elif method == "copy":
    copy(argvList)
elif method == "duplicate-contents":
    duplicate_contents(argvList)
elif method == "replace-string":
    replace_string(argvList)
