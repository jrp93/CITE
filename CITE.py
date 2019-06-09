from io import open
import urllib2
import string



archivo = open("Unidad_11_leccion_1.doc","w") 

leccion_1_titulo = "APARATOS PARA EL INTERCAMBIO DE SUSTANCIAS \n \n"
leccion_1_aparato_digestivo = "Aparato digestivo: \n es el encargado de tomar los alimentos del exterior y de prepararlos y transformarlos, para que puedan ser utilizados por todas las celulas del cuerpo \n \n"
leccion_1_aparato_respiratorio = "Aparato respiratorio: \n se encarga del intercambio gaseoso, capta oxigeno y expulsa dioxido de carbono \n \n"
leccion_1_aparato_circulatorio = "Aparato circulatorio: \n transporta los nutrientes, el oxigeno y los desechos producidos en la nutricion celular \n \n"
leccion_1_aparato_excretor = "Aparato excretor: \n expulsa al exterior los desechos de la nutricion celular"


archivo.write(unicode(leccion_1_titulo + leccion_1_aparato_digestivo + leccion_1_aparato_respiratorio + leccion_1_aparato_circulatorio + leccion_1_aparato_excretor))
archivo.close()


archivo_2 = open("Unidad_11_leccion_2.doc","w")

leccion_2_titulo = "EL APARATO DIGESTIVO \n \n"
leccion_2_anatomia_del_aparato_digestivo = "ANATOMIA DEL APARATO DIGESTIVO \n \n" 
leccion_2_el_tubo_digestivo = "El tubo digestivo: \n \n Es un conducto, de unos diez metros de longitud, constituido por la boca, la faringe, el esofago, el estomago, el intestino delgado, el intestino grueso y el ano. \n \n"
leccion_2_las_glandulas_digestivas = "Las glandulas digestivas: \n \n encargadas de producir los jugos necesarios para la digestion quimica de los alimentos en el interior del tubo digestivo. \n \n Estas son: \n \n Glandulas salivales \n \n Glandulas gastricas \n \n Higado \n \n Pancreas \n \n Glandulas intestinales \n \n "
leccion_2_etapas_del_proceso_digestivo = "ETAPAS DEL PROCESO DIGESTIVO \n \n"
leccion_2_Ingestion = "Ingestion: \n \n Entrada de alimentos en el tubo digestivo a traves de la boca. \n \n"
leccion_2_Digestion = "Digestion: \n \n Transformacion de los alimentos en sustancias mas sencillas, dos tipos: \n \n -Mecanicas: cortar, triturar y remover los alimentos(boca y estomago) reducen el tamaNo de los alimentos y mezclan sus componentes. \n \n -Quimicas: transformar los alimentos en compuestos mas sencillos, gracias a la accion de los jugos digestivos. \n \n"
leccion_2_Absorcion = "Absorcion: \n \n Proceso por el cual los nutrientes obtenidos en la digestion atraviesan la pared del tubo digestivo y pasan a la sangre. \n \n"
leccion_2_Defecacion = "Defecacion: \n \n Eliminacion al exterior de las sustancias no digeridas o no aprovechables."



archivo_2.write(unicode(leccion_2_titulo + leccion_2_anatomia_del_aparato_digestivo + leccion_2_el_tubo_digestivo + leccion_2_las_glandulas_digestivas + leccion_2_etapas_del_proceso_digestivo + leccion_2_Ingestion + leccion_2_Digestion + leccion_2_Absorcion + leccion_2_Defecacion))
archivo_2.close()
