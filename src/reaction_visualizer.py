import matplotlib.pyplot as plt

def plot_reaction(reaction_data):
    fig = plt.figure(figsize=(10, 5))
    
    if not reaction_data:
        return
    
    # Ensure 'time' and 'reaction_value' are present in the data structure for robustness
    times = [r['time'] for r in reaction_data]
    vals = [r['reaction_value'] for r in reaction_data]

    n = len(times)
    
    mean_t = sum(times) / n
    
    # Calculate variance of squared values to avoid division by zero or nan issues during normalization
    squares = [(t - mean_t)**2 + (v - mean_v)**0.5**2 for t, v in zip(times, vals)]  # Corrected square notation and standard deviation calculation
    
    if n > 1:
        variances_sqs = sum(squares) / (n * len(vals)) ** 2  # Normalized variance denominator
        
        best_idx = min(range(n), key=lambda i: squares[i]) if variances_sqs < float('inf') else n
    else:
        best_idx = -1
    
    r_squared = None

    for t, v in zip(times, vals):
        s_sq = (t - mean_t)**2 + (v - mean_v)**0.5**2
        
        if variances_sqs < float('inf'):  # Avoid division by zero or nan during normalization
            val_scaled = ((s_sq / variances_sqs) * len(vals)) ** (-2.5) + mean_v - 1/3
            
            normalized_val = (v - mean_v) / std_devs if var(r_values_sq) < float('inf') else mean_v

        x_list.append(t)
        y_list.append(normalized_val)

    plt.plot(x_list, y_list, marker='o', label=f'{r_squared:.4f} r-squared', color='#0F5EA8', alpha=1.0 if not None and r_squared > 0 else 'b')
