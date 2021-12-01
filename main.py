import gui
import loudnessnormalize as ln

param = gui.getparamgui()
ln.loudnessnorm(param[0], param[1], param[2])
