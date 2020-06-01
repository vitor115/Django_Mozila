from django.shortcuts import render
from django.views import generic
from catalog.models import Book, Author, BookInstance, Genre



def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    #Genres and book with a particular word
    num_lovecraft = Book.objects.filter(author__last_name__contains='Lovecraft').count
    num_mistery = Book.objects.filter(genre__name__exact='Mistério').count
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_lovecraft': num_lovecraft,
        'num_mistery':num_mistery,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
    #context_object_name = 'my_book_list'   # your own name for the list as a template variable
    #queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    #template_name = 'books/book_detail.html'  # Specify your own template name/location

    #def get_queryset(self):
    #    return Book.objects.filter(title__icontains='Cthulhu')[:5] # Get 5 books containing the title war

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        print(context)
        context['usuario'] = 'This is just some data'
        return context

class BookDetailView(generic.DetailView):
    model = Book
    
#Outro Metodo de Implementar com try catch
#def book_detail_view(request, primary_key):
#    try:
#        book = Book.objects.get(pk=primary_key)
#    except Book.DoesNotExist:
#        raise Http404('Book does not exist')
#    
#    return render(request, 'catalog/book_detail.html', context={'book': book})
# OU
#from django.shortcuts import get_object_or_404
#def book_detail_view(request, primary_key):
#    book = get_object_or_404(Book, pk=primary_key)
#    return render(request, 'catalog/book_detail.html', context={'book': book})