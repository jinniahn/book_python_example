class Song(object):
    "음악의 메타 정보"
    
    def __init__(self):
        self.dbid = ''
        self.uid = ''
        self.title = ''
        self.artist = ''
        self.url = ''
        self.img_url = ''
        self.description = ''
        self.duration = 0
        self.created_at = None
        self.played_count = 0

    def __str__(self):
        s = []
        s.append('Song: ')
        if(self.dbid):
            s.append('  - id: {}'.format(self.dbid))
        if(self.uid):
            s.append('  - uid: ' + self.uid)        
        if(self.title):
            s.append('  - title: ' + self.title)
        if(self.artist):
            s.append('  - artist: ' + self.artist)
        if(self.url):
            s.append('  - url: ' + self.url)
        if(self.img_url):
            s.append('  - img: ' + self.img_url)
        s.append('  - played count: {}'.format(self.played_count))

        return '\n'.join(s)

    def to_dict(self):
        ret = {}
        ret["dbid"] = self.dbid
        ret["uid"] = self.uid
        ret["title"] = self.title
        ret["artist"] = self.artist
        ret["url"] = self.url
        ret["img_url"] = self.img_url
        ret["description"] = self.description
        ret["duration"] = self.duration
        ret["created_at"] = self.created_at
        ret["played_count"] = self.played_count

        return ret
