# Python Learning Lab

A portfolio of Python applications covering terminal programs, desktop interfaces, API integration, browser automation, and Flask. Each project includes its own setup and usage instructions. Prototype limitations are documented alongside the implementation.

## Technologies and concepts

Python, object-oriented design, control flow, collections, file I/O, CSV processing, Turtle, Tkinter, Pandas, Requests, BeautifulSoup, Selenium, and Flask.

## Projects

### Python Fundamentals

| Project | Description |
|---|---|
| [Band Name Generator](python-fundamentals/band-name-generator/) | Combines a hometown and pet name into a suggested band name. |
| [Tip Calculator](python-fundamentals/tip-calculator/) | Calculates a per-person share of a bill including a percentage tip. |
| [Treasure Island](python-fundamentals/treasure-island/) | A branching terminal adventure driven by player choices. |
| [Rock Paper Scissors](python-fundamentals/rock-paper-scissors/) | Plays a terminal round against a randomly selected computer move. |
| [Password Generator](python-fundamentals/password-generator/) | Builds a password candidate by placing random characters into a list. |
| [Hangman](python-fundamentals/hangman/) | A terminal word-guessing game with staged ASCII illustrations. |
| [Caesar Cipher](python-fundamentals/caesar-cipher/) | Shifts alphabetic characters using modular arithmetic. |
| [Secret Auction](python-fundamentals/secret-auction/) | Collects named bids and reports the highest bidder. |
| [Calculator](python-fundamentals/calculator/) | An interactive arithmetic calculator that can reuse the previous result. |
| [Blackjack](python-fundamentals/blackjack/) | A simplified terminal card-total game against a computer dealer. |
| [Number Guessing Game](python-fundamentals/number-guessing-game/) | Asks the player to identify a random integer using high/low feedback. |
| [Higher Lower Game](python-fundamentals/higher-lower-game/) | Compares follower counts from a local profile dataset. |

### Object-Oriented Programs, Games, and GUIs

| Project | Description |
|---|---|
| [Coffee Machine](oop-games-gui/coffee-machine/) | Models drink recipes, ingredient availability, and coin payments in a terminal interface. |
| [Dot Painting](oop-games-gui/hirst-painting/) | Draws two randomly colored dots from a fixed RGB palette. |
| [Turtle Race](oop-games-gui/turtle-race/) | Animates a race among six turtles with randomized movement. |
| [Snake Game](oop-games-gui/snake-game/) | An object-oriented Snake game with food, growth, collision resets, and a saved high score. |
| [Pong Game](oop-games-gui/pong-game/) | A local two-player Pong game with paddles, scoring, and accelerating rallies. |
| [Turtle Crossing](oop-games-gui/turtle-crossing/) | A road-crossing game with moving cars and progressively faster traffic. |
| [Mail Merge](oop-games-gui/mail-merge/) | Creates personalized letters by replacing a name placeholder in a text template. |
| [U.S. States Game](oop-games-gui/us-states-game/) | Labels correctly guessed U.S. states on a map using CSV coordinates. |
| [NATO Alphabet](oop-games-gui/nato-alphabet/) | Converts entered letters into NATO phonetic alphabet words using CSV data. |
| [Miles to Kilometers Converter](oop-games-gui/miles-to-km-converter/) | Converts an integer distance in miles into kilometers in a desktop window. |
| [Pomodoro Timer](oop-games-gui/pomodoro-timer/) | Alternates timed work sessions with short and long breaks. |
| [Flash Card App](oop-games-gui/flash-card-app/) | Displays French vocabulary cards, reveals translations, and records remaining words. |

### APIs and Automation

| Project | Description |
|---|---|
| [Quizzler](apis-automation/quizzler-app/) | Fetches true/false trivia questions and presents them in a desktop quiz. |
| [Rain Alert](apis-automation/rain-alert/) | A weather-response prototype that checks condition codes and prints an umbrella reminder. |
| [Stock and News Prototype](apis-automation/stock-news-alert/) | Queries daily stock prices and calculates a percentage change for fixed dates. |
| [Habit Tracker Configuration](apis-automation/habit-tracker/) | Builds account, graph, and daily-entry request payloads for Pixela. |
| [Workout Tracker](apis-automation/workout-tracker/) | Parses natural-language exercise input through an API and writes workout rows to a spreadsheet endpoint. |

### Web Foundations

No standalone projects are currently included in this category.

### Web Scraping and Browser Automation

| Project | Description |
|---|---|
| [Top Movies Scraper](web-scraping-selenium/top-100-movies-scraper/) | Extracts ranked movie headings from an archived film article and writes them to a text file. |
| [Musical Time Machine](web-scraping-selenium/musical-time-machine/) | Scrapes chart song titles for a date and builds a YouTube Music playlist. |
| [Cookie Clicker Bot](web-scraping-selenium/cookie-clicker-bot/) | Clicks cookies and periodically attempts to purchase an affordable product. |
| [Dating Interface Automation](web-scraping-selenium/tinder-swiping-bot/) | Automates a demo dating interface login flow and performs a single like action. |
| [Follower Interface Automation](web-scraping-selenium/instagram-follower-bot/) | Signs into a demo social interface, opens an account follower list, and clicks follow buttons. |

### Flask Web Applications

| Project | Description |
|---|---|
| [Flask Routes](flask-web-apps/flask-introduction/) | A small Flask application serving two text routes. |
| [Name Card Website](flask-web-apps/name-card-website/) | Serves a responsive profile card through Flask and a third-party HTML/CSS template. |

## Running a project

Open a project README, create a separate virtual environment, and install its requirements when present. Run scripts from their project directory to resolve local resources. Desktop apps require Tk support; browser automation requires Chrome and compatible selectors.

## Configuration and data

Projects that need environment variables include `.env.example` with placeholder values. Scripts read process environment variables; examples are not automatically loaded. Private authentication files, browser profiles, and local credentials must remain outside version control.

## Attribution

Third-party designs, datasets, and assets are retained with their applicable notices. The name-card website identifies its template and asset credits in its own README.
