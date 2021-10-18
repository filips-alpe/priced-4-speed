# Welcome to priced-4-speed!

This project aims to calculate where to price crypto orders to have a good fulfill rate.

## The Plan

This is a very rough plan and may change according to discoveries made.

### Step 1

Find out how much volume is being traded on average.

### Step 2

Figure out the probability of each order being filled based on the planned sales volume.

### Step 3

Apply all orders to the market price with the corresponding probability.
If the chance that a particular order will be filled is 50%, and the market price would then rise by 1 unit, average out the market price rising by 1 multiplied by the 0.5 probability = 0.5 units.
We thus arrive at a final market price estimation. Based on this estimation, we calculate the best selling strategy.
As part of this strategy, if we predict that the price is going to change steeply, we might need to sell at lower and buy at higher prices than we otherwise would.

### Step 4

The estimate so far is not supposed to be precise yet. Try and account for the errors introduced by new orders still being placed during the time our order is already listed.
We might be able to estimate that on average a certain quantity of orders is placed soon after our order, in different amplitudes from the market place, and we
would then apply them to the market price too.

### Step 5

Play around with timing. See how accurate the predictions are for 5 seconds or 2 minutes.

#### Notes

Making this a solved problem might require a quite complicated equation of probabilities.
I tried but could not figure it out within the allocated time constraints (one day).

#### Ideas to investigate in the future

Could we ever be able to predict that now is not a great time to sell because the prices would likely rise soon?

It's not only about for how much to sell, but also when to sell.
If we predict that the price is going down in the next 10 seconds, we want to sell ASAP, not after 9 seconds, so we might price under current market value for what would be still over the market value after 9 seconds.
