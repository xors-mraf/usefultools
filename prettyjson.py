import json
def json_pretty_string(string):
    j=json.loads(string)
    print(json.dumps(j,indent=4))
def json_pretty_file(file_path):
  with open(file_path,'r')as file:
    j=json.load(file)
    print(json.dumps(j,indent=4))

if __name__ == '__main__':
    js=''
    print('hello please enter type of entering json (file or string):',end="")
    s=str(input())
    if(s=='file'):
        print('please enter json file path:',end='')
        js=str(input())
        json_pretty_file(js)
    elif(s=='string'):
        print('hello please enter string:')
        lines = []
        while True:
            line = input()
            if line:
                lines.append(line)
            else:
                break
        js= '\n'.join(lines)
        json_pretty_string(js)
