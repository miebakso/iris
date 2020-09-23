from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from pandas import read_csv
import os.path, requests, logging

logger = logging.getLogger(__name__)

def index(request):
    context = {}
    url = settings.MEDIA_ROOT + '/iris.csv'

    # Download and store file in DIR if not exist 
    if(not os.path.isfile(url)):
        iris_url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
        r = requests.get(iris_url, allow_redirects=True)
        open(url, 'w').write(r.text)
        logger.info('berhasil download')

    # iris data set
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    dataset = read_csv(url, names=names)

    # data set description
    shape = dataset.shape
    context['total_elements'] = shape[0]
    context['total_attributes'] = shape[1]
    context['labels'] = names

    # data head()
    datahead = []
    temp = dataset.head(10)
    i = 0
    for x in temp:
        j = 0
        while j < len(temp[x]):
            if i < len(temp):
                datahead.append([])
                datahead[j].append(temp[x][j])
                i+=1
            else:
                print(x)
                datahead[j].append(temp[x][j])
            j+=1

        
    context['head'] = datahead
    print(temp)
    
    #logger.info(dataset.head())
    #logger.info(type(dataset))
    #logger.info(context['head'])

    return render(request, 'iris/index.html', context)