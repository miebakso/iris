from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from pandas import read_csv
import os.path, requests, logging

logger = logging.getLogger(__name__)

def index(request):
    context = {'test':10}
    url =  settings.MEDIA_ROOT + '/iris.csv'

    # Download and store file in DIR if not exist 
    if(not os.path.isfile(url)):
        iris_url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
        r = requests.get(iris_url, allow_redirects=True)
        open(url, 'w').write(r.text)
        logger.info('berhasil download')
        
    # iris data set
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    dataset = read_csv(url, names=names)
    context['head'] = dataset.head().to_json()
    logger.info(dataset.head())
    logger.info(type(dataset))
    logger.info(context['head'])

    #print(settings.MEDIA_ROOT+"ASD")
    #path = default_storage.save('iris.csv', dataset.to_csv('iris.csv'))
    #print(path)
    #default_storage.save('iris.csv', dataset.to_csv('iris.csv'))
    #file_name = default_storage.save('iris.csv', dataset.to_csv('iris.csv'))
    return render(request, 'iris/index.html', context)