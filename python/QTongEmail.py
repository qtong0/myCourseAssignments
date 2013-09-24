import re

def parse_email(str_email):
    return_dict = {}
    regex = r'^(?P<user>[\ a-zA-Z0-9._\-\+]+)@(?P<domain>[a-zA-Z0-9.-]+)\.(?P<tld>[a-zA-Z/./ ]{2,})$'
    tmp = re.compile(regex)
    p = tmp.search(str_email)
    if p is not None:
        tld_tmp = p.group('tld')
        tld_list = re.split('\W+', tld_tmp)
        tld_tmp = tld_list[0]
        if tld_tmp.__len__() > 4:
            return return_dict
        
        user_tmp = p.group('user')
        user_list = re.split('\s+', user_tmp)
        user_tmp = user_list[-1]
        
        return_dict['tld'] = tld_tmp
        return_dict['user'] = user_tmp
        return_dict['domain'] = p.group('domain')

    return return_dict