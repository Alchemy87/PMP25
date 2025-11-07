from scipy.stats import gamma

total_calls = 180
total_time = 10

alpha_post = 1 + total_calls
beta_post = 1 + total_time

print("Posterior: Gamma(", alpha_post, ",", beta_post, ")")

hdi_low = gamma.ppf(0.03, alpha_post, scale=1/beta_post)
hdi_high = gamma.ppf(0.97, alpha_post, scale=1/beta_post)
print("94% HDI:", hdi_low, hdi_high)

mode = (alpha_post - 1) / beta_post
print("Mode:", mode)
