from django.conf.urls import patterns, url 
from .views import *

urlpatterns = [	
	url(r'^$',login_view, name = 'vista_login'),
	url(r'^logout/$',logout_view , name = 'vista_logout'),
	url(r'^edit_user/$',edit_user_view, name = 'vista_edit_user'),
	url(r'^edit_password/$',edit_password_view, name = 'vista_edit_password'),
	url(r'^admin_edit_password/(?P<id_user>.*)/$',admin_edit_password_view, name = 'vista_admin_edit_password'),
	url(r'^password_guardado_admin/$',password_guardado_admin_view, name = 'vista_password_guardado_admin'),
	url(r'^password_guardado_user/$',password_guardado_user_view, name = 'vista_password_guardado_user'),
	url(r'^index/$',index_view , name = 'vista_index'),
	url(r'^administrador/$',administrador_view , name = 'vista_administrador'),
	url(r'^registro/$',register_view, name = 'vista_registro'),
	url(r'^user/$',user_view, name = 'vista_user'),
	url(r'^admin_user/(?P<id_user>.*)/$',admin_user_view, name = 'vista_admin_user'),
	url(r'^instructores/page/(?P<pagina>.*)/$',instructores_view, name = 'vista_instructores'),
	url(r'^reportes/(?P<id_mes>.*)/$',reportes_view, name = 'vista_reportes'),
	url(r'^consultar/page/(?P<pagina>.*)/(?P<id_mes>.*)/$',consultar_view , name = 'vista_consultar'),
	url(r'^admin_edit_user/(?P<id_user>.*)/$',admin_edit_user_view, name = 'vista_admin_edit_user'),

	url(r'^del/reporte/(?P<id_reporte>.*)/$',del_reporte_view, name = 'vista_eliminar_reporte'),	
	#url(r'^del/reporte_enero/(?P<id_reporte>.*)/$',del_reporte_enero_view, name = 'vista_eliminar_reporte_enero'),
	#url(r'^del/reporte_enero/(?P<id_reporte>.*)/$',del_reporte_enero_view, name = 'vista_eliminar_reporte_enero'),
	#url(r'^del/reporte_febrero/(?P<id_reporte>.*)/$',del_reporte_febrero_view, name = 'vista_eliminar_reporte_febrero'),
	#url(r'^del/reporte_marzo/(?P<id_reporte>.*)/$',del_reporte_marzo_view, name = 'vista_eliminar_reporte_marzo'),
	#url(r'^del/reporte_abril/(?P<id_reporte>.*)/$',del_reporte_abril_view, name = 'vista_eliminar_reporte_abril'),	
	#url(r'^del/reporte_mayo/(?P<id_reporte>.*)/$',del_reporte_mayo_view, name = 'vista_eliminar_reporte_mayo'),
	#url(r'^del/reporte_junio/(?P<id_reporte>.*)/$',del_reporte_junio_view, name = 'vista_eliminar_reporte_junio'),
	#url(r'^del/reporte_julio/(?P<id_reporte>.*)/$',del_reporte_julio_view, name = 'vista_eliminar_reporte_julio'),
	#url(r'^del/reporte_agosto/(?P<id_reporte>.*)/$',del_reporte_agosto_view, name = 'vista_eliminar_reporte_agosto'),
	#url(r'^del/reporte_septiembre/(?P<id_reporte>.*)/$',del_reporte_septiembre_view, name = 'vista_eliminar_reporte_septiembre'),
	#url(r'^del/reporte_octubre/(?P<id_reporte>.*)/$',del_reporte_octubre_view, name = 'vista_eliminar_reporte_octubre'),
	#url(r'^del/reporte_noviembre/(?P<id_reporte>.*)/$',del_reporte_noviembre_view, name = 'vista_eliminar_reporte_noviembre'),																								
	#url(r'^del/reporte_diciembre/(?P<id_reporte>.*)/$',del_reporte_diciembre_view, name = 'vista_eliminar_reporte_diciembre'),								
	#url(r'^enero/$',enero_view , name = 'vista_enero'),
	#url(r'^febrero/$',febrero_view , name = 'vista_febrero'),
	#url(r'^marzo/$',marzo_view , name = 'vista_marzo'),
	#url(r'^abril/$',abril_view , name = 'vista_abril'),
	#url(r'^mayo/$',mayo_view , name = 'vista_mayo'),
	#url(r'^junio/$',junio_view , name = 'vista_junio'),
	#url(r'^julio/$',julio_view , name = 'vista_julio'),
	#url(r'^agosto/$',agosto_view , name = 'vista_agosto'),
	#url(r'^septiembre/$',septiembre_view , name = 'vista_septiembre'),
	#url(r'^octubre/$',octubre_view , name = 'vista_octubre'),
	#url(r'^noviembre/$',noviembre_view , name = 'vista_noviembre'),
	#url(r'^diciembre/$',diciembre_view , name = 'vista_diciembre'),
	
	#url(r'^consultar_febrero/$',consultar_febrero_view , name = 'vista_consultar_febrero'),
	#url(r'^consultar_marzo/$',consultar_marzo_view , name = 'vista_consultar_marzo'),
	#url(r'^consultar_abril/$',consultar_abril_view , name = 'vista_consultar_abril'),
	#url(r'^consultar_mayo/$',consultar_mayo_view , name = 'vista_consultar_mayo'),
	#url(r'^consultar_junio/$',consultar_junio_view , name = 'vista_consultar_junio'),
	#url(r'^consultar_julio/$',consultar_julio_view , name = 'vista_consultar_julio'),
	#url(r'^consultar_agosto/$',consultar_agosto_view , name = 'vista_consultar_agosto'),
	#url(r'^consultar_septiembre/$',consultar_septiembre_view , name = 'vista_consultar_septiembre'),
	#url(r'^consultar_octubre/$',consultar_octubre_view , name = 'vista_consultar_octubre'),
	#url(r'^consultar_noviembre/$',consultar_noviembre_view , name = 'vista_consultar_noviembre'),
	#url(r'^consultar_diciembre/$',consultar_diciembre_view , name = 'vista_consultar_diciembre'),
]	