## David Jun Kim
| Fecha | ¿Qué he hecho desde el último daily SCRUM? | ¿Qué haré durante el día de hoy? | ¿He visto o encontrado algún impedimento? |
| --- | --- | --- | --- |
| 19-09-2023 | Di inicio al primer Sprint. Sin embargo, no desarrollé ninguna historia de usuario | Durante el día de hoy, empezaré a desarrollar al menos una de las actividades que me corresponden | Por el momento no he encontrado ningún impedimento. |
| 20-09-2023 | Iniciar con el desarrollo de mis historias de usuario | Continuar con el desarrollo de las historias de usuario asignadas a mí | Tengo dudas sobre como implementar la funcionalidad de los reportes debido que, no tengo los datos suficientes |
| 26-09-2023 | Adelantar la implementación de las vistas para los informes | Terminaré las vistas de los informes | Aún no he logrado la implementación para cargar archivos |
| 27-09-2023 | Realice mucho refactor a las vistas del proyecto | Terminar de una vez por todas las vistas de los informes y la funcionalidad de cargar archivos | Necesitamos tiempo y más compromiso |
| 28-09-2023 | Sigo desarrollando la funcionalidad para subir archivos | Terminar la funcionalidad de subir los archivos para implementar otra funcionalidad | Actualmente me encuentro sin internet en el lugar donde resido, entonces me veo limitado al uso de internet en la universidad para consultar documentación |
| 02-10-2023 | Estuve trabajando en la implementación de la funcionalidad para subir archivos. Sin embargo, debido a inconvenientes personales no he podido avanzar mucho | Implementar al menos una funcionalidad especificada en el tablero de Jira | Por el momento, mucha carga academica por mi parte |
| 03-10-2023 | Implemente la funcionalidad para cargar archivos al programa. Sin embargo, aún quedan detalles por pulir y mejorar.| Implementaré al menos una funcionalidad pendiente en el tablero de SCRUM. | Para la funcionalidad de subir archivos, no encontré mucha documentación al respecto. |

## Juan Lora

| Fecha | ¿Qué he hecho desde el último daily SCRUM? | ¿Qué haré durante el día de hoy? | ¿He visto o encontrado algún impedimento? |
| --- | --- | --- | --- |
| 20-09-2023 | Inicie familiarizandome con el proyecto. Di una vista básica para Home, y cree una vista (y su path) para el cronograma/calendar | (Mañana) Crear un html para la vista Calendar | No sé si la redirección debería ser mediante el html(e.g con el '<a>') o mediante Django|
| 25-09-2023 | Creé las vistas básicas/generales de la aplicacion, el nav bar menu (resta el de gestión de informes, Jun lo hará) y creé un formulario con html para agregar un Cronograma| Crear un forms con Django para agregar cronograma | Necesito reafianzar los conceptos de Django forms, en primer lugar|
| 26-09-2023 | Se creó una base del formulario usando django| Completar el formulario con los datos necesarios para agregar cronograma, además, establecer su metodo POST | Solucionados los previos|
| 27-09-2023 | Configuré el formulario para funcionar con POST y se testeó manualmente con la DB| Terminar el formulario con todos los datos necesarios para agregar cronograma | time! |
| 28-09-2023 | Modelo de calendario creado con sus campos de fecha| Buscar e implementar una alternativa para los campos de fecha en el formulario, para practidad del end-user, y optimización del metodo POST| La forma en la que se reciben los datos por POST, funciona, pero quizá es ineficiente y quedaría muy largo. Debe cambiarse |
| 02-10-2023 | _(madrugada)_ Modifiqué el modelo del cronograma/calendario, además muestro los registros en la pantalla 'Calendar' y finalmente, cuando se clickean, se abre una nueva pantalla con la información del cronograma (Se empezó otra feature)| Dormir! y ya haré otro *daily-Scrum* ahora en la mañana temprano| No he podido enviar un objeto mediante la sintaxis jinja, lo máximo que consegui fue hacerlo pero sobre la misma view, y utilizando query|


## Jeison Lasprilla
| Fecha | ¿Qué he hecho desde el último daily SCRUM? | ¿Qué haré durante el día de hoy? | ¿He visto o encontrado algún impedimento? |
| --- | --- | --- | --- |
| 25-09-2023 | Familiarizandome con el proyecto, solucioné algunos problemas con la cofiguración del proyecto en mi maquina| Iniciaré con la implementación del API_R6_2: Inicio de Sesión a través de Credenciales de la API de Banner | Aun no termino por definir si sea buena idea hacer el inicio de sesión dependiente de las Credenciales de la API de Banner|
| 26-09-2023 | Hice un redireccionamiento a la pagina de la universidad para ingresar con banner| Relacionar los datos al ingresar en banner con el proyecto | Tenía problemas con la autenticación social con banner, encontré una solución que espero probar mañana|
| 27-09-2023 | Intente realizar el inicio de sesión con un API REST o un OAuth con banner| Saltaré a otro requerimiento por ahora y organizaré el redireccionamiento a banner de manera opcional | Se dificulta los servicios de autenticación al no contar con información puntual de la universidad para hacer el API REST o OIDC|
| 03-10-2023 | Cree la tabla app_becas_my_user en la base de datos y la vinculé con el django | Mejorar el diseño del html y subir al develop | Dificultades para hacer los reportes en el daily el mismo día |

## Santiago Prado Larrarte
| Fecha | ¿Qué he hecho desde el último daily SCRUM? | ¿Qué haré durante el día de hoy? | ¿He visto o encontrado algún impedimento? |
| --- | --- | --- | --- |
| 27-09-2023 | Solucione el problema que tenia con mi computador mac, por lo tanto este ultimo dia me puse al dia con el proyecto | Cree el metodo en la vista de   becas para buscar una beca por el nombre|Si, se debe crear la clase becas para ponerles los atributos y poderme a referir a el nombre de la beca, ya que, es necesario para mi feat de buscar beca por su nombre
| 29-09-2023 | Repase un poco mas el proyecto y me puse al dia con algunas tareas que tenia | Cree el metodo en la vista de becas para añadir una nueva beca|La clase beca sigue sin estar definida, por lo tanto no es posible probar los metodos aun, el dia de mañana lo definire y pondre a prueba los metodos creados 
| 01-10-2023 | Planifique las tares que tengo que realizar | Cree la clase beca con los atributos de name,description,type y amount|Ya que cree la clase beca, ahora toca relacionarlo con el html y verificar que los metodos creados anteriormente, funcionen correctamente
| 02-10-2023 | Me propuse realizar la estructura en html de las diferentes pestañas en la gestion de becas | Realice la estructura de html en la pestaña becas|No, me falta realizar la estructura de las demas pestañas de la gestion de becas y contectar los forms con la base de datos para realizar la prueba de los metodos


