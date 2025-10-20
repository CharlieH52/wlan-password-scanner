# WLAN SCANNER
Utilizo esta herramienta para llevar un registro de las contraseñas de todos los AP que están bajo mi administración, por lo que más que abusar de las posibilidades, te recomiendo que la utilices como debe de ser, como una herramienta...

> [!CAUTION]
> Únicamente será útil mientras que la interfaz **WMIC** siga en tu versión de **Windows**, que a partir de la versión ***24H2 de Windows 11*** estará siendo *deshabilitada* de todas las instalaciones de **Windows**, por lo que esta *"brecha"* para obtener las contraseñas **WLAN** desaparecerá.

Aunque puedes instalar o retomar estas funciones instalándolas manualmente mientras sean compatibles.

## MYSQL
Estos son los querys que he utilizado para comunicarme con mi base de datos MySQL local y lo que suelo utilizar para que mi API se comunique con la DB en remoto.

En caso de utilizar otra base de datos, según el motor utilizado puede cambiar la sintaxis, por ejemplo PostgreSQL en Supabase.

### CREA LA TABLA
```
CREATE TABLE table_name (
    id INT AUTO_INCREMENTAL PRIMARY KEY,
    ssid VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(200) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### CREA UN TRIGGER PARA ACTUALIZAR 
```
CREATE TRIGGER trigger_name
AFTER INSERT ON table_name
FOR EACH ROW
BEGIN
    UPDATE table_name
    SET updated_at = CURRENT_TIMESTAMP
    WHERE id = NEW.id;
END;
```

> [!NOTE]
> Para **PostgreSQL** es necesario que primero crees una **función** que llevara la lógica de actualización y después tendrás que crear el **trigger** *vinculandolo* a la función.