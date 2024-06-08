# Proyecto MLOps: Entrenamiento y Despliegue Continuo de Modelos con GitHub Actions y DVC

Este proyecto demuestra la implementación de prácticas de MLOps (Operaciones de Machine Learning) para automatizar el entrenamiento y despliegue continuo de modelos de machine learning. Utilizando GitHub Actions y DVC (Data Version Control), gestionamos todo el ciclo de vida del ML, desde la versionización de datos hasta el despliegue de modelos, asegurando reproducibilidad, escalabilidad y colaboración.

## Tecnologías
- **GitHub Actions**: Automatiza flujos de trabajo para integración y despliegue continuos.

- **DVC (Data Version Control): **Sistema de control de versiones para gestionar datos, modelos y experimentos.

- **AWS S3**: Almacenamiento en la nube escalable para conjuntos de datos y modelos.

- **Python:** Lenguaje de programación utilizado para el procesamiento de datos, entrenamiento de modelos y scripts de despliegue.

- **Docker:** Contenerización para entornos de desarrollo y producción consistentes.

## Prerrequisitos

- ** Git** 

- **DVC**

- **Python**

-  **AWS**

## Instalación

**1.** **Clonar el repositorio:**

```bash
git clone https://github.com/tuusuario/tu-repo-nombre.git
cd tu-repo-nombre
```
**2.  Instalar las dependencias de Python:**
```bash
pip install -r requirements.txt
```
**3. Configurar DVC con tu almacenamiento remoto:**
```bash
dvc remote add -d miremoto s3://nombre-del-bucket/ruta/a/datos
dvc remote modify miremoto region nombre-de-la-region
```
## **Uso**
**1.  Añadir y subir datos al almacenamiento remoto:**
```bash
dvc add data/tu-conjunto-de-datos.csv
dvc push
```

**2. Entrenamiento de Modelos:**
Desencadenar el entrenamiento del modelo mediante GitHub Actions al subir cambios al repositorio:

```bash
git add .
git commit -m "Desencadenar entrenamiento del modelo"
git push origin main
```
**3. Despliegue Continuo:**
El pipeline CI/CD desplegará automáticamente el modelo actualizado basado en los flujos de trabajo definidos en .github/workflows/.







