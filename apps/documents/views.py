from django.shortcuts import render_to_response, get_object_or_404

from apps.documents.models import Document


def index(request):
    documents = Document.objects.values_list('title', 'slug')
    print documents
    return render_to_response("documents/index.html", {'documents': documents})


def document_detail(request, slug):
    return render_to_response('documents/document_detail.html', {
        'item': get_object_or_404(Document, slug=slug)
    })
