# Commerce Django Project

## Overview
Commerce is a Django web application that allows users to create auction listings, make bids, add items to a watchlist, and interact with various features related to online auctions.


## Features
- **Models:**
  - Auction listings
  - Bids
  - Comments on auction listings
  - User watchlist

- **Create Listing:**
  - Users can create a new listing with a title, description, starting bid, optional image URL, and category.

- **Active Listings Page:**
  - Displays all currently active auction listings with essential details.

- **Listing Page:**
  - Detailed page for each listing with the option to:
    - Add/remove the item from the watchlist.
    - Bid on the item (if signed in).
    - Close the auction (if the creator and signed in).
    - Display winner information (if signed in and won).

- **Watchlist:**
  - Users can view a page displaying all listings added to their watchlist.

- **Categories:**
  - Users can explore listings by category.

- **Django Admin Interface:**
  - Administrators can perform CRUD operations on listings, bids, and comments through the Django admin interface.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/commerce.git
   cd commerce
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser for the admin interface:
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Visit `http://localhost:8000/admin` to log in as the superuser and manage the application through the Django admin interface.

## Usage
- Visit the default route (`http://localhost:8000/`) to explore active listings.
- Sign in to access additional features such as creating listings, bidding, and managing watchlists.

## Contributions
Contributions are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md).

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- Special thanks to the Django community and contributors.

```

.
