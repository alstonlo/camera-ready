# Report variability and compare like with like

A comparison between two numbers is a claim whose evidence includes their variability. For every reported comparison, the sentence, caption, or a convention stated once in the text must specify:

- How many runs each number covers and how it summarizes them (mean, median, or best run).
- Whether ± denotes a standard deviation, standard error, or confidence interval.
- What varies (seed, data split, or the test examples a bootstrap resamples).

Flag any missing information.

Both sides of a comparison must be computed the same way. A best-run number is not comparable with a mean of final results; a number copied from another publication is comparable only under the same evaluation protocol. Flag every comparison for which the text does not establish that both sides were computed alike. When the ranking of methods changes with the aggregate metric, limit each claim to the metric that produced it.
