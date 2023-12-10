# Define the probabilities
burglary_prob = {"+b": 0.001, "-b": 0.999}
earthquake_prob = {"+e": 0.002, "-e": 0.998}
alarm_prob = {
    ("+b", "+e", "+a"): 0.95, ("+b", "+e", "-a"): 0.05,
    ("+b", "-e", "+a"): 0.94, ("+b", "-e", "-a"): 0.06,
    ("-b", "+e", "+a"): 0.29, ("-b", "+e", "-a"): 0.71,
    ("-b", "-e", "+a"): 0.001, ("-b", "-e", "-a"): 0.999
}
john_calls_prob = {("+a", "+j"): 0.9, ("-a", "+j"): 0.05}

# Calculate joint probabilities including all variables
joint_prob = {}
for b in ["+b", "-b"]:
    for e in ["+e", "-e"]:
        for a in ["+a", "-a"]:
            joint_prob[(b, e, a)] = (
                burglary_prob[b] * earthquake_prob[e] * alarm_prob[(b, e, a)]
            )

# Sum out the Earthquake 'e' and Alarm 'a' variables by summing over their possible values
summed_out_ea = {}
for b in ["+b", "-b"]:
    prob_sum = 0
    for e in ["+e", "-e"]:
        for a in ["+a", "-a"]:
            prob_sum += joint_prob[(b, e, a)] * john_calls_prob[(a, "+j")]
    summed_out_ea[b] = prob_sum

# Normalize the result to get P(B|J=+j)
total_prob = sum(summed_out_ea.values())
normalized_prob = {b: p / total_prob for b, p in summed_out_ea.items()}

# Print the normalized probability distribution for P(B|J=+j)
for b, p in normalized_prob.items():
    print(f"P(B={b}|J=+j) = {p:.6f}")

