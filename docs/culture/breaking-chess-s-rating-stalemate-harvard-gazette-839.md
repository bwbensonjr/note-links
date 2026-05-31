---
id: 839
url: https://news.harvard.edu/gazette/story/2026/02/breaking-chesss-rating-stalemate/
title: Breaking chess’s rating stalemate — Harvard Gazette
domain: news.harvard.edu
source_date: '2026-02-14'
tags:
- news
- academic-paper
- gaming
summary: 'Harvard statistician Mark Glickman has developed a breakthrough ranking
  system for chess that addresses a fundamental flaw in existing ratings: they fail
  to account for the high probability of draws among elite players, where over 70%
  of games end without a winner. His new Bayesian model replaces fixed tie parameters
  with strength-dependent ones, allowing for more accurate predictions of wins, losses,
  and draws based on player skill levels. The International Correspondence Chess Federation
  adopted his system in 2023, and Glickman suggests the framework could also improve
  rankings in other sports like soccer, boxing, and cricket.'
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Breaking chess’s rating stalemate — Harvard Gazette

Here’s a statistical challenge worthy of a grandmaster: How do you create an accurate ranking system when the best players usually don’t win?

This is the conundrum of elite chess. The stronger the players, the greater the odds of the match ending in a draw.

“What ended up happening,” said [Mark Glickman](https://www.glicko.net/), senior lecturer in the Department of Statistics and longtime chess enthusiast, “is that these top players were not having their ratings change very much, just because the games would be drawn all the time.”

Now Glickman has devised a solution: the first-ever ranking system that takes account of player strength when estimating the probability of a tie.

Chess may be the quintessential game of skill, but oftentimes top-ranked competitors cancel each other out and prevent a decisive outcome. Among elite chess grandmasters, more than 70 percent of competitions end in ties. And that is just conventional “over the board” chess; in the growing realm of online competition known as “correspondence chess,” some 95 percent of matches end without a winner.

Even epic matchups have ended indecisively. In the 2018 world chess championships between Magnus Carlsen and Fabiano Caruana, all 12 games ended in draws — for the first time in history. One analyst asked, [“Is Classical Chess Dead From Draws?”](https://www.chess.com/article/view/the-draw-rule-is-classical-chess-dead)

Not only chess faces this deadlock dilemma. In simpler games such as checkers or tic-tac-toe, a match is guaranteed to end without a winner if neither player makes a mistake. Likewise, ties are common in sports such as soccer or cricket.

So Glickman decided it was time for a new statistical approach to rankings.

> “These top players were not having their ratings change very much, just because the games would be drawn all the time.”

As a child in New Jersey, he started playing chess around age 5, entered U.S. Chess Federation tournaments by age 11, and eventually attained the title of chess master. As an undergraduate at Princeton, he was appointed to the ratings committee of the U.S. Chess Federation and a few years later became chair of the committee while a Ph.D. student at Harvard.

Paired comparison models are widely used to measure relative strengths of competitors in games and sports. These systems are important not only for ranking-obsessed fans and players, but also for establishing betting odds or organizing tournament brackets.

In chess, most existing rating systems accounted only for win-loss outcomes and treated ties as half a win and half a loss. They did not explicitly model the probability of a draw — even though it was the most common outcome among top competitors.

“As a result, these systems may produce stagnant ratings,” observed Glickman, “especially for elite players.”

To address that shortcoming, Glickman built a new system. He adapted a widely used paired comparison model but replaced the fixed tie parameters with ones that incorporated measures of player strength. The new version, he says, yields a “richer and more realistic representation of competitive outcomes.”

Glickman presented his new model in two recent papers in the [Journal of Data Science](https://jds-online.org/journal/JDS/article/1455/info) and [Statistical Modeling](https://journals.sagepub.com/doi/abs/10.1177/1471082X251400474).

“My innovation basically allows you to come up with much more accurate probabilities of wins, losses, and draws — draws in particular,” said Glickman. “Before this, the probability of a draw would just simply not depend on how strong the players were. Now, if I have two strong players, my model allows me to predict that the probability of a draw is actually quite large. We would not have been able to do that before.”

Glickman began working on the new model several years ago and in 2021 the International Correspondence Chess Federation (ICCF) commissioned him to develop a revised rating system. Two years later, the organization adopted his model for its player rankings.

Austin Lockwood, the ICCF services director, said the organization turned to Glickman because its old rating system from the 1980s had become outdated. In recent years, online chess competitors have relied more and more on computer engines to help them plan moves. “It is increasingly difficult for strong players to find wins, even against a relatively weaker player,” he said. “The effect of this has been that nearly all games between highly rated players are now draws.”

He said the adoption of the Glickman system had gone smoothly for the ICCF.

“It does seem to be performing well so far,” Lockwood said. “Players (especially correspondence chess players) take a while to get used to change, but we haven’t had many complaints, which suggests that is has been well-received.”

Glickman believes that the ICCF is the first major organization to implement a rating algorithm that models the probability of a tie as a strength-dependent outcome.

He suggests the framework also might be useful in soccer, boxing, or cricket. (Ties also used to be more frequent in professional hockey until 2005, when the NHL introduced shootouts at the end of overtime.)

Glickman, who also serves as co-director of graduate studies in the Department of Statistics, often has applied his expertise beyond the University. Last year, he won the American Statistical Association’s Founders Award for his longtime service to the organization, and he currently chairs the ASA Committee on Data Science and AI.

When he appears at public events, odds are high that he will inject a little fun. He performs magic tricks and sings stat geek parody songs such as “Bayesian Believer” (a takeoff on “Daydream Believer”) and “Valencia Wood” (after “Norwegian Wood”).

But there’s one hobby he doesn’t have much time for these days: chess.

“I still play, but not competitively because of the amount of time it takes to remain competitive,” Glickman said, gesturing at shelves of chess books behind his desk. “I would have to be studying hours per day.”

#### Share this article



* ![](/wp-content/themes/harvard-gazette/assets/svg/facebook.svg)[Share on Facebook](#)
* ![](/wp-content/themes/harvard-gazette/assets/svg/linkedin.svg)[Share on LinkedIn](#)
* ![](/wp-content/themes/harvard-gazette/assets/svg/email.svg)[Email article](#)
* ![](/wp-content/themes/harvard-gazette/assets/svg/print.svg)[Print/PDF](javascript:window.print())
