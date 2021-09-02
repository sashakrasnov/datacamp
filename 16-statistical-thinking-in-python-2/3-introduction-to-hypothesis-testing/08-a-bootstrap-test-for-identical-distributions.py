import numpy as np
import pandas as pd

def bootstrap_replicate_1d(data, func):
    return func(np.random.choice(data, size=len(data)))

def draw_bs_reps(data, func, size=1):
    return np.array([bootstrap_replicate_1d(data, func) for _ in range(size)])

def diff_of_means(data_1, data_2):
    return np.mean(data_1) - np.mean(data_2)

df = pd.read_csv('../datasets/frog_tongue.csv', comment='#')

df['impact_force'] = df['impact force (mN)'] / 1000

force_a = df[df.ID == 'II'].impact_force.values
force_b = df[df.ID == 'IV'].impact_force.values

forces_concat = np.concatenate((force_a, force_b))
empirical_diff_means = diff_of_means(force_a, force_b)

# Initialize bootstrap replicates: bs_replicates
bs_replicates = np.empty(10000)

for i in range(10000):
    # Generate bootstrap sample
    bs_sample = np.random.choice(forces_concat, size=len(forces_concat))

    # Compute replicate
    bs_replicates[i] = diff_of_means(bs_sample[:len(force_a)],
                                     bs_sample[len(force_a):])

# Compute and print p-value: p
p = np.sum(bs_replicates >= empirical_diff_means) / len(bs_replicates)
print('p-value =', p)
