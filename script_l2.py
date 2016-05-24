import mcpi.minecraft as minecraft
import time

mc_server = "phaeton.soffice.it"
mc_player = "mnx"

mc = minecraft.Minecraft.create(address=mc_server, name=mc_player)

while True:
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    block = 38
    mc.setBlock(x, y, z, block)
    time.sleep(0.2)