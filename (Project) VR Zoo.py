import viz
import vizcam
import vizfx
import vizshape
import vizinput 
import vizact

#Enable full screen anti-aliasing (FSAA) to smooth edges
viz.setMultiSample(4)

viz.go()

#Increase the Field of View
viz.MainWindow.fov(60)

#prompt for a string
userName = vizinput.input('Hello and Welcome! Please enter your name :)')
print(userName)

#add keyboard navigation
vizcam.WalkNavigate()

vizshape.addAxes()

#add models
viz.addChild('zoologico.osgb')
viz.addChild('sky_day.osgb')
viz.MainView.move([26,0,-1])
viz.collision(viz.OFF)

sun=vizfx.addDirectionalLight()
sun.color(1.0,1.0,0.2875)
sun.setEuler(90,90,0)

aquaria = vizfx.addChild('aquaria.osgb')
aquaria.setPosition([25, 0, 30.5])

fish1 = vizfx.addChild('fish1.osgb')
fish1.setPosition([32, 1, 35])
fish1.setScale([0.01,0.01,0.01])

fish2 = vizfx.addChild('fish1.osgb')
fish2.setPosition([32, 1, 38])
fish2.setScale([0.01,0.01,0.01])

fish3 = vizfx.addChild('fish1.osgb')
fish3.setPosition([30, 1, 35])
fish3.setScale([0.01,0.01,0.01])

cheetah = vizfx.addChild('cheetah.osgb')
cheetah.setPosition([50, 0, 30])

cheetah = vizfx.addChild('cheetah.osgb')
cheetah.setPosition([48, 0, 33])

cheetah = vizfx.addChild('cheetah.osgb')
cheetah.setPosition([50, 0, 38])

cheetah = vizfx.addChild('cheetah.osgb')
cheetah.setPosition([47, 0, 40])

flamingo = vizfx.addChild('flamingo.osgb')
flamingo.setPosition([38, 0, 40])

cageflamingo = vizfx.addChild('cageflamingo.osgb')
cageflamingo.setPosition([35, 0, 38])

zebra=vizfx.addChild('newzebra.osgb')
zebra.setScale([0.5,0.5,0.5])
zebra.setPosition([8,0,35])

rusa=vizfx.addChild('rusa.osgb')
rusa.setScale([1,1,1])
rusa.setPosition([21,0,19])

caribou=vizfx.addChild('caribou.osgb')
caribou.setScale([1,1,1])
caribou.setPosition([18,0,21])

antelope1=vizfx.addChild('antelope.osgb')
antelope1.setScale([1,1,1])
antelope1.setPosition([16,0,21])

antelope2=vizfx.addChild('antelope.osgb')
antelope2.setScale([1,1,1])
antelope2.setPosition([14,0,21])

newcage=vizfx.addChild('newcage.osgb')
newcage.setScale([0.08,0.08,0.08])
newcage.setPosition([10,0,25])

p1=vizfx.addChild('Penguin.osgb')
p1.setScale([1.3,1.3,1.3])
p1.setPosition([14,0,26])

p2=vizfx.addChild('Penguin.osgb')
p2.setScale([1.3,1.3,1.3])
p2.setPosition([16,0,26])

p3=vizfx.addChild('Penguin.osgb')
p3.setScale([1.3,1.3,1.3])
p3.setPosition([14,0,28])

p4=vizfx.addChild('Penguin.osgb')
p4.setScale([1.3,1.3,1.3])
p4.setPosition([15,0,27])

p5=vizfx.addChild('Penguin.osgb')
p5.setScale([1.3,1.3,1.3])
p5.setPosition([16,0,28])

p6=vizfx.addChild('Penguin.osgb')
p6.setScale([1.3,1.3,1.3])
p6.setPosition([17,0,27])

p7=vizfx.addChild('Penguin.osgb')
p7.setScale([1.3,1.3,1.3])
p7.setPosition([18,0,26])

p8=vizfx.addChild('Penguin.osgb')
p8.setScale([1.3,1.3,1.3])
p8.setPosition([18,0,28])

van = vizfx.addChild('van.osgb')
van.setPosition([5.5, 0.5, 0.5])

bench = vizfx.addChild('bench.osgb')
bench.setPosition([25, 0, 10])

bench = vizfx.addChild('bench.osgb')
bench.setPosition([25, 0, 13])

bench = vizfx.addChild('bench.osgb')
bench.setPosition([25.5, 0, 16])

bench = vizfx.addChild('bench.osgb')
bench.setPosition([25.5, 0, 20])

spin=vizact.spin(0,1,0,30)
fish1.addAction(spin)
fish2.addAction(spin)
fish3.addAction(spin)
p1.addAction(spin)
p2.addAction(spin)
p3.addAction(spin)
p4.addAction(spin)
p5.addAction(spin)
p6.addAction(spin)
p7.addAction(spin)
p8.addAction(spin)

water = vizfx.addChild('Water.osgb')
water.setPosition([37.3,0.1,24.4])
water.setScale([1,1,1])

aviary = vizfx.addChild('AVIARY.osgb')
aviary.setPosition([38,0,27])
aviary.setScale([0.9,0.9,0.9])

tree = vizfx.addChild('Tree1.osgb')
tree.setPosition([31,0,20.5])
tree.setScale([2,2,2])

owl1 = vizfx.addChild('owl.osgb')
owl1.setPosition([38.4,1.6,27])
owl1.setScale([0.5,0.5,0.5])

birb = vizfx.addChild('BIRDxYELLOW.osgb')
birb.setPosition([38.5,2,27])
birb.setScale([0.1,0.1,0.1])

avocette = vizfx.addChild('AVOCETTE.osgb')
avocette.setPosition([37.3,0,24.8])
avocette.setScale([0.2,0.2,0.2])

jay = vizfx.addChild('Jay.osgb')
jay.setPosition([38,2.8,27])
jay.setScale([1.1,1.1,1.1])

peafowl = vizfx.addChild('Peafowl.osgb')
peafowl.setPosition([37,0,27])
peafowl.setScale([0.5,0.5,0.5])
spin = vizact.spin(0,0.1,0,10)
peafowl.addAction(spin)

#add audio
mySound = viz.addAudio('cheetahsound.mp3')
vizact.onkeydown('q', mySound.play)
vizact.onkeydown('e', mySound.stop)
mySound.loop(viz.ON)

mySound = viz.addAudio('flamingosound.mp3')
vizact.onkeydown('n', mySound.play)
vizact.onkeydown('b', mySound.stop)
mySound.loop(viz.ON)

mySound=viz.addAudio('penguin sound.mp3')
vizact.onkeydown('c', mySound.play)
vizact.onkeydown('v', mySound.stop)
mySound.loop(viz.ON)

mySound=viz.addAudio('antelope sound.mp3')
vizact.onkeydown('z', mySound.play)
vizact.onkeydown('x', mySound.stop)
mySound.loop(viz.ON)

mySound = viz.addAudio('Birbs.mp3')
vizact.onkeydown( 'p',mySound.play )
vizact.onkeydown( 'o', mySound.stop )
mySound.loop( viz.ON )

#add video
myVideo = viz.addVideo( 'birds-of-paradise-project-introduction_sgCrdWeB_vF9Z.mpg' )
myVideo.setTime(5)
myVideo.play()

myVideo1 = viz.addVideo( 'peacock.mpg' )
myVideo1.setTime(5)
myVideo1.play()

myVideo2 = viz.addVideo( 'Blue Jay.mpg' )
myVideo2.setTime(5)
myVideo2.play()

#use TexQuad as screen and texture with video
myScreen = viz.addTexQuad()
myScreen.texture( myVideo )
myScreen.setPosition([38,3,24])

myScreen = viz.addTexQuad()
myScreen.texture( myVideo1 )
myScreen.setPosition([38,2,24])

myScreen = viz.addTexQuad()
myScreen.texture( myVideo2 )
myScreen.setPosition([38,1,24])

#add environment
viz.addChild('sky_day.osgb') 