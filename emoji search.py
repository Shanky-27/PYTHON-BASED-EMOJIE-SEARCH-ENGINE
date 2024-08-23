
import tkinter as tk
from tkinter import font

# Dictionary mapping emojis to their text representations
emoji_to_text = {
    "😀": "Grinning Face",
    "😃": "Grinning Face with Big Eyes", 
    "😄": "Grinning Face with Smiling Eyes",
    "😁": "Beaming Face with Smiling Eyes", 
    "😆": "Grinning Squinting Face", 
    "😅": "Grinning Face with Sweat",
    "😂": "Face with Tears of Joy", 
    "🤣": "Rolling on the Floor Laughing", 
    "😊": "Smiling Face with Smiling Eyes",
    "😇": "Smiling Face with Halo", 
    "🙂": "Slightly Smiling Face", 
    "🙃": "Upside-Down Face",
    "😉": "Winking Face", 
    "😌": "Relieved Face", 
    "😍": "Smiling Face with Heart-Eyes",
    "🥰": "Smiling Face with Hearts", 
    "😘": "Face Blowing a Kiss", 
    "😗": "Kissing Face",
    "😙": "Kissing Face with Smiling Eyes", 
    "😚": "Kissing Face with Closed Eyes", 
    "😋": "Face Savoring Food",
    "😛": "Face with Tongue", 
    "😜": "Winking Face with Tongue", 
    "🤪": "Zany Face",
    "😝": "Squinting Face with Tongue", 
    "🤑": "Money-Mouth Face", 
    "🤗": "Hugging Face",
    "🤭": "Face with Hand Over Mouth", 
    "🤫": "Shushing Face", 
    "🤔": "Thinking Face",
    "🤐": "Zipper-Mouth Face", 
    "🤨": "Face with Raised Eyebrow", 
    "😐": "Neutral Face",
    "😑": "Expressionless Face", 
    "😶": "Face Without Mouth", 
    "😏": "Smirking Face",
    "😒": "Unamused Face", 
    "🙄": "Face with Rolling Eyes", 
    "😬": "Grimacing Face", 
    "🤥": "Lying Face",
    "😌": "Relieved Face", 
    "😔": "Pensive Face", 
    "😪": "Sleepy Face", 
    "🤤": "Drooling Face",
    "😴": "Sleeping Face", 
    "😷": "Face with Medical Mask", 
    "🤒": "Face with Thermometer",
    "🤕": "Face with Head-Bandage", 
    "🤢": "Nauseated Face", 
    "🤮": "Face Vomiting", 
    "🤧": "Sneezing Face",
    "🥵": "Hot Face", 
    "🥶": "Cold Face", 
    "🥴": "Woozy Face", 
    "😵": "Dizzy Face",
    "🤯": "Exploding Head", 
    "🤠": "Cowboy Hat Face", 
    "🥳": "Partying Face", 
    "😎": "Smiling Face with Sunglasses",
    "🤓": "Nerd Face", 
    "🧐": "Face with Monocle", 
    "😕": "Confused Face", 
    "😟": "Worried Face",
    "🙁": "Slightly Frowning Face", 
    "☹️": "Frowning Face", 
    "😮": "Face with Open Mouth",
    "😯": "Hushed Face", 
    "😲": "Astonished Face", 
    "😳": "Flushed Face", 
    "🥺": "Pleading Face",
    "😦": "Frowning Face with Open Mouth", 
    "😧": "Anguished Face", 
    "😨": "Fearful Face",
    "😰": "Anxious Face with Sweat", 
    "😥": "Sad but Relieved Face", 
    "😢": "Crying Face",
    "😭": "Loudly Crying Face", 
    "😱": "Face Screaming in Fear", 
    "😖": "Confounded Face",
    "😣": "Persevering Face", 
    "😞": "Disappointed Face", 
    "😓": "Downcast Face with Sweat",
    "😩": "Weary Face", 
    "😫": "Tired Face", 
    "🥱": "Yawning Face", 
    "😤": "Face with Steam From Nose",
    "😡": "Pouting Face", 
    "😠": "Angry Face", 
    "🤬": "Face with Symbols on Mouth",
    "😈": "Smiling Face with Horns", 
    "👿": "Angry Face with Horns", 
    "💀": "Skull",
    "☠️": "Skull and Crossbones", 
    "💩": "Pile of Poo", 
    "🤡": "Clown Face", 
    "👹": "Ogre",
    "👺": "Goblin", 
    "👻": "Ghost", 
    "👽": "Alien", 
    "👾": "Alien Monster", 
    "🤖": "Robot",
    "😺": "Grinning Cat", 
    "😸": "Grinning Cat with Smiling Eyes", 
    "😹": "Cat with Tears of Joy",
    "😻": "Smiling Cat with Heart-Eyes", 
    "😼": "Cat with Wry Smile", 
    "😽": "Kissing Cat",
    "🙀": "Weary Cat",
    "😿": "Crying Cat",
    "😾": "Pouting Cat", 
    "👶": "Baby", 
    "👧": "Girl",
    "🧒": "Child", 
    "👦": "Boy", 
    "👩": "Woman", 
    "🧑": "Person", 
    "👨": "Man",
    "👩‍🦱": "Woman: Curly Hair", 
    "🧑‍🦱": "Person: Curly Hair", 
    "👨‍🦱": "Man: Curly Hair",
    "👩‍🦰": "Woman: Red Hair", 
    "🧑‍🦰": "Person: Red Hair"
}

class EmojiSearchApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Emoji Search")

        self.entry_font = font.Font(family='Segoe UI Emoji', size=20)

        self.search_label = tk.Label(master, text="Search Emoji:")
        self.search_label.pack()

        self.search_entry = tk.Entry(master, font=self.entry_font)
        self.search_entry.pack()

        self.search_button = tk.Button(master, text="Search", command=self.search_emoji)
        self.search_button.pack()

        self.results_text = tk.Text(master, height=10, width=50)
        self.results_text.pack()

    def search_emoji(self):
        query = self.search_entry.get().lower()
        self.results_text.delete('1.0', tk.END)
        for emoji, description in emoji_to_text.items():
            if query in description.lower():
                self.results_text.insert(tk.END, f"{emoji} - {description}\n")

def main():
    root = tk.Tk()
    app = EmojiSearchApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

