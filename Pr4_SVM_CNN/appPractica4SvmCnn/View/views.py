from PIL import Image
from django.shortcuts import render

from Pr4_SVM_CNN.settings import BASE_DIR
from appPractica4SvmCnn.Modelo.forms import ImagenForm
from appPractica4SvmCnn.Logica.modelos import prediccionSVM,prediccionCNN
import os
import uuid
from django.core.files.storage import default_storage
import base64
from django.http import HttpResponse
import numpy as np

()
class Clasificacion():

    def vistaPrincipal(request):
        form = ImagenForm(request.POST, request.FILES)
        if request.method == 'POST' and request.FILES['imagen']:
            imagen = request.FILES['imagen']
            form = ImagenForm(request.POST, request.FILES)

            imagen_procesada = Clasificacion.preprocesar_imagen(imagen)
            imagen_base64 = base64.b64encode(imagen_procesada.tobytes()).decode('utf-8')

            return render(request, 'Principal.html', {'form': form})

        return render(request, "Principal.html",{'form': form})

    @staticmethod
    def preprocesar_imagen(imagen):

        imagen_pil = Image.open(imagen)
        imagen_procesada = imagen_pil.resize((250, 225))
        return imagen_procesada

    def subir_imagen(request):
        if request.method == 'POST':
            form = ImagenForm(request.POST, request.FILES)

            if form.is_valid():
                try:
                    nombre_archivo = str(uuid.uuid4()) + '_' + form.cleaned_data['imagen'].name
                    carpeta_imagenes = os.path.join(BASE_DIR, 'Pr4_SVM_CNN', 'Recursos', 'Imagenes')
                    ruta = os.path.join(carpeta_imagenes, nombre_archivo)

                    # Crear la carpeta si no existe
                    os.makedirs(carpeta_imagenes, exist_ok=True)

                    with default_storage.open(ruta, 'wb+') as destination:
                        for chunk in form.cleaned_data['imagen'].chunks():
                            destination.write(chunk)

                            # Procesa la imagen
                    imagen_or = Image.open(ruta)
                    imagen_pil = imagen_or.resize((32, 32))
                    imagen_np = np.array(imagen_pil)

                    # Llama a tu función de predicción SVM
                    opcion_=form.cleaned_data['opcion']
                    if opcion_ == 'svm':
                        prediccion_resultado = prediccionSVM(imagen_np)
                    elif opcion_ == 'cnn':
                        prediccion_resultado = prediccionCNN(imagen_np)
                    else:
                        raise ValueError('Modelo no reconocido')

                    return render(request, 'resultado.html', {'resultado': prediccion_resultado})
                except Exception as e:
                    return HttpResponse(f'Error al subir la imagen: {str(e)}')

        else:
            form = ImagenForm()

        return render(request, 'Principal.html', {'form': form})
