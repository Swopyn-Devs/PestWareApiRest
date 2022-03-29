name_login = 'Iniciar sesión'
name_register = 'Crear instancia'
name_profile = 'Obtener Perfil'
name_refresh = 'Refrescar Token'

desc_login = """
Todos los recursos son privados, es decir para lograr interactuar con el API es necesario que nuestras solicitudes 
(peticiones) http sean autorizadas por el backend; Para lograr dicha autorización se requiere de una autenticación
por correo y contraseña. Una vez autenticado se podrá hacer uso de un Json Web Token **JWT** para gestionar una sesión.

Una sesión de usuario tiene un vencimiento de **08 horas** para modo desarrollo, es decir el token expira y será 
necesario solicitar uno nuevo para continuar con la sesión del usuario activo en tu aplicación (web y mobile)."""

desc_register = """
Para crear una nueva cuenta de empresa (instancia) se deberán contemplar las siguientes validaciones:

* El **nombre** de la empresa debe ser **único**.
* La ip del cliente no deberá estar en la lista negra del servidor.
* Preferentemente no usar más de una vez los datos de contacto de la cuenta.

El proceso de creación de cuenta se divide en los siguientes pasos:

1. Creación de usuario.
2. Verificación de usuario por correo.
3. Creación de empresa (instancia).
4. Creación de empleado.
5. Asignación de empleado a cuenta de usuario.
6. Activación de la cuenta (temporalmente).

La **activación de la cuenta** consiste en asignar un período demo (n días) y posterior a ello se deberá realizar
una contratación por parte del cliente mediante el registro de los datos bancarios en Stripe y una vez validado el pago
se activara la cuenta de forma permanente a no ser de que sea suspendida o el cliente no decida contratar."""

desc_profile = 'Regresa el objeto "User" relacionado al token de la sesión.'
desc_refresh = """Estos son tokens de larga duración que se pueden usar para crear nuevos tokens de acceso una vez que
 haya caducado un token de acceso anterior. Los tokens de actualización no pueden acceder a un recurso protegido."""
