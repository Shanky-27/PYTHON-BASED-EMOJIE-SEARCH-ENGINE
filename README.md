Emoji Search Application
Overview
The Emoji Search Application is a simple Python GUI application built using Tkinter. It allows users to search for emojis based on their descriptions. The application displays emojis that match the search query along with their textual descriptions.

Features
Search Functionality: Users can enter a keyword in the search box, and the application will display all emojis whose descriptions contain the keyword.
Emoji Display: The application shows emojis with their corresponding text descriptions in a text box.
User-Friendly Interface: The application has an intuitive and easy-to-use interface with a search box, search button, and results display area.
Prerequisites
Python 3.x installed on your system.
Tkinter library (usually comes pre-installed with Python).
Font support for emojis on your system. The application uses the 'Segoe UI Emoji' font, which is commonly available on Windows.
How to Run
Clone the Repository:
cd emoji-search-app
Install Required Libraries:
Tkinter comes pre-installed with Python, so no additional libraries are required.

Run the Application:
Run the emoji_search.py file using Python:

bash
Copy code
python emoji_search.py
Search for Emojis:

Enter a keyword in the search box and click the "Search" button.
The matching emojis along with their descriptions will be displayed in the results area.


Adding More Emojis: The emoji dictionary emoji_to_text can be expanded by adding more emoji-description pairs.
Changing Fonts: The font used for the search input can be customized by modifying the self.entry_font attribute in the EmojiSearchApp class.
