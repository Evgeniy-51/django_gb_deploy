from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    html_content = """
    <h1> Это мой первый </h1>
    <h2> Django сайт </h2>
    """
    return HttpResponse(html_content)

def about_me(request):
    logger.info('About page accessed')
    html_content = """
    <h1> Это страничка </h1>
    <h2> про меня </h2>
    """
    return HttpResponse(html_content)
