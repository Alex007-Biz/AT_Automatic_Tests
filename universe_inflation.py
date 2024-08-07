hubble_constant = 70 # km/sec / MParsec
relict_microwave_wavelenght = 0.002 # meter

inflation_speed = hubble_constant / 3.3  # km/sec / 1 mln light years
print(f"inflation_speed = {inflation_speed}, km/sec / 1 mln light years")
wavelenght = relict_microwave_wavelenght
delta_wavelenght = inflation_speed / (1000000 * 300000 * (3600 * 24 * 365))
print(f"delta_wavelenght = {delta_wavelenght}")

distance = 13000 # mln light years
for i in range(1000):
    distance += inflation_speed
    wavelenght += wavelenght * delta_wavelenght

print(f"Distance correct = {distance}, mln light years")
print(f"relict_microwave_wavelenght = {relict_microwave_wavelenght}, meter")
