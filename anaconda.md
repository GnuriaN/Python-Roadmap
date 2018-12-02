# Anaconda
![https://www.anaconda.com/wp-content/themes/anaconda/images/logo-dark.png](https://www.anaconda.com/wp-content/themes/anaconda/images/logo-dark.png)

**Anaconda** - это дистрибутив с установленным в него "большим" набором инструментов для работы с данными. Он основан да систему управления версий [Conda](https://conda.io/docs/). Скачать свежую версию, всегда можно скачать с [https://www.anaconda.com/download](https://www.anaconda.com/download/).

Что входив с состав данного дистрибутива?
![./img/anaconda_navigator.png](./img/anaconda_navigator.png)    

## Jupyter Lab
**JupyterLab** – гибкой, интегрируемой и легко расширяемой среды, поддерживающей одновременную работу с несколькими блокнотами Jupyter, текстовыми файлами, датасетами, терминалами и другими компонентами. Аналогично классическим IDE в JupyterLab можно упорядочивать документы в рабочей области в удобном порядке при помощи вкладок и разделителей.
![./img/anaconda_jupyterlab.png](./img/anaconda_jupyterlab.png)    

## Notebook
**Jupyter Notebook** – это крайне удобный инструмент для создания красивых аналитических отчетов, так как он позволяет хранить вместе код, изображения, комментарии, формулы и графики:
![./img/anaconda_jupyternotebook.png](./img/anaconda_jupyternotebook.png)    
![./img/anaconda_jupyternotebook_view.png](./img/anaconda_jupyternotebook_view.png)    

P.S. Есть очень интересная статья, которая посвещена этим двум инструментам: [https://proglib.io/p/jupyter/](https://proglib.io/p/jupyter/)

Существует небольшой "косяк" (_ну это я так щитаю_), по умолчанию эти программы (_в операционной среде Windows_)запускаются с рабочей диреторией `%USERPROFILE%`, и чтобы это исправить, нужно изменить запуск в ярлыках, или запускать программы с укаханием директорий.    
Пример:
```console
C:\Anaconda\V3-5.0.1\envs\My\Scripts> jupyter-lab.exe %Anaconda%
```
или
```console
C:\Anaconda\V3-5.0.1\python.exe C:\Anaconda\V3-5.0.1\cwp.py C:\Anaconda\V3-5.0.1 C:\Anaconda\V3-5.0.1\python.exe C:\Anaconda\V3-5.0.1\Scripts\jupyter-notebook-script.py %Anaconda%
```
где `%Anaconda%` - это переменная окружения. Но вы всегда можете создать и свои `костыли` =)
```console
> echo %Anaconda%
E:\!Git!
```

## Qt Console
**Qt Console** - это GUI для реализации IPython.
![./img/anaconda_qt_console.png](./img/anaconda_qt_console.png)    

## Spyder
**Spyder** - свободная и кроссплатформенная интерактивная IDE для научных расчетов на языке Python, обеспечивающая простоту использования функциональных возможностей и легковесность программной части.
![./img/anaconda_qt_spyder.png](./img/anaconda_spyder.png)    

## Glueviz

## Orange 3

## RStudio

## VS code