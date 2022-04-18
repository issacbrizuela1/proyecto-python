"""
archivo de configuacion para conexcion con la base de datos
"""
class conf:        
    DB='proyecto'#nombre de la BD
    USUARIO='root'#usuario de la BD
    COLECCION=''#nombre de la coleccion(tabla)
    PASSWORD='ZXCVzxcv1234'#password del usuario en la bd
    URL='mongodb+srv://'+USUARIO+':'+PASSWORD+'@sandbox1.1jic6.mongodb.net/'+DB+'?authSource=admin&replicaSet=atlas-lz7100-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true'
    U_USUARIO=''#variable con el correo para un login
    U_PASSWORD=''#contraseña del usuario
    TOKEN=''#lo que respondera la api