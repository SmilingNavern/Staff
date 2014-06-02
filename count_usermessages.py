#!/usr/bin/env python
#
#

import requests
import re


def posts_sorted_count(posts_of_users):
    users_list = posts_of_users.keys()

    users_list = sorted(users_list, key=posts_of_users.__getitem__, reverse = True)

    for name in users_list:
        print "%s => %d" % (name, posts_of_users[name])

def find_user_posts(topic_id, start_page, last_page):

    pattern = re.compile(r'quote\(selection,\'(?P<user_name>.*)\'\)')

    user_posts = {}

    page_id = start_page

    for i in xrange(start_page, last_page + 1):

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

    return user_posts

def main():

    users_posts = find_user_posts("37314", 4, 11)
    posts_sorted_count(users_posts)
    
if __name__ == '__main__':
    main()