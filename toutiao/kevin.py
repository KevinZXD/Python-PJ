# -*- encoding:utf-8  -*-


def get_high_video_url(r):
    try:
        main_url=r['data']['video_list']['video_3']['main_url']

    except KeyError ,e:
        try:
            main_url = r['data']['video_list']['video_2']['main_url']
            print(e.args[0])
        except KeyError ,e:
            try:
                main_url = r['data']['video_list']['video_1']['main_url']
            except KeyError,e:
                print(e.args[0])

    return main_url