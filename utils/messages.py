def detail_message(string, id):
    return f'El {string} con el id {id} no esta disponible.'


def delete_message(string):
    return f'El {string} se eliminó correctamente.'


def file_error_updated(string):
    return f'No fue posible actualizar el archivo {string}.'


def file_error_deleted(string):
    return f'No fue posible eliminar el archivo {string}.'


def db_error():
    return 'Ocurrió un problema, verifique los datos.'
