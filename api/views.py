import json
from rest_framework.views import APIView
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist, ViewDoesNotExist
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import CatalogoPalabras
from .serializers import CatalogoPalabrasSerializador

# Create your views here.

class GetPalabraView(APIView):
    """Vista para el modelo catalogo_palabras de la base de datos donde se puede realizar la operación GET"""
    serializer_class = CatalogoPalabrasSerializador

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(GetPalabraView, self).dispatch(request, *args, **kwargs)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'clave', openapi.IN_PATH, type=openapi.TYPE_INTEGER, description='Clave o ID de la palabra'),
        ],
        responses={
            200: CatalogoPalabrasSerializador,
            404: "Palabra no encontrada",
            500: "Error en el servidor"
        },
        operation_id='get_palabra',
        tags=['Obtener palabra']
    )
    def get(self, request, clave=0):
        """Método para obtener una palabra del catálogo"""
        try:
            print(request.body)
            palabra = list(CatalogoPalabras.objects.filter(id=clave).values())
            if len(palabra) > 0:
                response_data = {'estatus': 200,
                                 'mensaje': 'Palabra encontrada', 'contenido': palabra[0]}
            else:
                response_data = {'estatus': 404,
                                 'mensaje': 'Palabra no encontrada'}
            return JsonResponse(response_data)
        except ViewDoesNotExist:
            return JsonResponse({'estatus': 500, 'mensaje': 'Error en el servidor'}, status=500)


class PostPalabraView(APIView):
    """Vista para el modelo catalogo_palabras de la base de datos donde se puede realizar la operación POST"""

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PostPalabraView, self).dispatch(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            200: "Palabra agregada",
            400: "Datos invalidos",
            500: "Error en el servidor"
        },
        operation_id='post_palabra',
        tags=['Agregar palabra']
    )
    def post(self, request):
        """Método para agregar una palabra al catálogo"""
        try:
            data = json.loads(request.body)
            CatalogoPalabras.objects.create(
                palabra=data['palabra'].upper(),
                caracteres=len(data['palabra']),
                raiz=data['raiz'].upper(),
                letra_inicial=data['palabra'][0].upper()
            )
            response_data = {'estatus': 201, 'mensaje': 'Palabra agregada'}
            return JsonResponse(response_data)
        except json.JSONDecodeError:
            return JsonResponse({'estatus': 400, 'mensaje': 'Datos invalidos', 'detalles': 'Error en el formato JSON'}, status=400)
        except KeyError as e:
            return JsonResponse({'estatus': 400, 'mensaje': 'Datos invalidos', 'detalles': f'Falta el campo obligatorio: {e}'}, status=400)
        except ViewDoesNotExist:
            return JsonResponse({'estatus': 500, 'mensaje': 'Error en el servidor', 'detalles': 'Error en el servidor'}, status=500)


class PutPalabraView(APIView):
    """Vista para el modelo catalogo_palabras de la base de datos donde se puede realizar la operación PUT"""

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PutPalabraView, self).dispatch(request, *args, **kwargs)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'clave', openapi.IN_PATH, type=openapi.TYPE_INTEGER, description='Clave o ID de la palabra'),
        ],
        responses={
            200: "Palabra actualizada",
            400: "Datos invalidos",
            404: "Palabra no encontrada",
            500: "Error en el servidor"
        },
        operation_id='put_palabra',
        tags=['Actualizar palabra']
    )
    def put(self, request, clave=0):
        """Método para actualizar una palabra del catálogo"""
        data = json.loads(request.body)
        try:
            palabra = CatalogoPalabras.objects.get(id=clave)
            palabra.palabra = data['palabra'].upper()
            palabra.caracteres = len(data['palabra'])
            palabra.raiz = data['raiz'].upper()
            palabra.letra_inicial = data['palabra'][0].upper()
            palabra.save()
            response_data = {'estatus': 202, 'mensaje': 'Palabra actualizada'}
            return JsonResponse(response_data)
        except json.JSONDecodeError:
            return JsonResponse({'estatus': 400, 'mensaje': 'Datos invalidos', 'detalles': 'Error en el formato JSON'}, status=400)
        except KeyError as e:
            return JsonResponse({'estatus': 400, 'mensaje': 'Datos invalidos', 'detalles': f'Falta el campo obligatorio: {e}'}, status=400)
        except ObjectDoesNotExist:
            return JsonResponse({'estatus': 404, 'mensaje': 'Palabra no encontrada'}, status=404)
        except ViewDoesNotExist:
            return JsonResponse({'estatus': 500, 'mensaje': 'Error en el servidor'}, status=500)
