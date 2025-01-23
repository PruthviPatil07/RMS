# Restaurant Management System (RMS)

## Project Description
The Restaurant Management System (RMS) is a Python-based application designed to streamline restaurant operations, such as managing orders, generating bills, and verifying payments. The system includes a user-friendly command-line interface and a basic GUI created with Tkinter for enhanced usability.

## Features
- **Menu Display**: Users can view the restaurant's menu with item names and prices.
- **Order Processing**: Customers can place orders, which are then prepared and served virtually.
- **Billing System**: Automatically calculates the total bill and handles payment verification.
- **Repeat Orders**: Allows customers to add more items to their order.
- **Graphical User Interface**: A simple Tkinter GUI for starting the order process.

## Technologies Used
- **Programming Language**: Python
- **GUI Framework**: Tkinter
- **Time Simulation**: `time` module for simulating order preparation

## Usage
1. Run the script:
    ```bash
    python rms.py
    ```
2. A Tkinter GUI window will appear with a "Start" button. Click the button to begin the order process.
3. Follow the prompts to place your order, view your bill, and make payment.

## Code Overview
### Main Class: `RMS`
- **Attributes**:
  - `restaurant_name`: Name of the restaurant.
  - `restaurant_menu`: Dictionary containing menu items and their prices.
  - `user_bill`, `user_order`, `user_pay`: Track bill amount, order, and payment status.
- **Methods**:
  - `Welcome_user()`: Displays a welcome message.
  - `Display_menu()`: Shows the menu to the user.
  - `Take_order()`: Takes the user's order.
  - `Prepare_order()`: Simulates order preparation.
  - `Sereve_order()`: Displays a message when the order is ready.
  - `Display_bill()`: Shows the total bill amount.
  - `Verify_payment()`: Handles payment verification.
  - `Thank_user()`: Displays a thank-you message.
  - `Order_process()`: Main workflow to handle the order process.
  - `Repeat_order()`: Allows additional orders.

### Tkinter GUI
- **Window Title**: `Pruthvi Patil`
- **Window Dimensions**: 400x400 pixels
- **Elements**:
  - Welcome label
  - "Start" button to begin the order process

## Example Menu
The following items are available in the default menu:
- Pizza: ₹599
- Burger: ₹150
- Fries: ₹100
- Cold Coffee: ₹199
- Choco: ₹200
- Nuggets: ₹349
- Shake: ₹279
- Sandwich: ₹99
- Lassi: ₹80
- Brownie: ₹149


