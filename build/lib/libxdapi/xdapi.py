import requests

def getCDNPath(): # 获取图片CDN地址
    url = "https://api.nmb.best/api/getCDNPath"
    response = requests.get(url).json()
    return response

def getForumList(): # 获取板块列表
    url = "https://api.nmb.best/api/getForumList"
    response = requests.get(url).json()
    return response

def getTimelineList(): # 获取时间线列表
    url = "https://api.nmb.best/api/getTimelineList"
    response = requests.get(url).json()
    return response

def showf(fid,page,usercookie): # 查看版面，fid为版面ID，page为页数（可置空），usercookie为饼干（可置空）
    url = "https://api.nmb.best/api/showf?id=" + str(fid) + "&page=" + str(page)
    cookies = {
        "userhash": usercookie
    }
    response = requests.get(url, cookies=cookies).json()
    return response

def timeline(page,usercookie): # 查看时间线，page为页数（可置空），usercookie为饼干（可置空）
    url = "https://api.nmb.best/api/timeline?page=" + str(page)
    cookies = {
        "userhash": usercookie
    }
    response = requests.get(url, cookies=cookies).json()
    return response

def thread(id,page): # 查看串，id为串号，page为页数（可置空）
    url = "https://api.nmb.best/api/thread?id=" + str(id) + "&page=" + str(page)
    response = requests.get(url).json()
    return response

def po(id,page): # 只看po，id为串号，page为页数（可置空）
    url = "https://api.nmb.best/api/po?id=" + str(id) + "&page=" + str(page)
    response = requests.get(url).json()
    return response

def feed(uuid,page): # 查看订阅，uuid为订阅id，page为页数（可置空）
    url = "https://api.nmb.best/api/feed?uuid=" + str(uuid) + "&page=" + str(page)
    response = requests.get(url).json()
    return response

def addFeed(uuid,tid): # 添加订阅，uuid为订阅id，tid为串号
    url = "https://api.nmb.best/api/addFeed?uuid=" + str(uuid)
    payload = 'tid=' + str(tid)
    response = requests.post(url, data=payload).json()
    return response

def delFeed(uuid,tid): # 删除订阅，uuid为订阅id，tid为串号
    url = "https://api.nmb.best/api/delFeed?uuid=" + str(uuid)
    payload = 'tid=' + str(tid)
    response = requests.post(url, data=payload).json()
    return response

def ref(id): # 查看引用，id为串号
    url = "https://api.nmb.best/api/ref?id=" + str(id)
    response = requests.get(url).json()
    return response

def doPostThread(imageurl,fid,title,content,water,usercookie): # 发新串，fid为板块id，content为内容，usercookie为饼干，imageurl为文件路径（可置空），water为是否添加水印（可置空），title为标题（可置空），注意content和imageurl只能置空其中一项。
    url = "https://www.nmbxd1.com/Home/Forum/doPostThread.html"
    headers = {
        "Content-Type": "multipart/form-data"
    }
    cookies = {
        "userhash": usercookie
    }
    payload = {
        "fid": fid,
        "title": title,
        "content": content,
        "water": water
    }
    if imageurl == '':
        files = {}
    else:
        files = {
            'file': open(imageurl, 'rb')
        }
    response = requests.post(url, headers=headers, data=payload, files=files, cookies=cookies)
    return response

def doReplyThread(imageurl,id,title,content,water,usercookie): # 回复串，id为串号，content为内容，usercookie为饼干，imageurl为文件路径（可置空），water为是否添加水印（可置空），title为标题（可置空），注意content和imageurl只能置空其中一项。
    url = "https://www.nmbxd1.com/Home/Forum/doReplyThread.html"
    headers = {
        "Content-Type": "multipart/form-data"
    }
    cookies = {
        "userhash": usercookie
    }
    payload = {
        "resto": id,
        "title": title,
        "content": content,
        "water": water
    } 
    if imageurl == '':
        files = {}
    else:
        files = {
            'file': open(imageurl, 'rb')
        }
    response = requests.post(url, headers=headers, data=payload, files=files, cookies=cookies)
    return response