import pymc as pm
import numpy as np


def run_change_point_model(returns: np.ndarray):
    """
    Bayesian change point model for mean shift in log returns.

    Parameters
    ----------
    returns : np.ndarray
        1D array of log returns (numeric, no dates)

    Returns
    -------
    trace : arviz.InferenceData
        Posterior samples
    """
    if returns.ndim != 1:
        raise ValueError("Expected a 1D array of log returns")

    returns = returns.astype(float)

    n = len(returns)
    idx = np.arange(n)

    with pm.Model() as model:
        # Prior for change point
        tau = pm.DiscreteUniform("tau", lower=0, upper=n - 1)

        # Priors for means before and after change
        mu_1 = pm.Normal("mu_1", mu=0, sigma=1)
        mu_2 = pm.Normal("mu_2", mu=0, sigma=1)

        # Shared volatility
        sigma = pm.HalfNormal("sigma", sigma=1)

        # Switch function
        mu = pm.math.switch(idx < tau, mu_1, mu_2)

        # Likelihood
        pm.Normal("obs", mu=mu, sigma=sigma, observed=returns)

        # Sampling
        trace = pm.sample(
            draws=2000,
            tune=1000,
            target_accept=0.95,
            return_inferencedata=True,
            progressbar=True
        )

    return trace
