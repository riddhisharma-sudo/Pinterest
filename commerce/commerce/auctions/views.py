from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User , Category , Listing

def listing(request , id ):
    listingData=Listing.objects.get(pk=id)
    isListingInWatchlist = request.user in listingData.watchlist.all()
    isListingInWatchlist=False
    return render(request ,"auctions/listing.html",{
        "listing": listingData,
        "isListingInWatchlist":isListingInWatchlist        
    })

def removeWatchlist(request , id):
    listingData=Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.remove(currentUser)
    return HttpResponseRedirect(reverse("listing",args=(id, )))

def addWatchlist(request , id):
    listingData=Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.add(currentUser)
    return HttpResponseRedirect(reverse("listing",args=(id, )))



def index(request):
    activeListings = Listing.objects.filter(isActive=True)
    allCategories=Category.objects.all()
    return render(request, "auctions/index.html",{
          "listings":activeListings,
          "categories":allCategories,
    })

def displayCategory(request):
    if request.method == "POST":
        categoryFromForm = request.POST['category']
        category = Category.objects.get(categoryName=categoryFromForm)
    activeListings = Listing.objects.filter(isActive=True , category=category)
    allCategories=Category.objects.all()
    return render(request, "auctions/index.html",{
          "listings":activeListings,
          "categories":allCategories,
    })


def createListing(request):
    if request.method == "GET":
        allCategories=Category.objects.all()
        return render(request , "auctions/create.html",{
            "categories":allCategories
        })
    else:
        # get the data from the form
        title = request.POST["title"]
        description = request.POST["description"]
        imageurl =request.POST["imageurl"]
        price = request.POST["Price"]
        category = request.POST["category"] 
        currentUser = request.user
        # create a new listing object
        # get all content about the particular category 
        categoryData = Category.objects.get(categoryName=category)
        newListing = Listing(
            title = title,
            description=description,
            imageUrl=imageurl,
            price = float(price),
            category =categoryData,
            owner = currentUser
        )
        # insert the object in our database
        newListing.save
        # redirect to index page
        return HttpResponseRedirect(reverse(index))
        


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
