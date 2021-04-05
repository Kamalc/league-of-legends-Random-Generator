from google_images_search import GoogleImagesSearch
from Ignore_Area.myAPI_Key import get_my_key  # Delete this import  (I use it to get my api key)

def Search_Save(Champ,save_path):
    cx = '93e5e6f08c6709af0'  # this my search engine cc if u wanna use or create one by yourself ^_^
    api_key = get_my_key()    # use your own API here this private stuff dude ^_^
    gis = GoogleImagesSearch(api_key, cx)
    _search_params = {
        'q': Champ,
        'num': 1,
        'safe': 'high',
        'fileType': 'jpg',
        'imgType': 'photo',
        'imgSize': 'XXLARGE',
    }

    gis.search(search_params=_search_params, path_to_dir=save_path,
               custom_image_name=Champ)