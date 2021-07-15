def checkAir(samples, threshold):
    ordered_samples = sorted(samples)
    clean = 0
    dirty = 0
    for sample in ordered_samples:
        if sample == "clean":
            clean += 1
    dirty += 1
    pollution_rate = (clean / (dirty + clean))*100
    pollution_accepted = threshold * 100
    round(pollution_rate, 2)
    round(pollution_accepted, 2)
    if pollution_rate > pollution_accepted:
        return f"Polluted ({pollution_rate}% out of {pollution_accepted}%)"
    return f"Clean ({pollution_rate}% out of {pollution_accepted}%)"


print(checkAir(
  ['clean', 'clean', 'dirty', 'clean', 'dirty', 'clean', 'clean', 'dirty', 'clean', 'dirty'],
  0.3
))

print(checkAir(
  ['dirty', 'dirty', 'dirty', 'dirty', 'clean'],
  0.25
))

print(checkAir(
  ['clean', 'dirty', 'clean', 'dirty', 'clean', 'dirty', 'clean'],
  0.9
))