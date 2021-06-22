def solution(new_id):
    new_id = new_id.lower()
    new_id = new_id.replace('~','').replace('!','').replace('@','').replace('#','').replace('$','').replace('%','').replace('^','').replace('&','').replace('*','').replace('(','').replace(')','').replace('=','').replace('+','').replace('[','').replace(']','').replace('{','').replace('}','').replace(':','').replace('?','').replace(',','').replace('<','').replace('>','').replace('/','')
    while '..' in new_id:
        new_id = new_id.replace('..','.')
    if new_id[0]=='.':
        new_id = new_id[1:]
    if len(new_id)!=0:
        if new_id[-1]=='.':
            new_id = new_id[:-1]
    if new_id=='':
        new_id += 'a'
    if len(new_id)>15:
        new_id = new_id[:15]
    if new_id[-1]=='.':
        new_id = new_id[:14]
    while len(new_id)<3:
        new_id += new_id[-1]
    return new_id