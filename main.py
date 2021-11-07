import gui
import loudnessnormalize as ln

param = gui.getparam()
ln.loudnessnorm(param[0], float(param[1]), float(param[2]))
