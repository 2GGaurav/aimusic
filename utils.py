ALLOWED_EXTENSIONS=['mid']
UPLOADS_FOLDER='uploads/'

def file_valid(file):
    return '.' in file and \
      file.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS