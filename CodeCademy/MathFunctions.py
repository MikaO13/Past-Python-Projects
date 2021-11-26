train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp):
  return (f_temp - 32) * 5/9

def c_to_f(c_temp):
  return c_temp * 9 / 5 + 32

def get_force(mass, acceleration):
  return mass * acceleration

def get_energy(mass, c=3*10**8):
  return (mass * c) ** 2

def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

f100_in_celsius = f_to_c(100)
c0_in_fahrenheit = c_to_f(0)
train_force = get_force(train_mass, train_acceleration)

print("The GE train supplies {} Newtons of force.".format(str(train_force)))

bomb_energy = get_energy(bomb_mass)

print("A 1kg bomb supplies {} Joules".format(str(bomb_energy)))

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does {} Joules of work over {} meters.".format(str(train_work), str(train_distance)))