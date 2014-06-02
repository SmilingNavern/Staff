#!/usr/bin/env python
#
#

import requests
import re


def posts_count(posts_of_users):
    users_list = posts_of_users.keys()

    users_list = sorted(users_list, key=posts_of_users.__getitem__, reverse = True)

    for name in users_list:
        print "%s => %d" % (name, posts_of_users[name])

def main(last_page):
    user_posts = {}

    #User values
    topic_id = "37314"
    page_id = 4

    pattern = re.compile(r'quote\(selection,\'(?P<user_name>.*)\'\)')


    for i in xrange(page_id,last_page+1):
        payload = {'topic' : topic_id, 'page' : page_id}
        page_content = requests.get("http://reps.ru/forum.php", params=payload)
        
        for line in page_content.text.splitlines():
            result = pattern.search(line )
            
            if result:
                if result.group("user_name") in user_posts.keys():
                    user_posts[result.group("user_name")] += 1
                else:
                    user_posts[result.group("user_name")] = 1

        page_id += 1

    
    posts_count(user_posts)
    
if __name__ == '__main__':
    main(10)