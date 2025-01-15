import django
import sys
import os

project_root = os.path.abspath(os.path.dirname(__file__) + '/../')
sys.path.insert(0, project_root)
print(os.getenv('DJANGO_SETTINGS_MODULE'))


os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
django.setup()

from api.models import Category

categories = {
    "Electronics":[
        "Mobile Phones",
        "Laptops & Computers",
        "Tablets",
        "Smartwatches",
        "Audio devices",
        "Cameras & Photography",
        "Home Appliances",
        "Networking Devices",
        "Wearable Tech",
        "Gadgets"
    ],
    "Fashion":[
        "Men Clothing",
        "Women Clothing",
        "Kids Wear"
        "Footwear",
        "Accessories",
        "Jewelry",
        "Bags",
        "Sportswear",
        "Traditional Wear",
    ],
    "Home & Kitchen":[
        "Furniture",
        "Kitchen Appliances",
        "Home Decoration",
        "Bedding",
        "Cleaning Supplies",
        "Storage & Organization",
        "Cookware & Utensils",
        "Gardening",
    ],
    "Health & Fitness":[
        "Fitness Equipment",
        "Supplements",
        "Yoga & Meditation",
        "Sports Equipments",
        "Rehabilitation Aids",
        "Hygiene Products"
    ],
    "Gaming":[
        "Gaming Console",
        "Gaming Accessories",
        "PC Gaming",
        "VR Equipment",
        "Gaming Chairs",
        "Collectibles"
    ],
    "Beauty & Personal Care":[
        "Skincare",
        "Haircare",
        "Makeup",
        "Fragrances",
        "Men's Grooming",
        "Beauty tools",
        "Personal Hygiene",
    ],
    "E-reading & Books":[
        "E-readers",
        "Fiction",
        "Non-Fiction",
        "Academic Textbook",
        "Children",
        "Magazines & Journals",
        "Audiobooks",
    ],
    "Toys & Hobbies":[
        "Figures & Collectibles",
        "Building & Construction",
        "Educational",
        "Puzzle & Board game",
        "Outdoor",
        "Remote Controlling",
        "Art & Crafting",
        "Music & Instrumentals"
    ],
    "Office":[
        "Stationary",
        "Office Furniture",
        "Storage Solutions",
        "Printer & Scanners",
        "Paper Products",
        "Writable Board",
    ],
    "Travel & Outdoor":[
        "Luggage",
        "Safety Gears",
        "Camping",
    ]
}
def populate_categories():
    for supercategory, subcategories in categories.items():
        supercategory_obj, _ = Category.objects.get_or_create(name=supercategory, parent_id=None)
        for subcategory in subcategories:
            Category.objects.get_or_create(name=subcategory, parent_id=supercategory_obj)

if __name__ == "__main__":
    populate_categories()