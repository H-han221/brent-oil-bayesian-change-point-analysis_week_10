## Assumptions and Limitations

### Key Assumptions
- Brent oil price dynamics can be partially explained by changes in statistical properties (mean and volatility).
- Major geopolitical, economic, and OPEC-related events influence market expectations and behavior.
- Log returns are a suitable transformation to stabilize variance and support time series modeling.
- Market reactions may occur slightly before or after the documented event dates.

### Correlation vs Causation
This analysis identifies statistical change points in the time series and compares their timing with known real-world events. While temporal alignment suggests potential associations, it does not prove causal impact.

Change point detection highlights *when* a structural change occurs, but not *why* it occurs. Multiple overlapping factors—including speculation, currency movements, and global demand—may contribute to observed price changes. Therefore, all event associations are interpreted as hypotheses rather than definitive causal conclusions.
## Communication of Results

To ensure insights are actionable for different stakeholders, results will be communicated using multiple formats:

- **Investors:**  
  Concise reports and interactive dashboards highlighting regime shifts, volatility changes, and probabilistic price impacts.

- **Policymakers:**  
  Written analytical reports supported by visual evidence of structural breaks, focusing on economic stability and energy security implications.

- **Energy Companies:**  
  Dashboards and summary briefs emphasizing operational risk, supply disruptions, and price uncertainty.

Primary communication channels include:
- A written analytical report (PDF or Medium-style blog)
- An interactive web-based dashboard (Flask + React)
- Visual summaries and plots embedded in presentations
## Bayesian Change Point Models in the Brent Oil Context

Bayesian change point models are used to identify points in time where the statistical properties of a time series change. In the context of Brent oil prices, such changes may reflect shifts in market regimes caused by geopolitical conflicts, economic crises, sanctions, or OPEC policy decisions.

The model assumes that the time series can be divided into distinct segments, each characterized by its own parameters (such as mean price or volatility). A latent variable, known as the change point, represents the unknown date at which the transition between regimes occurs. Bayesian inference is used to estimate the posterior distribution of this change point, allowing uncertainty to be explicitly quantified.

### Expected Model Outputs
- **Posterior distribution of change point dates**, indicating when a structural break most likely occurred  
- **Parameter estimates before and after the change point**, such as shifts in average price or volatility  
- **Credible intervals**, reflecting uncertainty in both timing and magnitude of changes  

### Interpretation in the Brent Oil Market
Detected change points will be compared with major geopolitical and economic events (e.g., wars, sanctions, OPEC decisions). Temporal alignment suggests potential associations between events and price regime shifts, providing probabilistic insights into how global developments influence oil markets.

### Limitations
- Change point detection identifies statistical breaks, not causal mechanisms  
- Multiple overlapping events may contribute to a single detected change  
- Market anticipation or delayed reactions may shift the timing relative to event dates  

Despite these limitations, Bayesian change point models provide a robust framework for understanding regime changes under uncertainty.
