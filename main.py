import sys
from errors import * 

projectName, projectType = sys.argv[1], sys.argv[2]

if len(sys.argv) < 4:
    raise InsufficientArguments('Insufficient Arguments Provided, (scaffold <path> <projectType>)')

print(projectName, projectType)
