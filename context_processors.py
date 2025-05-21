
def categories(request):
    categories = [
    'programming',
    'Food',
    "Travel"
]
    return {'categories' : categories}
