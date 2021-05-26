# Hands-on Test Instructions

Test Vocabulary Note: "must" means they're the most important parts of the test, "should" means they're important but less important than "must".

This test has three parts:

1. Player/Hero/PlayerHero/Game models
2. Recording games
3. Calculating stats

# 1. Player/Hero/PlayerHero/Game models
This is all about the underlying models and database structure.
Once you've created the models and registered them to Django admin, you'll be able to go to http://localhost:8000/admin/ and create entries from there, without writing anything for the frontend.

## 1.a. Player model
Already created before this test: http://localhost:8000/admin/players/player/

## 1.b. Hero model
This represents the actual hero, as well as overall stats for that hero across all players.
This can contain a lot of fields, but the ones needed for the test are:

The Hero model must have these fields:

- `name`: Char[30], the hero's name.
- `winrate`: Decimal, the hero's global winrate, in percentage format (1 decimal place). For example: 52.6
- `num_games`: Integer, the hero's total number of games.

When you print out this hero (`print(hero)`), it should print out the hero's name.

## 1.c. PlayerHero model
This represents a player's stats with a hero, containing the total stats that player has with that hero.

The PlayerHero model must have these fields:

- `player`: Foreign Key to Player, you
- `hero`:  Foreign Key to Hero, your hero
- `winrate`: Decimal, your winrate for this hero, in percentage format (1 decimal place). For example: 70.5
- `num_games`: Integer, your total number of games for this hero

## 1.d. Game model
This represents an individual game for one player. All the data only pertains to that player: what hero did you use, did you win, what's your KDA.
We may extend this to represent the stats for all players within this game, but that's not within the scope of this test.

The Game model must have these fields:

- `player`: Foreign Key to Player, the player adding this game
- `hero`:  Foreign Key to Hero, the hero you used
- `result`: Integer with options: 1 = Win, 2 = Loss, 3 = Invalid
- `kills`: Integer, your number of kills
- `deaths`: Integer, your number of deaths
- `assists`: Integer, your number of assists
- `date`: DateTime, when the game started
- `duration`: Duration, how long the game took

All of these fields should be registered to Django admin.
Once they're registered, go add add some heroes through Django admin. You'll need them for Part 2.

# 2. Recording games

## 2.a. Recording a game

When you're logged in to http://localhost:8000/, you'll see a link called "Enter your latest games here!".
When clicked, this link must go to a new page containing a form with these fields:

- Hero: a select dropdown showing all the heroes in the system
- Result: a select dropdown with these options: "Win", "Loss", "Invalid"
- Kills: a number textbox
- Deaths: a number textbox
- Assists: a number textbox
- Date: a text box, pre-populate this with the current date
- Duration: a text box, accepting a duration in "minutes:seconds" format (like "25:44")

And then a "Save" button to finish recording that game.

What's not included on this page is the Player field. When the player hits "Save", it should automatically link that game to the current logged-in player.
After hitting "Save", it should redirect the player back to the home page.

## 2.b. Rendering your games
There is a section in the home page (http://localhost:8000/) named "Your Last 5 Games". This table must show the current logged-in player's last 5 games, in descending order (latest game on top). The home.html template already has a suggested markup for rendering these games; you may use it or change it to match your models.

# 3. Calculating stats
Whenever a player records a game, the system must recompute both the total stats for that hero and the player's stats for that hero.

## 3.a. Total stats
Here are the formulas for the two Hero model fields:

- `num_games = number of games won + number of games lost` (this ignores invalid games)
- `winrate = number of games won / num_games * 100`

## 3.b. Your stats
One extra consideration here is that if it's your very first time recording a game for a hero, you do not have a PlayerHero entry yet. In this case, the system must create that PlayerHero entry between you and the hero, and then compute the stats with that game. (If you already have a PlayerHero entry, just retrieve that and recompute the stats.)

The formulas are the same as above, but only limited to the games the player has with that hero (instead of all games by all players).

## 3.c. Rendering the stats
There are two sections in the home page called "Your Top 5 Favorite Heroes" and "Top 5 Global Heroes". These sections must contain the top 5 heroes (your top 5 / everyone's top 5), ordered by winrate. The sample markup in home.html assumes you're pulling the data for "Your Top 5" from the PlayerHero model, while "Top 5 Global" pulls from the Hero model. Feel free to reuse / change it.

