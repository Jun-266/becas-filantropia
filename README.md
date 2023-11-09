## David Jun Kim
| Fecha      | ¿Qué he hecho desde el último daily SCRUM?                                                                                                                                               | ¿Qué haré durante el día de hoy?                                                                  | ¿He visto o encontrado algún impedimento?                                                                                                                  |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 19-09-2023 | Di inicio al primer Sprint. Sin embargo, no desarrollé ninguna historia de usuario                                                                                                       | Durante el día de hoy, empezaré a desarrollar al menos una de las actividades que me corresponden | Por el momento no he encontrado ningún impedimento.                                                                                                        |
| 20-09-2023 | Iniciar con el desarrollo de mis historias de usuario                                                                                                                                    | Continuar con el desarrollo de las historias de usuario asignadas a mí                            | Tengo dudas sobre como implementar la funcionalidad de los reportes debido que, no tengo los datos suficientes                                             |
| 26-09-2023 | Adelantar la implementación de las vistas para los informes                                                                                                                              | Terminaré las vistas de los informes                                                              | Aún no he logrado la implementación para cargar archivos                                                                                                   |
| 27-09-2023 | Realice mucho refactor a las vistas del proyecto                                                                                                                                         | Terminar de una vez por todas las vistas de los informes y la funcionalidad de cargar archivos    | Necesitamos tiempo y más compromiso                                                                                                                        |
| 28-09-2023 | Sigo desarrollando la funcionalidad para subir archivos                                                                                                                                  | Terminar la funcionalidad de subir los archivos para implementar otra funcionalidad               | Actualmente me encuentro sin internet en el lugar donde resido, entonces me veo limitado al uso de internet en la universidad para consultar documentación |
| 04-10-2023 | Estuve trabajando en la HU, P1MB-29. Sin embargo, por falta de comunicación con el equipo, mi trabajo fue desechado debido que, la funcionalidad la estaba desarrollando otro compañero. | Estuve trabajando brevemente en la HU, P1MB-34                                                    | Por el momento ninguno.                                                                                                                                    |
| 09-10-2023 | Terminé la funcionalidad para subir archivos a la aplicación                                                                                                                             | Implementaré la funcionalidad P1MB-28 del tablero                                                 | Por el momento, no he encontrado ningún impedimento                                                                                                        |
| 10-10-2023 | Estoy a la espera de que me acepten mi pull request para hacer merge con la rama develop y sigo trabajando en la funcionalidad P1MB-28 | Hoy estuve haciendo unos pequeños retoques para hacer la interfaz para la carga de archivos más pulida | Por el momento, no he encontrado ningún impedimento. |
| 11-10-2023 | Trabajar en la implementación de la funcionalidad P1MB-28 | No trabaje en el proyecto porque estaba repasando para otras materias | Ninguno. |
| 13-10-2023 | Trabaje muy poco en la funcionalidad P1MB-28 y no he terminado su implementación | Pulire la GUI para los informes y añadiré los loginrequired haciendo que el usuario tenga que logearse para ver los informes | Por el momento no he encontrado ningún impedimento. |
| 26-10-2023 | Implementé la funcionalidad para eliminar informes. | Implementaré la funcionalidad para generar informes de acuerdo a los requerimientos del cliente. | No he encontrado impedimento alguno. |
| 08-11-2023 | Añadí los archivos necesarios junto con la configuración necesaria para hacer el deploy de la aplicación. | Revisar de nuevo la configuración para hacer el deploy | La aplicación fue desplegada, pero se muestra una página de error 404. |

## Juan Lora

| Fecha      | ¿Qué he hecho desde el último daily SCRUM?                                                                                                                                                                                                                     | ¿Qué haré durante el día de hoy?                                                                                                            | ¿He visto o encontrado algún impedimento?                                                                                                                                               |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 20-09-2023 | Inicie familiarizandome con el proyecto. Di una vista básica para Home, y cree una vista (y su path) para el cronograma/calendar                                                                                                                               | (Mañana) Crear un html para la vista Calendar                                                                                               | No sé si la redirección debería ser mediante el html(e.g con el '<a>') o mediante Django                                                                                                |
| 25-09-2023 | Creé las vistas básicas/generales de la aplicacion, el nav bar menu (resta el de gestión de informes, Jun lo hará) y creé un formulario con html para agregar un Cronograma                                                                                    | Crear un forms con Django para agregar cronograma                                                                                           | Necesito reafianzar los conceptos de Django forms, en primer lugar                                                                                                                      |
| 26-09-2023 | Se creó una base del formulario usando django                                                                                                                                                                                                                  | Completar el formulario con los datos necesarios para agregar cronograma, además, establecer su metodo POST                                 | Solucionados los previos                                                                                                                                                                |
| 27-09-2023 | Configuré el formulario para funcionar con POST y se testeó manualmente con la DB                                                                                                                                                                              | Terminar el formulario con todos los datos necesarios para agregar cronograma                                                               | time!                                                                                                                                                                                   |
| 28-09-2023 | Modelo de calendario creado con sus campos de fecha                                                                                                                                                                                                            | Buscar e implementar una alternativa para los campos de fecha en el formulario, para practidad del end-user, y optimización del metodo POST | La forma en la que se reciben los datos por POST, funciona, pero quizá es ineficiente y quedaría muy largo. Debe cambiarse                                                              |
| 02-10-2023 | _(madrugada)_ Modifiqué el modelo del cronograma/calendario, además muestro los registros en la pantalla 'Calendar' y finalmente, cuando se clickean, se abre una nueva pantalla con la información del cronograma (Se empezó otra feature)                    | Dormir! y ya haré otro *daily-Scrum* ahora en la mañana temprano                                                                            | No he podido enviar un objeto mediante la sintaxis jinja, lo máximo que consegui fue hacerlo pero sobre la misma view, y utilizando query                                               |
| 04-10-2023 | Explicación de git a compañeros y solución de dudas                                                                                                                                                                                                            | Crear la función de buscar cronograma mediante su id, con metodo get, y mostrarlo en pantalla como único objeto de una lista                | -                                                                                                                                                                                       |
| 05-10-2023 | Se creó la función de buscar cronograma por id de beca asociado, se muestra listado, y al darle click muestra su información                                                                                                                                   | Mostrar la información de cada cronograma completa                                                                                          | -                                                                                                                                                                                       |
| 06-10-2023 | Se muestra la info completa, _Limpié_ un poco el código, creé una nueva rama HU-19 para borrar records, e implementé dicha funcionalidad usando un forms vacio y método post, pero finalmente decidí buscar hacerlo de otra forma. Definí hacerlo con sessions | Implementar la funcionalidad de borrar record de un cronograma con session                                                                  | No sé mucho de como utilizar el request.session                                                                                                                                         |
| 08-10-2023 | Aprendí como utilizar el session. Se implementó el eliminar beca con request.session                                                                                                                                                                           | Crear la funcionalidad de modificar cronograma                                                                                              | -                                                                                                                                                                                       |
| 09-10-2023 | Implementé la funcionalidad de modificar un cronograma, aun falta pulir detalles                                                                                                                                                                               | Terminar la funcionalidad de modificar cronograma, y empezar una nueva rama                                                                 | He tenido algunos problemas al hacer y también aprobar tantos pull request en un día. Debo mejorar en ello                                                                              |
| 10-10-2023 | Modificar cronograma hecho. Se inció la rama para la funcionalidad de enlazar becas a cronogramas                                                                                                                                                              | Trabajar en el enlazar cronograma con beca, para que cuando no exista el cronograma, se pueda crear e inmediatamente enlazar su id          | Aún tengo dificultades para redireccionar cuando se de click a una beca, porque se puede hacer como con Calendar con send_id, pero quiero creer que existe otra forma más fácil         |
| 11-10-2023 | He estado resolviendo problemas de integración entre los codigos de los coequiperos                                                                                                                                                                            | Continuar con esa integración, solución de errores y dirección                                                                              | time!                                                                                                                                                                                   |
| 12-10-2023 | Continué resolviendo problemas de integración                                                                                                                                                                                                                  | Implementar las redirecciones correctamente, utilizando send_id, y mostrar la información de las becas                                      | still time!                                                                                                                                                                                   |
| 19-10-2023 | Esta semana se estuvo haciendo mucho enfasis en el retrospective y el re-planear el sprint para mejorar. Puesto que tuvimos algunos inconvenientes en el previo                                                                                                | Verificar las HU                                                                                                                            |                                                                                                                                                                            |

## Jeison Lasprilla
| Fecha        | ¿Qué he hecho desde el último daily SCRUM?                                                                                                             | ¿Qué haré durante el día de hoy?                                                                                       | ¿He visto o encontrado algún impedimento?                                                                                                           |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| 25-09-2023   | Familiarizandome con el proyecto, solucioné algunos problemas con la cofiguración del proyecto en mi maquina                                           | Iniciaré con la implementación del API_R6_2: Inicio de Sesión a través de Credenciales de la API de Banner             | Aun no termino por definir si sea buena idea hacer el inicio de sesión dependiente de las Credenciales de la API de Banner                          |
| 26-09-2023   | Hice un redireccionamiento a la pagina de la universidad para ingresar con banner                                                                      | Relacionar los datos al ingresar en banner con el proyecto                                                             | Tenía problemas con la autenticación social con banner, encontré una solución que espero probar mañana                                              |
| 27-09-2023   | Intente realizar el inicio de sesión con un API REST o un OAuth con banner                                                                             | Saltaré a otro requerimiento por ahora y organizaré el redireccionamiento a banner de manera opcional                  | Se dificulta los servicios de autenticación al no contar con información puntual de la universidad para hacer el API REST o OIDC                    |
| 05 -10 -2023 | Actualicé mi rama con los cambios de develop                                                                                                           | Hacer el enum de los roles y organizar las opciones en una caja de selección. También iniciar con el modelo de donante | No he podido dedicar mucho tiempo al proyecto entre semana                                                                                          |
| 06 -10 -2023 | Hice el enum con los roles y modifiqué el hmtl con bootstrap                                                                                           | Iniciar con el modelo de donante y definir respecto a que continuar                                                    | -                                                                                                                                                   |
| 07 -10 -2023 | Continué modificando el hmtl con bootstrap y finalicé este requerimiento. Inicié feat-27                                                               | Terminar la relación modelo - donante                                                                                  | Este es mi ultimo requerimiento, así que posterior a este tendré que aportar realizando cambios que ayuden asemejar el proyecto al mockup del figma |
| 08 -10 -2023 | Creé los modelos de donante, contacto, los relacioné entre sí y con las becas. También cambié el html del login para conseguir una vista más amigable. | Conectar la relación beca - donante con el html que corresponda                                                        | -                                                                                                                                                   |
| 09 -10 -2023 | Creé un delete user y espero hacer un modificar user que me permita hacer la conexión beca - donante                                                   | Continuar con la relación beca - donante                                               | -                                                                                                                                                   |
| 10 -10 -2023 | Realicé correcciones en delete user y actualicé la rama local con la que se aprobó en el pull request del remoto                                       | Continuar la función de modificar y buscar usuario                                                                 | -                                                                                                                 |
| 13 -10 -2023 | Terminé de hacer la funcionalidad de modificar usuario                                                                                                 | Colocar un campo que permita relacionar la beca y donante con su id y/o hacer busquedas de becas por id                | Queda poco tiempo para finalizar el Sprint 1
| 14 -10 -2023 | Cambié los auto_id de los modelos para almacenarlos como texto, hice la vista y el html de donantes con sus respectivos botones de modificar y eliminar | implementar la logica en los campos de relacionar beca con donante y contacto con donante                             | Ninguno
| 15 -10 -2023 | Implementé la lógica en los campos de relacionar beca con donante y contacto con donante | Hacer un html para los contactos o hacer las busquedas                                 | Ninguno
| 21 -10 -2023 | Modifqué la vista de editar donante, definí en lo que voy a trabajar este fin de semana mientras iniciamos el sprint. Comencé por agregar y mostrar contacto | Hacer la función de eliminar y editar contacto| Ninguno
| 22 -10 -2023 | Hice la función de eliminar y editar contacto | Crear el modelo de Student y avanzar con la base de la vista| Ninguno
| 23 -10 -2023 | Creé el modelo de Student y Major con su relación de 1 a 1 | Avanzar con la vista de Student | Ninguno
| 24 -10 -2023 | Creé la base de la vista de Student e hice un ajuste para solucionar un problema con el manage_user | Continuar con la vista de Student y su relación en la interfaz con Major | Ninguno
| 29 -10 -2023 | Terminé de hacer la función de agregar y borrar Student, también adelante la de modificar para asociar el estudiante con major | Trabajar en la interfaz de modificar student para relacionar con Major  | Ninguno
| 30 -10 -2023 | Terminé de hacer la interfaz de modificar student para agregar major o modificar el estudiante con major | Hacer la relación de beca con estudiante e ir relacionando con el estado de la aplicación a la beca | Ninguno
| 31 -10 -2023 | Al hacer el pull request recibí retroalimentación por parte de mi equipo acerca de la interpretación que había dado a la tabla Major, por lo que volví a cambiar la interfaz de manage student y también la parte de modificar el estudiante para darle la semantica adecuada | Cambiar la relación de la tabla Major con Student y modificar el codigo para que funcione | Encuentro mejoras que se pueden hacer en el modelo relacional, por lo que realizaré unos cambios en las relaciones del modelo actual para que el modelo se mantenga fiel a la realidad y a lo pactado con el equipo
| 01 -11 -2023 | Cambié la relación de la tabla Major con Student e hice las debidas modificaciones para que funcione sin problema | Una vez solucionados el pull request, continuaré con la siguiente hu de relacioinar beca con estudiante y si es posible también ir relacionando con el estado de la aplicación a la beca | Ninguno
| 03 -11 -2023 | Creé un modelo ScholarshipApplication que relaciona los modelos Scholarship y Student. Hice también su propia tabla ApplicationStatus con su columna type y valores especificados | Continuar con la parte grafica de la relación | Ninguno
| 05 -11 -2023 | Ya se puede hacer la relación entre los modelos Scholarship y Student por el id de la beca con un ApplicationStatus por defecto de 'En proceso' | Continuar con el Siguiente requerimiento (feat-5) para gestionar el status del estudiante seleccionado para beca | la verificación que hago en manage_student.py para crear valores iniciales en las tablas tal vez se pueda realizar de una mejor forma
| 06 -11 -2023 | Inicié el requerimiento feat-5 para gestionar el status del estudiante seleccionado para beca, terminé una primera versión sin embargo continuaré con mejoras bajo el mismo requerimiento| Agregar un auto_id a la tabla ScholarshipAplication y continuar mejorando feat-5 | Este es el último requerimieto, tengo varias ideas para continuar una vez finalizado pero primero debo llevarlas al jira. 



## Santiago Prado Larrarte
| Fecha      | ¿Qué he hecho desde el último daily SCRUM?                                                                                             | ¿Qué haré durante el día de hoy?                                                                                                                                                    | ¿He visto o encontrado algún impedimento?                                                                                                                               |
|------------|----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 27-09-2023 | Solucione el problema que tenia con mi computador mac, por lo tanto este ultimo dia me puse al dia con el proyecto                     | Cree el metodo en la vista de   becas para buscar una beca por el nombre                                                                                                            | Si, se debe crear la clase becas para ponerles los atributos y poderme a referir a el nombre de la beca, ya que, es necesario para mi feat de buscar beca por su nombre |
| 29-09-2023 | Repase un poco mas el proyecto y me puse al dia con algunas tareas que tenia                                                           | Cree el metodo en la vista de becas para añadir una nueva beca                                                                                                                      | La clase beca sigue sin estar definida, por lo tanto no es posible probar los metodos aun, el dia de mañana lo definire y pondre a prueba los metodos creados           |
| 01-10-2023 | Planifique las tares que tengo que realizar                                                                                            | Cree la clase beca con los atributos de name,description,type y amount                                                                                                              | Ya que cree la clase beca, ahora toca relacionarlo con el html y verificar que los metodos creados anteriormente, funcionen correctamente                               |
| 02-10-2023 | Me propuse realizar la estructura en html de las diferentes pestañas en la gestion de becas                                            | Realice la estructura de html en la pestaña becas                                                                                                                                   | No, me falta realizar la estructura de las demas pestañas de la gestion de becas y contectar los forms con la base de datos para realizar la prueba de los metodos      |
| 03-10-2023 | Realice la estructura de html de tres historias de usuario                                                                             | Realice la estructura de html en la pestaña becas y en el de registrar nueva beca                                                                                                   | No, me falta realizar la estructura de las demas pestañas de la gestion de becas y contectar los forms con la base de datos para realizar la prueba de los metodos      |
| 04-10-2023 | Me propuse relizar dos funcionalidades y que se conectara el registro con la base de datos                                             | Realice la funcionalidad de registro de becas y la generacion automatica del ID                                                                                                     | No, por ahora no he encontrado un impedimento mas alla de conocer nuevas formas de realizar formularios y conectarlos con la base de datos                              |
| 04-10-2023 | Pude realizar tres funcionalidad las cuales son: Generar ID automatico para las becas, registrar nueva beca y seleccionar tipo de beca | Realice el pull request de las tres funcionalidades y Voy a empezar a trabajar en la funcionalidad de registrar nuevo tipo de beca                                                  | No, por ahora no he encontrado ningun impedimento                                                                                                                       |
| 05-10-2023 | Estoy en proceso de realizar la funcionalidad de agregar nuevo tipo de beca                                                            | El dia de hoy cree el template de adicionar un tipo de beca y cree la vista de adicionar un nuevo tipo de beca, debere hacer el contenido del template para introducir tipo de beca | No, por ahora no he encontrado ningun impedimento aun                                                                                                                   | 
| 08-10-2023 | El dia de hoy estuve trabajando en configurar bien la funcionalidad de agregar beca y culmine la funcionalidad de agregar tipo de beca | El dia de hoy termine y comprobe la funcionalidad de agregar nuevo tipo de beca                                                                                                     | No, por ahora no he encontrado ningun impedimento aun                                                                                                                   |
| 09-10-2023 | El dia de hoy estuve trabajando en implementar la funcionalidad de eliminar tipo de beca| El dia de hoy termine y comprobe la funcionalidad de eliminar un tipo de beca existente                                                                                                     | No, por ahora no he encontrado ningun impedimento aun                                                                                                                   |
| 10-10-2023 | Estoy a la espera de que me acepten mi pull request para continuar con la HU de mostrar informacion de la beca| Comprobe las funcionalidades credas anteriormente                                                                                                    | Si, estoy a la espera de que mi pull request sea aceptado                                                                                                                   |
| 11-10-2023 | Espere la revision de mi pull request y revise los comentarios que se le hicieron| Realice los arreglos que se le pusieron como comoentario en mi pull request y realice el merge con develop                                                                                                  | Si, ahora que corregi el pull request, esperare la confirmacion para continuar realizando otras HU                                                                                                           |
| 12-10-2023 | Pense como seria la HU de buscar una beca por su id| Realice la creacion del html y la view para la nueva HU que voy a trabajar                                                                                                  | Si, mi compañero realizo un metodo de mostrar la informacion de las becas y estoy esperando que se apruebe el pull request que realizo para poner a prueba el metodo de buscar las becas por su id                                                                                                          |
| 13-10-2023 | Trabaje en la funcionalidad de buscar una beca por su nombre| Realice casi toda la funcionalidad pero no se estan mostrando las becas encontradas                                                                                                 | Si, por ahora no me funciona                                                                                                          |
| 17-10-2023 | La funcionalidad de buscar beca por nombre ya quedo hecha, realice el pull request y me hicieron unos comentarios para corregir| Realice la correccion a los comentarios hecho por mi companero y realice el psuh                                                                                                | Estoy a la espera de la aprobacion de mi pull request                                                                                                          |
| 31-10-2023 |Elimine el campo para busqueda en el eliminar tipo de beca| Realice las cards para eliminar tipo de beca seleccionando                                                                                                | No, mañana seguire desarrollando                                                                                                          |
| 1-10-2023 |Finalice la eliminacion del tipo de beca| Realice la funcion de poder seleccionar varios tipos de beca y eliminarlos al tiempo con un mensaje de confirmacion                                                                                                | No, mañana seguire desarrollando                                                                                                          |
| 7-10-2023 |Estoy en proceso de la adicion de los parametros de las becas con referencia al tipo de beca| Realice la adicion de las unidades, el peso porcentual y la cantidad                                                                                                 | No, mañana seguire desarrollando                                                                                                          |


### Nota:
Debido a inconvenientes con algunos compañeros, este archivo quedo modificado de tal forma que, hace parecer que 
Jeison Lasprilla y mi persona (David Kim) no hemos hecho el reporte diario desde el 28 de Septiembre. Recomiendo revisar 
el historial para confirmar de que hemos estado haciendo el reporte diario desde el 02 de Octubre. Gracias por su atención.
