import os

backup_path = '/home/sylwia/backup4'

folders_paths = {
    'flaga': '/var/www',
    '.ssh': '/home/sylwia'
}

files_paths = { 
    'flaga.service': '/etc/systemd/system',
    'programowanie-python.online': '/etc/nginx/sites-available',
    'backup_scrypt.py': '/home/sylwia'
}

os.system('mkdir {}'.format(backup_path))

for name, path in folders_paths.items():
    folder_source = path + '/' + name
    dest = backup_path
    os.system('cp -r {} {}'.format(folder_source, dest))
    print(folder_source)
    print(dest)
    print()

for name, path in files_paths.items():
    file_source = path + '/' + name
    dest = backup_path
    os.system('cp {} {}'.format(file_source, dest))
    print(file_source)
    print(dest)
