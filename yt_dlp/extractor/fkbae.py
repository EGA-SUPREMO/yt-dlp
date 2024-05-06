from .common import InfoExtractor

import re


class FKBAEIE(InfoExtractor):
    _VALID_URL = r'https://fkbae\.to/(?P<id>\d+)/?'
    _TESTS = [{
        'url': 'https://fkbae.to/9778/',
        'md5': '490496174de8ab8dbf69317ca8d79418',
        'info_dict': {
            'id': '9778',
            'ext': 'mp4',
            'title': 'Nude snapchat girl put her panties to the side and rubbed her 18+ teen pussy',
            'age_limit': 18
        },
    }, {
        'url': 'https://fkbae.to/223',
        'only_matching': True,
    }]

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)

        formats = []
        format_url = self._html_search_regex(r'"embedURL":"([^"]+)"', webpage, 'video URL')
        format_url = re.sub(r'\\', '', format_url)

        webpage_video = self._download_webpage(format_url, video_id)

        match = re.search(r'(https:\/\/[^"]+\.mp4)', webpage_video)
        format_url = match.group(1)
        formats.append({
            'url': format_url,
            'format_id': 'default',
        })

        title = self._html_search_regex(r'<span class="fl-heading-text">(.+?)</span>', webpage, 'title')

        http_headers = {'Referer': 'https://fkbae.to/'}

        return {
            'id': video_id,
            'title': title,
            'formats': formats,
            'age_limit': 18,
            'http_headers': http_headers
        }
 
