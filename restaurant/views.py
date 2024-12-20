from django.shortcuts import render, get_object_or_404
from .models import Menu

# Function to display the menu
def menu(request):
    menu_data = Menu.objects.all()
    
    # Check if the menu is empty
    if not menu_data:
        message = "No menu items available."  # Message for when there are no items
    else:
        message = None  # If there are items, no message will be displayed
    
    # Passing 'menu' and 'message' to the template
    return render(request, 'menu.html', {'menu': menu_data, 'message': message})

# Function to display a specific menu item
def display_menu_item(request, pk=None):
    # Using get_object_or_404 to avoid exceptions if the item doesn't exist
    menu_item = get_object_or_404(Menu, pk=pk)
    
    # Passing the menu item to the template
    return render(request, 'menu_item.html', {'menu_item': menu_item})

# Function for the about page
def about(request):
    return render(request, 'about.html')  # Ensure you have an 'about.html' template

# Function for the booking page
def book(request):
    return render(request, 'book.html')  # Ensure you have a 'book.html' template
