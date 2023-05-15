import os
import shutil 



extensions = {
    'video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg', 'mpeg', 'm4v', 'h264', 'flv','rm', 'swf', 'vob'],    
    'audio': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa', 'wma', 'wpl', 'cda'],
    'images': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif', 'tiff'],
    'archives': ['zip', 'rar', '7z', 'z', 'gz', 'rpm', 'arj', 'pkg', 'deb'],
    'documents': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt'] ,
    'other':[]}




def normalize(text):  #нормализайия имени файла 
    trans_map = {ord('а'):'a',ord('б'):'b',ord('в'):'v',ord('г'):'h',ord('д'):'d',ord('е'):'e',ord('є'):'ye',ord('ж'):'zh',ord('з'):'z',\
    ord('и'):'y',ord('і'):'i',ord('ї'):'yi',ord('й'):'y', ord('к'):'k',ord('л'):'l',ord('м'):'m',ord('н'):'n',ord('о'):'o',ord('п'):'p',\
    ord('р'):'r',ord('с'):'s',ord('т'):'t',ord('у'):'u',ord('ф'):'f',ord('х'):'kh',ord('ц'):'ts',ord('ч'):'ch',ord('ш'):'sh',ord('щ'):'shch',\
    ord('ь'):"'",ord('ю'):'yu',ord('я'):'ya',ord(' '):'_'}
    norm_name=text.lower().translate(trans_map)
    return norm_name

def list_of_file(path):  #список файлов в папке 
    file_list = os.listdir(path)
    return file_list

def create_new_folder(path): #создание новых папок для сортировки
    for ext in extensions:
        if not os.path.exists(os.path.join(path, ext)):
            os.mkdir(os.path.join(path, ext))

def sort_files(folder_path):
    global path
    file_paths = list_of_file(folder_path)
    ext_list = list(extensions.items())

    for file in file_paths: 
        if os.path.isdir(os.path.join(folder_path, file)):  #проверка на папку 
            if file not in extensions.keys():               #отсекаем папки для сортировки
                sort_files(os.path.join(folder_path, file))


        if os.path.isfile(os.path.join(folder_path, file)):   #проверка на файл 
            extent = file.split('.')[-1]
            norm_name = normalize(file.split('.')[0])
            if extent in extensions['archives']:  #проверка на архив
                fr = os.path.join(folder_path, file)
                to = f'{path}\{ext_list[3][0]}\{norm_name}'
                shutil.unpack_archive(fr, to , extent)
                os.remove(fr)
                continue
                
            for ext in range(len(list(ext_list))):
                if extent in ext_list[ext][1]:                      
                    to = f'{path}\{ext_list[ext][0]}\{norm_name}.{extent}'
                    fr = f'{folder_path}\{file}'
                    shutil.move(fr, to)
                    break
            
def del_empty_dir(path): # удаляем пустые папки
    for d in os.listdir(path):
        a = os.path.join(path, d)
        if os.path.isdir(a):
            del_empty_dir(a)
            if not os.listdir(a):
                os.rmdir(a)



if __name__ == "__main__":
    path = input ('Enter folder: ')
    create_new_folder(path)
    sort_files(path)
    del_empty_dir(path)

